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
    cur.execute('SELECT * FROM productos')
    dato = cur.fetchall()
    return render_template('producto_nuevo.html', productos = dato)

@app.route('/agregar_productos', methods=['POST'])
def agregar_productos():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        stock = request.form['stock']
        imagen = request.form['imagen']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO productos (nombre, descripcion, precio, stock, imagen) VALUES (%s, %s, %s, %s, %s)',(nombre, descripcion, precio, stock, imagen))
        mysql.connection.commit()
        flash('Producto agregado correctamente')
        return redirect(url_for('productos'))


@app.route('/editar/<id>')
def edit_productos(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM productos WHERE id = %s', (id))
    dato = cur.fetchall()
    return render_template('producto_editar.html', producto = dato[0])

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