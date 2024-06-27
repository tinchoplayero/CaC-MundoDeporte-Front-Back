import os #Manejador de sistema operativa
import mysql.connector #Conector a la base de datos
from flask import g #Variable global de flask
from dotenv import load_dotenv #Libreria para la ubicación del .env

load_dotenv() #Busca el archivo .env por defecto en la raiz del proyecto

DATABASE_CONFIG = {#Creo un diccionario con la info que viene del .env que voy a usar para conectar a la BD
    'user' : os.getenv('DB_USERNAME'),
    'password' : os.getenv('DB_PASSWORD'),
    'host' : os.getenv('DB_HOST'),
    'port' : os.getenv('DB_PORT'),
    'database' : os.getenv('DB_NAME')
}

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(**DATABASE_CONFIG)#Le paso al conector el diccionario del .env
    return g.db

def close_db(e = None):#Funcion para cerrar la base de dato.
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_app(app): ##Inicia la aplicación con la conexion a la base de datos.
    app.teardown_appcontext(close_db)