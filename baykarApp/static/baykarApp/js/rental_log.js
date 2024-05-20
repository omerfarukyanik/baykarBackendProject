$(document).ready(function () {
    $('#rentalLogsTable').DataTable({
        "paging": true,
        "searching": true,
        "ordering": true,
        "info": true,
    });
});

function openEditModal(button) {
    // Get the closest table row
    const row = button.closest('tr');
    const rentalLogId = row.dataset.rentalLogId;
    const data_fields = {
        "product": {
            "name": row.children[2].innerText,
            "price": row.children[4].innerText,
        },
        "user": {
            "username": row.children[1].innerText
        },
        "log_time": row.children[0].innerText,
        "quantity": row.children[3].innerText,
        "total_cost": row.children[5].innerText,
        "log_id": rentalLogId
    }

    // Populate the modal fields with data
    document.getElementById('productName').innerText = data_fields.product.name;
    document.getElementById('quantity').value = data_fields.quantity;
    document.getElementById('unitCost').value = data_fields.product.price;
    document.getElementById('rentalLogEditDialogRentalId').value = data_fields.log_id;

    // Show the modal
    document.getElementById('editModal').classList.remove('hidden');
}

// Function to close the edit modal
function closeEditModal() {
    document.getElementById('editModal').classList.add('hidden');
}

// Function to save changes
function saveChanges() {
    // Get data from the modal fields
    const productName = document.getElementById('productName').value;
    const quantity = document.getElementById('quantity').value;
    const unitCost = document.getElementById('unitCost').value;
    const rentalId = document.getElementById('rentalLogEditDialogRentalId').value;

    // Implement your logic to save changes (e.g., send an AJAX request to your server)

    // Close the modal after saving
    closeEditModal();
}