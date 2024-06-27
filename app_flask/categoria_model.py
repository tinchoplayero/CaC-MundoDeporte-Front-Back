from database import get_db

class CategoriaModel:
    def __init__(self):
        pass

    def get_all_categories(self):
        db = None
        cursor = None
        categories = None
        try:
            db = get_db()
            cursor = db.cursor(dictionary=True)
            query = '''
                SELECT id, nombre
                FROM categorias
            '''
            cursor.execute(query)
            categories = cursor.fetchall()
        except Exception as e:
            print(f"Error getting all categories: {e}")
        finally:
            if cursor:
                cursor.close()
            if db:
                db.close()
        return categories

    def add_category(self, nombre):
        db = None
        cursor = None
        try:
            db = get_db()
            cursor = db.cursor()
            query = '''
                INSERT INTO categorias (nombre)
                VALUES (%s)
            '''
            cursor.execute(query, (nombre,))
            db.commit()
        except Exception as e:
            print(f"Error adding category: {e}")
        finally:
            if cursor:
                cursor.close()
            if db:
                db.close()

    def get_category_by_id(self, categoria_id):
        db = None
        cursor = None
        category = None
        try:
            db = get_db()
            cursor = db.cursor(dictionary=True)
            query = "SELECT * FROM categorias WHERE id = %s"
            cursor.execute(query, (categoria_id,))
            category = cursor.fetchone()
        except Exception as e:
            print(f"Error getting category by id: {e}")
        finally:
            if cursor:
                cursor.close()
            if db:
                db.close()
        return category

    def update_category(self, categoria_id, nombre):
        db = None
        cursor = None
        try:
            db = get_db()
            cursor = db.cursor()
            query = '''
                UPDATE categorias
                SET nombre = %s
                WHERE id = %s
            '''
            cursor.execute(query, (nombre, categoria_id))
            db.commit()
        except Exception as e:
            print(f"Error updating category: {e}")
        finally:
            if cursor:
                cursor.close()
            if db:
                db.close()

    def delete_category(self, categoria_id):
        db = None
        cursor = None
        try:
            db = get_db()
            cursor = db.cursor()
            query = "DELETE FROM categorias WHERE id = %s"
            cursor.execute(query, (categoria_id,))
            db.commit()
        except Exception as e:
            print(f"Error deleting category: {e}")
        finally:
            if cursor:
                cursor.close()
            if db:
                db.close()
