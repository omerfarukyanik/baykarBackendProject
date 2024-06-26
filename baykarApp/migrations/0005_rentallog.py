# Generated by Django 5.0.6 on 2024-05-20 08:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baykarApp', '0004_alter_cart_quantity'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RentalLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_time', models.DateTimeField(auto_now_add=True)),
                ('rental_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rental_amount', models.PositiveIntegerField()),
                ('rental_unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baykarApp.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-rental_time'],
            },
        ),
    ]
