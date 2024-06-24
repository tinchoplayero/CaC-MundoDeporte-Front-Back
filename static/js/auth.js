document.addEventListener('DOMContentLoaded', function() {
    const isLoggedIn = localStorage.getItem('isLoggedIn');
    const username = localStorage.getItem('nombre');
    const isAdmin = localStorage.getItem('isAdmin');
    const loginRegisterLink = document.querySelector('.login-register');
    const carritoAdminLink = document.querySelector('.cart');
    const container = document.querySelector('.container');

    const currentPath = window.location.pathname;
    
    if (isLoggedIn && isLoggedIn === 'true') {
        // Oculto el enlace de iniciar sesión
        if (username) {
            document.title += username;
        }
        if (loginRegisterLink) {
            loginRegisterLink.style.display = 'none';
        }

        // Creo enlace de cierre de sesión
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
            carritoAdminLink.style.display = 'none';
            const adminElement = document.createElement('a');
            adminElement.className = 'cart';
            adminElement.href = 'templates/usuarios.html';
            adminElement.innerHTML = '<img src="static/img/users.png" width="20px" height="25px"> Administración de Usuarios';
            container.appendChild(adminElement);
        }
    } else {
        if (loginRegisterLink) {
            loginRegisterLink.style.display = 'block';
        }
    }
});

function logout() {
    localStorage.removeItem('isLoggedIn');
    localStorage.removeItem('isAdmin');
    location.reload(); //Refresca la página
}
