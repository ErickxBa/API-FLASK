from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

# Archivo para persistencia del inventario
INVENTARIO_FILE = "inventario.json"

# Funciones para manejar el inventario

def cargar_inventario():
    """Carga el inventario desde un archivo JSON."""
    if os.path.exists(INVENTARIO_FILE):
        with open(INVENTARIO_FILE, "r") as file:
            return json.load(file)
    return {}

def guardar_inventario():
    """Guarda el inventario en un archivo JSON."""
    with open(INVENTARIO_FILE, "w") as file:
        json.dump(inventario, file, indent=4)

inventario = cargar_inventario()

# Parte 1: Programación Defensiva
def consultar_producto(id_producto):
    if not isinstance(id_producto, int) or id_producto <= 0:
        return {"error": "El ID del producto debe ser un número entero positivo."}, 400
    producto = inventario.get(str(id_producto))
    if not producto:
        return {"error": "Producto no encontrado."}, 404
    return {"nombre": producto["nombre"], "cantidad": producto["cantidad"]}, 200

def agregar_producto(id_producto, nombre, cantidad):
    if not isinstance(id_producto, int) or id_producto <= 0:
        return {"error": "El ID del producto debe ser un número entero positivo."}, 400
    if not isinstance(cantidad, int) or cantidad <= 0:
        return {"error": "La cantidad debe ser un número entero positivo."}, 400
    if not nombre or not isinstance(nombre, str):
        return {"error": "El nombre del producto debe ser una cadena válida."}, 400
    if str(id_producto) in inventario:
        return {"error": "El producto con este ID ya existe."}, 400
    inventario[str(id_producto)] = {"nombre": nombre, "cantidad": cantidad}
    guardar_inventario()
    return {"message": "Producto agregado correctamente."}, 201

# Parte 2: Programación por Contrato y Aserciones
def actualizar_stock(id_producto, nueva_cantidad):
    if not isinstance(id_producto, int) or id_producto <= 0:
        return {"error": "El ID del producto debe ser un número entero positivo."}, 400
    if not isinstance(nueva_cantidad, int) or nueva_cantidad < 0:
        return {"error": "La cantidad debe ser un número entero no negativo."}, 400

    producto = inventario.get(str(id_producto))
    if not producto:
        return {"error": "Producto no encontrado."}, 404

    producto["cantidad"] = nueva_cantidad
    guardar_inventario()
    return {"message": "Stock actualizado correctamente."}, 200

# Parte 3: Creación de la API
@app.route('/producto/<int:id_producto>', methods=['GET'])
def get_producto(id_producto):
    return consultar_producto(id_producto)

@app.route('/producto', methods=['POST'])
def post_producto():
    datos = request.get_json()
    id_producto = datos.get("id_producto")
    nombre = datos.get("nombre")
    cantidad = datos.get("cantidad")
    return agregar_producto(id_producto, nombre, cantidad)

@app.route('/producto/<int:id_producto>', methods=['PUT'])
def put_producto(id_producto):
    datos = request.get_json()
    nueva_cantidad = datos.get("cantidad")
    return actualizar_stock(id_producto, nueva_cantidad)

# Ruta para la interfaz HTML
@app.route('/')
def home():
    return render_template('index.html')

# Ejecución de la aplicación
if __name__ == '__main__':
    app.run(debug=True)
