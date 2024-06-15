import mysql.connector

class UserModel:
    def __init__(self):
        self.connection = None

    def connect(self):
        if not self.connection or not self.connection.is_connected():
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='cacpython',
                database='mundo_deporte'
            )

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()

    def add_user(self, nombre, email, contrasenia, admin):
        self.connect()
        cursor = self.connection.cursor()
        query = """
        INSERT INTO usuarios (nombre, email, contrasenia, admin) 
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (nombre, email, contrasenia, admin))
        self.connection.commit()
        cursor.close()
        self.close()

    def get_user_by_email(self, email):
        self.connect()
        cursor = self.connection.cursor(dictionary=True)
        query = "SELECT * FROM usuarios WHERE email = %s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()
        cursor.close()
        self.close()
        return user

    def get_all_users(self):
        self.connect()
        cursor = self.connection.cursor(dictionary=True)
        query = "SELECT * FROM usuarios"
        cursor.execute(query)
        users = cursor.fetchall()
        cursor.close()
        self.close()
        return users

    def delete_user(self, user_id):
        self.connect()
        cursor = self.connection.cursor()
        query = "DELETE FROM usuarios WHERE id = %s"
        cursor.execute(query, (user_id,))
        self.connection.commit()
        cursor.close()
        self.close()

    def update_user(self, user_id, nombre, email, contrasenia, admin):
        self.connect()
        cursor = self.connection.cursor()
        query = """
        UPDATE usuarios 
        SET nombre = %s, email = %s, contrasenia = %s, admin = %s
        WHERE id = %s
        """
        cursor.execute(query, (nombre, email, contrasenia, admin, user_id))
        self.connection.commit()
        cursor.close()
        self.close()
