#import mysql.connector
from database import *

class UserModel:
    def __init__(self):
        pass

    def add_user(self, nombre, email, contrasenia, admin):
        db = None
        cursor = None
        try:
            db = get_db()
            cursor = db.cursor()
            query = """
            INSERT INTO usuarios (nombre, email, contrasenia, admin) 
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (nombre, email, contrasenia, admin))
            db.commit()
        except Exception as e:
            print(f"Error adding user: {e}")
        finally:
            if cursor:
                cursor.close()
            if db:
                db.close()

    def get_user_by_email(self, email):
        db = None
        cursor = None
        user = None
        try:
            db = get_db()
            cursor = db.cursor(dictionary=True)
            query = "SELECT * FROM usuarios WHERE email = %s"
            cursor.execute(query, (email,))
            user = cursor.fetchone()
        except Exception as e:
            print(f"Error getting user by email: {e}")
        finally:
            if cursor:
                cursor.close()
            if db:
                db.close()
        return user

    @staticmethod #Lo designo como método estático para poder usarlo sin necesidad de instanciar el objeto UserModel
    def get_all_users():
        db = None
        cursor = None
        users = None
        try:
            db = get_db()
            cursor = db.cursor(dictionary=True)
            query = "SELECT * FROM usuarios"
            cursor.execute(query)
            users = cursor.fetchall()
        except Exception as e:
            print(f"Error getting all users: {e}")
        finally:
            if cursor:
                cursor.close()
            if db:
                db.close()
        return users

    def delete_user(self, user_id):
        db = None
        cursor = None
        try:
            db = get_db()
            cursor = db.cursor()
            query = "DELETE FROM usuarios WHERE id = %s"
            cursor.execute(query, (user_id,))
            db.commit()
        except Exception as e:
            print(f"Error deleting user: {e}")
        finally:
            if cursor:
                cursor.close()
            if db:
                db.close()

    def update_user(self, user_id, nombre, email, contrasenia, admin):
        db = None
        cursor = None
        try:
            db = get_db()
            cursor = db.cursor()
            query = """
            UPDATE usuarios 
            SET nombre = %s, email = %s, contrasenia = %s, admin = %s
            WHERE id = %s
            """
            cursor.execute(query, (nombre, email, contrasenia, admin, user_id))
            db.commit()
        except Exception as e:
            print(f"Error updating user: {e}")
        finally:
            if cursor:
                cursor.close()
            if db:
                db.close()
