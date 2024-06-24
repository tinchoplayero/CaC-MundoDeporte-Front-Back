document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();

    clean_localStorage()
    
    const email = document.getElementById('uname').value;
    const contrasenia = document.getElementById('pass').value;

    fetch('http://127.0.0.1:5000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, contrasenia })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success === 'Inicio de sesión exitoso') {
            alert('Inicio de sesión exitoso');
            localStorage.setItem('isLoggedIn', 'true');//Guardo en el localStorage que ya se encuetra logueado el ususario
            localStorage.setItem('isAdmin', data.isAdmin ? 'true' : 'false');
            localStorage.setItem('nombre', data.nombre)
            window.location.href = '../index.html'; // Redirigir al inicio
        } else {
            alert('Email o contraseña incorrectos');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Hubo un error en el inicio de sesión');
    });
});

function clean_localStorage() {
    if (localStorage.getItem('isLoggedIn')) {
        localStorage.removeItem('isLoggedIn');
    }

    if (localStorage.getItem('isAdmin')) {
        localStorage.removeItem('isAdmin');
    }

    if (localStorage.getItem('nombre')) {
        localStorage.removeItem('nombre');
    }
}
