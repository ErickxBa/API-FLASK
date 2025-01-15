# API de Inventario

Esta es una API simple de inventario que permite consultar, agregar y actualizar productos. Incluye una interfaz web básica y pruebas automatizadas para garantizar su correcto funcionamiento.

---

## Funcionalidades

### **1. Consultar Producto**

Permite consultar un producto por su ID.

- **Ruta**: `GET /producto/<int:id_producto>`
- **Parámetros**: El ID del producto como un entero positivo.
- **Respuesta**:
  - Si el producto existe:
    ```json
    {
        "nombre": "Producto A",
        "cantidad": 50
    }
    ```
  - Si el producto no existe:
    ```json
    {
        "error": "Producto no encontrado."
    }
    ```

### **2. Agregar Producto**

Permite agregar un nuevo producto al inventario.

- **Ruta**: `POST /producto`
- **Cuerpo de la Solicitud**:
  ```json
  {
      "id_producto": 1,
      "nombre": "Producto A",
      "cantidad": 50
  }
  ```
- **Respuesta**:
  - Si se agrega correctamente:
    ```json
    {
        "message": "Producto agregado correctamente."
    }
    ```
  - Si el ID del producto ya existe:
    ```json
    {
        "error": "El producto con este ID ya existe."
    }
    ```

### **3. Actualizar Stock**

Permite actualizar la cantidad de un producto existente.

- **Ruta**: `PUT /producto/<int:id_producto>`
- **Cuerpo de la Solicitud**:
  ```json
  {
      "cantidad": 100
  }
  ```
- **Respuesta**:
  - Si el stock se actualiza correctamente:
    ```json
    {
        "message": "Stock actualizado correctamente."
    }
    ```
  - Si el producto no existe:
    ```json
    {
        "error": "Producto no encontrado."
    }
    ```

---

## Requisitos

- **Python** 3.7+
- Bibliotecas:
  - Flask
  - json
  - unittest

Para instalar Flask, ejecuta:

```bash
pip install flask
```

---

## Configuración del Proyecto

### **Estructura de Archivos**

```
/tu_proyecto
├── app.py
├── inventario.json
├── templates
│   └── index.html
├── static
│   ├── styles.css
│   └── scripts.js
├── test_app.py
```

### **Archivo** **`inventario.json`**

Este archivo almacena los productos del inventario. Este archivo para poderse ejecutar las pruebas unitarias tiene que mantenerse con estos mismo datos. 

###Ejemplo:

```json
{
    "1": {
        "nombre": "Producto A",
        "cantidad": 50
    },
    "2": {
        "nombre": "Producto B",
        "cantidad": 30
    }
}
```

### **Archivo ** **`app.py`**

Contiene el código principal de la API, incluyendo las rutas y la lógica para manejar el inventario.

### **Archivo ** **`index.html`**

Una interfaz básica para interactuar con la API desde el navegador.

### **Archivo ** **`styles.css`**

Estilos para la interfaz web.

### **Archivo ** **`scripts.js`**

Contiene la lógica de JavaScript para enviar solicitudes a la API y mostrar las respuestas.

### **Archivo ** **`test_app.py`**

Pruebas unitarias para verificar el correcto funcionamiento de la API.

---

## Ejecución

1. Iniciar el servidor Flask:

   ```bash
   python app.py
   ```

2. Abrir el navegador y ve a:

   ```
   http://127.0.0.1:5000/
   ```

3. Usa la interfaz para interactuar con la API.

---

## Pruebas

El archivo `test_app.py` contiene pruebas para las rutas principales de la API.

### **Ejecutar las Pruebas**

Ejecuta el siguiente comando:

```bash
python test_app.py
```

### **Casos de Prueba**

1. **Consultar Producto Existente:** Verifica que un producto existente sea retornado correctamente.
2. **Consultar Producto Inexistente:** Verifica que se devuelva un error 404 cuando se consulta un producto inexistente.
3. **Agregar Producto Válido:** Verifica que un producto nuevo pueda ser agregado al inventario.
4. **Agregar Producto Existente:** Verifica que no se pueda agregar un producto con un ID duplicado.
5. **Actualizar Stock Válido:** Verifica que el stock de un producto existente pueda ser actualizado.
6. **Actualizar Producto Inexistente:** Verifica que se devuelva un error 404 al intentar actualizar un producto que no existe.



