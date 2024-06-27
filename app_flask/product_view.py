from flask import jsonify
from product_model import ProductModel

class ProductView:
    def __init__(self):
        self.product_model = ProductModel()

    def get_all_products(self):
        try:
            products = self.product_model.get_all_products()
            return jsonify(products), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def add_product(self, data):
        nombre = data.get('nombre')
        descripcion = data.get('descripcion')
        precio = data.get('precio')
        stock = data.get('stock')
        imagen = data.get('imagen')
        cat_id = data.get('cat_id')

        if not nombre or not descripcion or not precio or not stock or not cat_id:
            return jsonify({'error': 'Faltan datos necesarios'}), 400

        try:
            self.product_model.add_product(nombre, descripcion, precio, stock, imagen, cat_id)
            return jsonify({'success': 'Producto agregado correctamente'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def get_product(self, product_id):
        try:
            product = self.product_model.get_product_by_id(product_id)
            if product:
                return jsonify(product), 200
            else:
                return jsonify({'error': 'Producto no encontrado'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def update_product(self, product_id, data):
        nombre = data.get('nombre')
        descripcion = data.get('descripcion')
        precio = data.get('precio')
        stock = data.get('stock')
        imagen = data.get('imagen')
        cat_id = data.get('cat_id')

        if not nombre or not descripcion or not precio or not stock or not cat_id:
            return jsonify({'error': 'Faltan datos necesarios'}), 400

        try:
            self.product_model.update_product(product_id, nombre, descripcion, precio, stock, imagen, cat_id)
            return jsonify({'success': 'Producto actualizado correctamente'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def delete_product(self, product_id):
        try:
            self.product_model.delete_product(product_id)
            return jsonify({'success': 'Producto eliminado exitosamente'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
