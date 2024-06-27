from flask import jsonify #Importo el metodo para convertir a json las respuestas de los metodos
from model import UserModel #Importo el modelo de la tabla usuarios

class UserView:
    def __init__(self):#Instancio en el contructor el modelo de la tabla
        self.user_model = UserModel()

    #Método para el registro de ususarios
    def register_user(self, data):
        nombre = data.get('nombre')
        email = data.get('email')
        contrasenia = data.get('contrasenia')
        admin = data.get('admin', False)#El atributo admin recibe por defecto el valor falso para que cuando se use el metodo desde el registro de una persona externa, que no trae ese dato, se cargue bien la query

        if not nombre or not email or not contrasenia:
            return jsonify({'error': 'Faltan datos necesarios'}), 400 #Si falta algun dato devuelvo el error

        try:
            self.user_model.add_user(nombre, email, contrasenia, admin) #Ejecuto el guardado de usuario con el metodo del modelo
            return jsonify({'success': 'Usuario registrado exitosamente'}), 201
        except Exception as e: #Manejo las posibles excepciones y devuelvo el error para ser mostrado al usuario
            return jsonify({'error': str(e)}), 500

    #metodo de logueo
    def login_user(self, data):
        email = data.get('email')
        contrasenia = data.get('contrasenia')

        if not email or not contrasenia: #Si falta algun dato devuelvo la respuesta y salgo del metodo para evitar errores
            return jsonify({'error': 'Faltan datos necesarios'}), 400

        user = self.user_model.get_user_by_email(email) #Declaro la variable y guardo el resultado de la consulta al modelo.
        if user and user['email'] == email and user['contrasenia'] == contrasenia: # type:ignore
            #Uso type ignore para evitar que VSCode me de un error porque intento acceder a un diccionario antes de que se produsca.
            #Comparo su hay un par email contrasenia que coincidan y devuelvo success o error.
            return jsonify({'success': 'Inicio de sesión exitoso', 'isAdmin' : user['admin'], 'nombre': user['nombre']}), 200 # type: ignore
        else:
            return jsonify({'error': 'Email o contraseña incorrectos'}), 401

    #Metodo para traer 1 solo usuario a traves del correo electrónico
    def get_user(self, data):
        try:
            user = self.user_model.get_user_by_email(data)
            return jsonify(user), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    #método para traer todos los ususarios
    def get_all_users(self):
        try:
            users = self.user_model.get_all_users()
            return jsonify(users), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    #Borra ususarios
    def delete_user(self, user_id):
        try:
            self.user_model.delete_user(user_id)
            return jsonify({'success': 'Usuario eliminado exitosamente'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    #Edita usuarios
    def edit_user(self, user_id, data):
        nombre = data.get('nombre')
        email = data.get('email')
        contrasenia = data.get('contrasenia')
        admin = data.get('admin')

        if not nombre or not email or not contrasenia or admin is None:
            return jsonify({'error': 'Faltan datos necesarios'}), 400

        try:
            self.user_model.update_user(user_id, nombre, email, contrasenia, admin)
            return jsonify({'success': 'Usuario actualizado exitosamente'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        
        
