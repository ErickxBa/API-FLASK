import unittest
from app import app, cargar_inventario, guardar_inventario
import json
import os

class TestInventarioAPI(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        app.testing = True
        self.inventario_inicial = {
            "1": {"nombre": "Producto A", "cantidad": 50},
            "2": {"nombre": "Producto B", "cantidad": 30}
        }
        with open("inventario.json", "w") as file:
            json.dump(self.inventario_inicial, file)

    def tearDown(self):
        if os.path.exists("inventario.json"):
            os.remove("inventario.json")

    def test_get_producto_existente(self):
        response = self.client.get('/producto/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"nombre": "Producto A", "cantidad": 50})

    def test_get_producto_inexistente(self):
        response = self.client.get('/producto/999')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json["error"], "Producto no encontrado.")

    def test_post_producto_valido(self):
        response = self.client.post('/producto', json={"id_producto": 3, "nombre": "Producto C", "cantidad": 20})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["message"], "Producto agregado correctamente.")

    def test_post_producto_existente(self):
        response = self.client.post('/producto', json={"id_producto": 1, "nombre": "Producto A", "cantidad": 50})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json["error"], "El producto con este ID ya existe.")

    def test_put_producto_valido(self):
        response = self.client.put('/producto/1', json={"cantidad": 100})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["message"], "Stock actualizado correctamente.")

    def test_put_producto_inexistente(self):
        response = self.client.put('/producto/999', json={"cantidad": 100})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json["error"], "Producto no encontrado.")

if __name__ == "__main__":
    unittest.main()
