from flask import Flask, request, jsonify
from flask_cors import CORS #Incorpore esto porque me arrojaba un error
from views import UserView
from database import init_app #importo desde el conecto la conección a la base de datos 

app = Flask(__name__)
init_app(app)
CORS(app)

user_view = UserView()

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    return user_view.register_user(data)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    return user_view.login_user(data)

@app.route('/users', methods=['GET'])
def users():
    return user_view.get_all_users()

@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete(user_id):
    return user_view.delete_user(user_id)

@app.route('/user/<int:user_id>', methods=['PUT'])
def edit(user_id):
    data = request.json
    return user_view.edit_user(user_id, data)

if __name__ == '__main__':
    app.run(debug=True)
