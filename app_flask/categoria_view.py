from flask import jsonify, request
from categoria_model import CategoriaModel

class CategoriaView:
    def __init__(self):
        self.categoria_model = CategoriaModel()

    def get_all_categories(self):
        try:
            categories = self.categoria_model.get_all_categories()
            return jsonify(categories), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def add_category(self):
        data = request.json
        nombre = data.get('nombre')

        if not nombre:
            return jsonify({'error': 'Falta el nombre de la categoría'}), 400

        try:
            self.categoria_model.add_category(nombre)
            return jsonify({'success': 'Categoría agregada correctamente'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def get_category(self, categoria_id):
        try:
            category = self.categoria_model.get_category_by_id(categoria_id)
            if category:
                return jsonify(category), 200
            else:
                return jsonify({'error': 'Categoría no encontrada'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def update_category(self, categoria_id):
        data = request.json
        nombre = data.get('nombre')

        if not nombre:
            return jsonify({'error': 'Falta el nombre de la categoría'}), 400

        try:
            self.categoria_model.update_category(categoria_id, nombre)
            return jsonify({'success': 'Categoría actualizada correctamente'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def delete_category(self, categoria_id):
        try:
            self.categoria_model.delete_category(categoria_id)
            return jsonify({'success': 'Categoría eliminada exitosamente'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
