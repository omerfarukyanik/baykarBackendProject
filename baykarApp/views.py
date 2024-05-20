from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import Http404, HttpResponseNotAllowed

from .forms import RentalLogForm
from .models import Product, Cart, RentalLog
from .utils import serialize_messages


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        user = authenticate(username=username, password=password1)
        if user is not None:
            login(request, user)
            messages.success(request, "Signup successful")
            return redirect('main_page')
        else:
            messages.error(request, "Authentication failed")
            return redirect('signup')

    context = serialize_messages(messages, request)
    return render(request, 'signup.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect('home_page')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    context = serialize_messages(messages, request)
    return render(request, 'login.html', context)


@login_required
def home_page(request):
    return render(request, 'home_page.html')


@login_required
def list_products(request):
    products = Product.objects.all()
    context = serialize_messages(messages, request)
    context["products"] = products
    return render(request, 'all_products.html', context)


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_entry, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_entry.quantity += 1
        cart_entry.save()
    messages.success(request, f"Added <strong>{product.name}</strong> to your cart.")
    # Handle redirection based on the 'next' parameter
    next_page = request.GET.get('next', 'cart_view')  # Default to view_cart if no 'next' parameter is provided
    return redirect(next_page)


@login_required
def view_cart(request):
    cart_entries = Cart.objects.filter(user=request.user)

    context = serialize_messages(messages, request)

    sub_total = 0
    for cart_entry in cart_entries:
        sub_total += cart_entry.quantity * cart_entry.product.price

    cart_entries.sub_total = sub_total
    cart_entries.total = sub_total + 45
    context["cart_entries"] = cart_entries

    return render(request, 'cart.html', context)


@login_required
def remove_from_cart(request, product_id):
    try:
        cart_entry = get_object_or_404(Cart, product=product_id, user=request.user)
    except Http404 as e:
        messages.error(request, "Cart entry does not exist")
        return redirect('view_cart')
    if cart_entry.quantity == 1:
        cart_entry.delete()
    elif cart_entry.quantity > 1:
        cart_entry.quantity -= 1
        cart_entry.save()
    messages.success(request, 'Item removed from cart')
    return redirect('view_cart')


@login_required
def purchase_cart(request):
    if request.method == 'POST':
        cart_entries = Cart.objects.filter(user=request.user)
        for cart_entry in cart_entries:
            rental_log = RentalLog.objects.create(
                user=request.user,
                product=cart_entry.product,
                rental_cost=cart_entry.product.price * cart_entry.quantity,
                rental_amount=cart_entry.quantity,
                rental_unit_price=cart_entry.product.price
            )
            rental_log.save()

        # Clear the cart after purchase
        cart_entries.delete()
        messages.success(request, 'Purchase successful. Rental logs created.')
        return redirect('rental_logs')

    # Handle GET request or other cases
    return HttpResponseNotAllowed(['POST'])


@login_required
def get_rental_logs(request):
    # Get all rental logs
    rental_logs = RentalLog.objects.all()
    context = serialize_messages(messages, request)
    context["rental_logs"] = rental_logs
    return render(request, 'rental_log.html', context)


@login_required
def delete_rental_log(request, log_id):
    try:
        rental_log = RentalLog.objects.get(id=log_id)
        rental_log.delete()
        messages.success(request, "Rental log deleted successfully.")
    except RentalLog.DoesNotExist:
        messages.error(request, "Rental log does not exist.")
    return redirect('rental_logs')


@login_required
def edit_rental_log(request, log_id):
    try:
        rental_log = get_object_or_404(RentalLog, id=log_id, user=request.user)

        if request.method == 'POST':
            form = RentalLogForm(request.POST, instance=rental_log)
            if form.is_valid():
                form.save()
                messages.success(request, "Rental log updated successfully.")
                return redirect('rental_logs')
    except Http404 as e:
        messages.error(request, "Rental log does not exist.")
    return redirect('rental_logs')
