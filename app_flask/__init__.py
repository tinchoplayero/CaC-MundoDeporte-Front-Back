from flask import Flask, request, jsonify
from flask_cors import CORS #Incorpore esto porque me arrojaba un error
from views import UserView
from product_view import ProductView
from categoria_view import CategoriaView
from database import init_app #importo desde la conección a la base de datos 

app = Flask(__name__)
init_app(app)
CORS(app)

user_view = UserView()
product_view = ProductView()
categoria_view = CategoriaView()


#Ruta para el registro de ususarios
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    return user_view.register_user(data)

#Ruta para logueo de usuarios
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    return user_view.login_user(data)

#Ruta para la vista de todos los usuarios
@app.route('/users', methods=['GET'])
def users():
    return user_view.get_all_users()

#Ruta para recuperar 1 solo usuarios a traves del correo
@app.route('/user/<string:user_mail>', methods=['GET'])
def get_user(user_mail):
    return user_view.get_user(user_mail)

#Ruta para borrar ususarios
@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete(user_id):
    return user_view.delete_user(user_id)

#Ruta para editar un usuario
@app.route('/user/<int:user_id>', methods=['PUT'])
def edit(user_id):
    data = request.json
    return user_view.edit_user(user_id, data)

# Rutas para productos
@app.route('/productos', methods=['GET'])
def get_products():
    return product_view.get_all_products()

@app.route('/producto', methods=['POST'])
def add_product():
    data = request.json
    return product_view.add_product(data)

@app.route('/producto/<int:product_id>', methods=['GET'])
def get_product(product_id):
    return product_view.get_product(product_id)

@app.route('/producto/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    return product_view.update_product(product_id, data)

@app.route('/producto/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    return product_view.delete_product(product_id)

# Rutas para categorías
@app.route('/categorias', methods=['GET'])
def get_categories():
    return categoria_view.get_all_categories()

@app.route('/categorias', methods=['POST'])
def add_category():
    return categoria_view.add_category()

@app.route('/categoria/<int:categoria_id>', methods=['GET'])
def get_category(categoria_id):
    return categoria_view.get_category(categoria_id)

@app.route('/categoria/<int:categoria_id>', methods=['PUT'])
def update_category(categoria_id):
    return categoria_view.update_category(categoria_id)

@app.route('/categoria/<int:categoria_id>', methods=['DELETE'])
def delete_category(categoria_id):
    return categoria_view.delete_category(categoria_id)


if __name__ == '__main__':
    app.run(debug=True)
