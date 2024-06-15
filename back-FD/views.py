from flask import jsonify
from model import UserModel

class UserView:
    def __init__(self):
        self.user_model = UserModel()

    def register_user(self, data):
        nombre = data.get('nombre')
        email = data.get('email')
        contrasenia = data.get('contrasenia')
        admin = data.get('admin', False)

        if not nombre or not email or not contrasenia:
            return jsonify({'error': 'Faltan datos necesarios'}), 400

        try:
            self.user_model.add_user(nombre, email, contrasenia, admin)
            return jsonify({'message': 'Usuario registrado exitosamente'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def login_user(self, data):
        email = data.get('email')
        contrasenia = data.get('contrasenia')

        if not email or not contrasenia:
            return jsonify({'error': 'Faltan datos necesarios'}), 400

        user = self.user_model.get_user_by_email(email)
        if user and user['email'] == email and user['contrasenia'] == contrasenia:
            return jsonify({'message': 'Inicio de sesión exitoso', 'isAdmin' : user['admin']}), 200
        else:
            return jsonify({'error': 'Email o contraseña incorrectos'}), 401

    def get_all_users(self):
        try:
            users = self.user_model.get_all_users()
            return jsonify(users), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def delete_user(self, user_id):
        try:
            self.user_model.delete_user(user_id)
            return jsonify({'message': 'Usuario eliminado exitosamente'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def edit_user(self, user_id, data):
        nombre = data.get('nombre')
        email = data.get('email')
        contrasenia = data.get('contrasenia')
        admin = data.get('admin')

        if not nombre or not email or not contrasenia or admin is None:
            return jsonify({'error': 'Faltan datos necesarios'}), 400

        try:
            self.user_model.update_user(user_id, nombre, email, contrasenia, admin)
            return jsonify({'message': 'Usuario actualizado exitosamente'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
