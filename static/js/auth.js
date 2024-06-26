document.addEventListener('DOMContentLoaded', function() {//Este método lo usamos para comprobar si hay un usuario logueado y si este ususario es administrador o no
    const isLoggedIn = localStorage.getItem('isLoggedIn');//REcojo del localStorage si esta logueado, nombre y si es admin
    const username = localStorage.getItem('nombre');
    const isAdmin = localStorage.getItem('isAdmin');
    const loginRegisterLink = document.querySelector('.login-register');//Recojo el containes, el login register y el carrito que vamos a modificar si esta logueado ono y si es administrador o no
    const carritoAdminLink = document.querySelector('.cart');
    const container = document.querySelector('.container');

    const currentPath = window.location.pathname;//Verifico el path para adaptar la busqueda de assets segun si estamos en el index o en otro locación
    
    if (isLoggedIn && isLoggedIn === 'true') {
        // Si ya hay un usuario logueado oculto el enlace de iniciar sesión y le agrego el nombre de ususario el titulo
        if (username) {
            document.title += username;
        }
        if (loginRegisterLink) {
            loginRegisterLink.style.display = 'none';
        }

        // Creo enlace de cierre de sesión en el espacio del grid en que iba el de logueo segun la pagina en la que esta el ususario
        const logoutLink = document.createElement('a');
        logoutLink.href = '#';
        if (currentPath === '/CaC-MundoDeporte-Front-Back/' || currentPath === '/CaC-MundoDeporte-Front-Back/index.html' || currentPath === '/CaC-MundoDeporte-Front-Back/index.html') {
            logoutLink.className = 'logout';
            logoutLink.innerHTML = `
                <img src="static/img/user.png" width="20px" height="20px">
                Salir
            `;
            container.appendChild(logoutLink);
        } else {
            logoutLink.className = "nav-link";
            logoutLink.innerHTML = `
                <img src="../static/img/user.png" width="20px" height="20px">
                Salir
            `;
            // Creo el elemento de lista y agregar el enlace de cierre de sesión
            const logoutListItem = document.createElement('li');
            logoutListItem.className = 'nav-item';
            logoutListItem.appendChild(logoutLink);

            // Agrego el elemento de lista a la lista de navegación
            const navbarNav = document.querySelector('.navbar-nav');
            if (navbarNav) {
                navbarNav.appendChild(logoutListItem);
            }
        }
        logoutLink.onclick = logout;

        //Verifico que si se esta cargadon ususarios.html y no es admin entonces vuevla al index
        if (currentPath === '/CaC-MundoDeporte-Front-Back/templates/usuarios.html') {
            if (!isAdmin || isAdmin !== 'true') {
                alert('No tienes permisos de administrador. Serás redirigido a la página principal.');
                window.location.href = '/CaC-MundoDeporte-Front-Back/';
                return;
            }
        }


        // Aca la idea es que se muestre lo que el administrador puede ver
        if (isAdmin && isAdmin === 'true') {
            if (carritoAdminLink && currentPath != '/CaC-MundoDeporte-Front-Back/templates/usuarios.html') {
                carritoAdminLink.style.display = 'none';
            }
            if (currentPath != '/CaC-MundoDeporte-Front-Back/templates/usuarios.html') {
                const adminElement = document.createElement('a');
                adminElement.className = 'cart';
                adminElement.href = 'templates/usuarios.html';
                adminElement.innerHTML = '<img src="static/img/users.png" width="20px" height="25px"> Administración de Usuarios';
                container.appendChild(adminElement);
            }
            
        }
    } else {
        if (loginRegisterLink) {
            loginRegisterLink.style.display = 'block';
        }
    }
});

function logout() {//Funcion para desloguear un usuario y redirigir al inicio
    if (localStorage.getItem('isLoggedIn')) {
        localStorage.removeItem('isLoggedIn');
        console.log('El elemento isLoggedIn fue eliminado.');
    }

    if (localStorage.getItem('isAdmin')) {
        localStorage.removeItem('isAdmin');
        console.log('El elemento isAdmin fue eliminado.');
    }

    if (localStorage.getItem('nombre')) {
        localStorage.removeItem('nombre');
        console.log('El elemento nombre fue eliminado.');
    }
    window.location.href = '/CaC-MundoDeporte-Front-Back/index.html';
}