function register(){
    let format = /[ `!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~]/;
    let uname=document.getElementById("uname");
    let email=document.getElementById("email");
    let email2=document.getElementById("r-email");
    let pass=document.getElementById("pass");
    let pass2=document.getElementById("pass2");

// ***********************Comprobacion nombre de usuario***************************************

    if (uname.value.length<=0){ 
        // alert("El nombre de usuario no puede estar vacio"); 
        Swal.fire({
            icon: "warning",
            title: "ERROR en el nombre de usuario",
            text: "El nombre de usuario no puede estar vacio",
            confirmButtonText: "OK"
          });
          return false;
    }
    if (uname.value.length>=10){ 
        // alert("El nombre de usuario no puede superar los 10 caracteres"); 
        Swal.fire({
            icon: "warning",
            title: "ERROR en el nombre de usuario",
            text: "El nombre de usuario no puede superar los 10 caracteres",
            confirmButtonText: "OK"
          });
          return false;

    }
    if (format.test(uname.value)){
        //  alert("El nombre de usuario no puede tener caracteres especiales"); 
        Swal.fire({
            icon: "warning",
            title: "ERROR en el nombre de usuario",
            text: "El nombre de usuario no puede tener caracteres especiales",
            confirmButtonText: "OK"
          });
          return false;

    }

// **************************Comprobacion email***************************************
    if(email.value.length<=0 || email2.value.length<=0){
        Swal.fire({
            icon: "warning",
            title: "ERROR en el correo",
            text: "Los correos electronicos no pueden ser vacios",
            confirmButtonText: "OK"
        });
        return false;    
        }    

    if(!(email.value===email2.value)){
            Swal.fire({
                icon: "warning",
                title: "ERROR en el correo",
                text: "Los correos electronicos no son iguales",
                confirmButtonText: "OK"
            });
            return false;    
            }
//**************************************Comprobacion contraseña**********************************

    if(pass.value.length<=0 || pass2.value.length<=0){
        Swal.fire({
            icon: "warning",
            title: "ERROR en la contraseña",
            text: "La contraseña no puede estar vacia",
            confirmButtonText: "OK"
        });
        return false;    
        }    

    if(pass.value.length<=8 || pass2.value.length<=8){
        Swal.fire({
            icon: "warning",
            title: "ERROR en la contraseña",
            text: "La contraseña debe tener 8 o mas caracteres",
            confirmButtonText: "OK"
        });
        return false;    
        }    

    if(!(pass.value===pass2.value)){
            Swal.fire({
                icon: "warning",
                title: "ERROR en la contraseña",
                text: "Las contraseñas no pueden ser distintas",
                confirmButtonText: "OK"
            });
            return false;    
            }
    return true;    //en caso de que no entre a ningun condicional enviara el formulario
}//end function
