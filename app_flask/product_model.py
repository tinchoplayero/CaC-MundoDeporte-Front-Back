from database import get_db

class ProductModel:
    def __init__(self):
        pass

    def get_all_products(self):
        db = None
        cursor = None
        products = None
        try:
            db = get_db()
            cursor = db.cursor(dictionary=True)
            query = '''
                SELECT p.id, p.nombre, p.descripcion, p.precio, p.stock, c.nombre AS categoria, p.imagen
                FROM productos p
                JOIN categorias c ON p.cat_id = c.id
            '''
            cursor.execute(query)
            products = cursor.fetchall()
        except Exception as e:
            print(f"Error getting all products: {e}")
        finally:
            if cursor:
                cursor.close()
            if db:
                db.close()
        return products

    def add_product(self, nombre, descripcion, precio, stock, imagen, cat_id):
        db = None
        cursor = None
        try:
            db = get_db()
            cursor = db.cursor()
            query = '''
                INSERT INTO productos (nombre, descripcion, precio, stock, imagen, cat_id)
                VALUES (%s, %s, %s, %s, %s, %s)
            '''
            cursor.execute(query, (nombre, descripcion, precio, stock, imagen, cat_id))
            db.commit()
        except Exception as e:
            print(f"Error adding product: {e}")
        finally:
            if cursor:
                cursor.close()
            if db:
                db.close()

    def get_product_by_id(self, product_id):
        db = None
        cursor = None
        product = None
        try:
            db = get_db()
            cursor = db.cursor(dictionary=True)
            query = "SELECT * FROM productos WHERE id = %s"
            cursor.execute(query, (product_id,))
            product = cursor.fetchone()
        except Exception as e:
            print(f"Error getting product by id: {e}")
        finally:
            if cursor:
                cursor.close()
            if db:
                db.close()
        return product

    def update_product(self, product_id, nombre, descripcion, precio, stock, imagen, cat_id):
        db = None
        cursor = None
        try:
            db = get_db()
            cursor = db.cursor()
            query = '''
                UPDATE productos
                SET nombre = %s, descripcion = %s, precio = %s, stock = %s, imagen = %s, cat_id = %s
                WHERE id = %s
            '''
            cursor.execute(query, (nombre, descripcion, precio, stock, imagen, cat_id, product_id))
            db.commit()
        except Exception as e:
            print(f"Error updating product: {e}")
        finally:
            if cursor:
                cursor.close()
            if db:
                db.close()

    def delete_product(self, product_id):
        db = None
        cursor = None
        try:
            db = get_db()
            cursor = db.cursor()
            query = "DELETE FROM productos WHERE id = %s"
            cursor.execute(query, (product_id,))
            db.commit()
        except Exception as e:
            print(f"Error deleting product: {e}")
        finally:
            if cursor:
                cursor.close()
            if db:
                db.close()
