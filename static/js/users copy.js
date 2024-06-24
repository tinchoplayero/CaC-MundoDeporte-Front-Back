document.addEventListener('DOMContentLoaded', function () {
    console.log('entropy')
    fetch('http://127.0.0.1:5000/users', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(response => response.json())
        .then(data => {
            const userTableBody = document.getElementById('userTableBody');
            userTableBody.innerHTML = ''; // Clear any existing rows
            data.forEach(user => {
                const row = document.createElement('tr');

                row.innerHTML = `
                    <td>${user.id}</td>
                    <td>${user.nombre}</td>
                    <td>${user.email}</td>
                    <td>${user.admin ? 'Yes' : 'No'}</td>
                    <td>
                        <button class="btn btn-primary btn-sm edit-btn" data-id="${user.id}">Edit</button>
                        <button class="btn btn-danger btn-sm delete-btn" data-id="${user.id}">Delete</button>
                    </td>
                `;

                userTableBody.appendChild(row);
            });

            // Add event listeners for the edit and delete buttons
            document.querySelectorAll('.edit-btn').forEach(button => {
                button.addEventListener('click', handleEdit);
            });

            document.querySelectorAll('.delete-btn').forEach(button => {
                button.addEventListener('click', handleDelete);
            });
        });
});

function handleEdit(event) {
    const userId = event.target.getAttribute('data-id');
    const nombre = prompt("Enter new name:");
    const email = prompt("Enter new email:");
    const contrasenia = prompt("Enter new password:");
    const admin = confirm("Is the user an admin?");

    if (nombre && email && contrasenia) {
        fetch(`http://127.0.0.1:5000/user/${userId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ nombre, email, contrasenia, admin })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                location.reload();
            } else {
                alert('Failed to update user.');
            }
        });
    }
}

function handleDelete(event) {
    const userId = event.target.getAttribute('data-id');

    if (confirm("Are you sure you want to delete this user?")) {
        fetch(`http://127.0.0.1:5000/user/${userId}`, {
            method: 'DELETE'
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                location.reload();
            } else {
                alert('Failed to delete user.');
            }
        });
    }
}
