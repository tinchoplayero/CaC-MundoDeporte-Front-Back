document.addEventListener('DOMContentLoaded', function() {
    const isLoggedIn = localStorage.getItem('isLoggedIn');
    const isAdmin = localStorage.getItem('isAdmin');
    const loginRegisterLink = document.querySelector('.login-register');
    const container = document.querySelector('.container');
    
    if (isLoggedIn && isLoggedIn === 'true') {
        // Oculto el enlace de iniciar sesión
        if (loginRegisterLink) {
            loginRegisterLink.style.display = 'none';
        }

        // Creo enlace de cierre de sesión
        const logoutLink = document.createElement('a');
        logoutLink.className = 'logout';
        logoutLink.href = '#';
        logoutLink.innerHTML = `
            <img src="../static/img/user.png" width="20px" height="20px">
            Salir
        `;
        logoutLink.onclick = logout;

        container.appendChild(logoutLink);

        // Aca la idea es que se muestre lo que el administrador puede ver
        if (isAdmin && isAdmin === 'true') {
            const adminElement = document.createElement('div');
            adminElement.className = 'admin-panel';
            adminElement.innerHTML = '<a href="admin.html">Panel de Administrador</a>';
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
