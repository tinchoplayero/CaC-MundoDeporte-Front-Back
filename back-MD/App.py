from flask import Flask, render_template, request,redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#Conexion SQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASS'] = ''
app.config['MYSQL_DB'] = 'mundo_deporte'
mysql = MySQL(app)

# Configuraciones
app.secret_key = 'misesion'
 
@app.route('/')
def Index():
    return 'Mundo Deporte Admin - Login'

@app.route('/productos')
def productos():
    cur = mysql.connection.cursor()
    
    # TRAE LOS DATOS DE LOS PRODUCTOS
    #cur.execute('SELECT * FROM productos')
    cur.execute('''
        SELECT p.id, p.nombre, p.descripcion, p.precio, p.stock, c.nombre AS categoria, p.imagen
        FROM productos p
        JOIN categorias c ON p.cat_id = c.id
    ''')

    dato = cur.fetchall()
    
    #TRAE LOS DATOS DE LAS CATEGORIAS
    cur.execute('SELECT id, nombre FROM categorias')
    datos_cat = cur.fetchall()

    #PINTO EL HTML Y ME LLEVO LOS DATOS DE PRODUCTOS Y CATEGORIA
    return render_template('producto_nuevo.html', productos = dato, categorias = datos_cat)


@app.route('/agregar_productos', methods=['POST'])
def agregar_productos():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        stock = request.form['stock']
        imagen = request.form['imagen']
        cat_id = request.form['cat_id']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO productos (nombre, descripcion, precio, stock, imagen, cat_id) VALUES (%s, %s, %s, %s, %s, %s)',(nombre, descripcion, precio, stock, imagen, cat_id))
        mysql.connection.commit()
        flash('Producto agregado correctamente')
        return redirect(url_for('productos'))


@app.route('/editar/<id>')
def edit_productos(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM productos WHERE id = %s', (id,))
    producto = cur.fetchone()  
    
    cur.execute('SELECT id, nombre FROM categorias')
    categorias = cur.fetchall()
    
    return render_template('producto_editar.html', producto=producto, categorias=categorias)


@app.route('/modificar/<id>', methods = ['POST'])
def modificar_producto(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        stock = request.form['stock']
        cat_id = request.form['cat_id']
        imagen = request.form['imagen']
        cur = mysql.connection.cursor()
        cur.execute(""" 
        UPDATE productos
        SET nombre = %s,
            descripcion = %s,
            precio = %s,
            stock = %s,
            cat_id = %s,
            imagen = %s
        WHERE id = %s
    """,(nombre, descripcion, precio, stock, cat_id, imagen, id))
        mysql.connection.commit()
        flash("El producto  fue actualizado correctamente")
        return redirect(url_for('productos'))
    


@app.route('/borrar/<id>')
def borrar_productos(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM productos WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('El producto fue eliminado exitosamente')
    return redirect(url_for('productos'))


if __name__ == '__main__':
    app.run(port = 3000, debug = True)