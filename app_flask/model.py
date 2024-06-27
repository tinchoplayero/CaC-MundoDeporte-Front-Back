from database import * #Importo la conecciona a la base de datos

class UserModel:
    def __init__(self): #No le paso argumentos al constructor porque no me interesa mucho usarlo con objeto el model y prefiero que las variables sean locales a cada metodo.
        pass

    def add_user(self, nombre, email, contrasenia, admin):#Metodo para agregar nuevos usuarios
        db = None #Declaro las variables para la base de datos  
        cursor = None
        try:
            db = get_db()#guardo la conección
            cursor = db.cursor() #guardo el cursor
            #Creo la query que voy a ejecutar luego con el cursor
            query = """
            INSERT INTO usuarios (nombre, email, contrasenia, admin) 
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (nombre, email, contrasenia, admin))#Ejecuto la query creada y hago el commit a la base de datos para que se guarden los datos nuevos
            db.commit()
        except Exception as e:#Manejo las excepciones y finalmente cierro el cursos y la conección.
            print(f"Error adding user: {e}")
        finally:
            if cursor:
                cursor.close()
            if db:
                db.close()

    def get_user_by_email(self, email):
        db = None
        cursor = None
        user = None#A diferencia del de agregar declaro una variable para guardar lo que traiga de la base de datos para luego devolverlo a la consulta
        try:
            db = get_db()
            cursor = db.cursor(dictionary=True)
            query = "SELECT * FROM usuarios WHERE email = %s"
            cursor.execute(query, (email,))
            user = cursor.fetchone()#Guardo en la variable la respuesta de la base de datos
        except Exception as e:
            print(f"Error getting user by email: {e}")
        finally:
            if cursor:
                cursor.close()
            if db:
                db.close()
        return user #Devuelvo lo que trajo la consulta

    @staticmethod #Lo designo como método estático para poder usarlo sin necesidad de instanciar el objeto UserModel
    #Metodo para traer todos los usuarios de la base de datos
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

    #Metodo para borrar usuarios
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

    #Método para actualizar un usuario
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
