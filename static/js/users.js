document.addEventListener('DOMContentLoaded', function () {
    fetch('http://127.0.0.1:5000/users', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => { //Aca leo y despliego todos los usuarios que trae la api
        const userTableBody = document.getElementById('userTableBody');
        userTableBody.innerHTML = ''; // Limpio cualquier elemento que pueda tener
        data.forEach(user => {
            const row = document.createElement('tr');

            row.innerHTML = `
                <td>${user.id}</td>
                <td>${user.nombre}</td>
                <td>${user.email}</td>
                <td>${user.admin ? 'Yes' : 'No'}</td>
                <td>
                    <button class="btn btn-primary btn-sm edit-btn" data-id="${user.id}" data-mail="${user.email}" data-bs-toggle="modal" data-bs-target="#userModal">Edit</button>
                    <button class="btn btn-danger btn-sm delete-btn" data-id="${user.id}">Delete</button>
                </td>
            `;

            userTableBody.appendChild(row);
        });

        // Listeners para el edit y el delete
        document.querySelectorAll('.edit-btn').forEach(button => {
            button.addEventListener('click', handleEdit);
        });

        document.querySelectorAll('.delete-btn').forEach(button => {
            button.addEventListener('click', handleDelete);
        });
    });

    // manejador para agregar ususarios
    const addUserBtn = document.getElementById('addUserBtn');
    addUserBtn.addEventListener('click', function() {
        resetModal();
        document.getElementById('userModalLabel').innerText = 'Agregar Usuario';
        document.getElementById('modalSubmitBtn').innerText = 'Agregar Usuario';
    });

    // manejador para el envio de formulario segun sea para edit o para creacio
    const userForm = document.getElementById('userForm');
    userForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const userId = document.getElementById('userId').value;
        const nombre = document.getElementById('userNombre').value;
        const email = document.getElementById('userEmail').value;
        const contrasenia = document.getElementById('userContrasenia').value;
        const admin = document.getElementById('userAdmin').checked;

        const method = userId ? 'PUT' : 'POST';
        const url = userId ? `http://127.0.0.1:5000/user/${userId}` : 'http://127.0.0.1:5000/register';

        fetch(url, {
            method: method,
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ nombre, email, contrasenia, admin })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                resetModal();
                location.reload();
            } else {
                alert('Failed to ' + (userId ? 'update' : 'add') + ' user.');
            }
        });
    });
});

function handleEdit(event) {
    const userMail = event.target.getAttribute('data-mail');
    fetch(`http://127.0.0.1:5000/user/${userMail}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(user => {
        document.getElementById('userId').value = user.id;
        document.getElementById('userNombre').value = user.nombre;
        document.getElementById('userEmail').value = user.email;
        document.getElementById('userContrasenia').value = user.contrasenia;
        document.getElementById('userAdmin').checked = user.admin;

        document.getElementById('userModalLabel').innerText = 'Editar Usuario';
        document.getElementById('modalSubmitBtn').innerText = 'Guardar Cambios';
    });
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

function resetModal() {
    document.getElementById('userId').value = '';
    document.getElementById('userNombre').value = '';
    document.getElementById('userEmail').value = '';
    document.getElementById('userContrasenia').value = '';
    document.getElementById('userAdmin').checked = false;
}
