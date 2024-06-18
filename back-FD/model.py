#import mysql.connector
from database import *

class UserModel:
    def __init__(self):
        pass

    def add_user(self, nombre, email, contrasenia, admin):
        db = get_db()
        cursor = db.cursor()
        query = """
        INSERT INTO usuarios (nombre, email, contrasenia, admin) 
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (nombre, email, contrasenia, admin))
        db.commit()
        cursor.close()

    def get_user_by_email(self, email):
        db = get_db()
        cursor = db.cursor(dictionary=True)#Agrego el parámetro dictionary porque devuelve diccionarios en lugar de tuplas.
        query = "SELECT * FROM usuarios WHERE email = %s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()
        cursor.close()
        return user

    @staticmethod #Uso el decorador para indicar que es estatico y no se necesita instanciar
    def get_all_users(): #No lleva self porque es estatico.
        db = get_db()
        cursor = db.cursor(dictionary=True)#Agrego el parámetro dictionary porque devuelve diccionarios en lugar de tuplas.
        query = "SELECT * FROM users"
        cursor.execute(query)
        users = cursor.fetchall()
        cursor.close()
        return users

    def delete_user(self, user_id):
        db = get_db()
        cursor = db.cursor()
        query = "DELETE FROM usuarios WHERE id = %s"
        cursor.execute(query, (user_id,))
        db.commit()
        cursor.close()

    def update_user(self, user_id, nombre, email, contrasenia, admin):
        db = get_db()
        cursor = db.cursor()
        query = """
        UPDATE usuarios 
        SET nombre = %s, email = %s, contrasenia = %s, admin = %s
        WHERE id = %s
        """
        cursor.execute(query, (nombre, email, contrasenia, admin, user_id))
        db.commit()
        cursor.close()
     
