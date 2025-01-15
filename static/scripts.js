const API_URL = "http://127.0.0.1:5000";

// Consultar Producto
document.getElementById("consultar-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const id = document.getElementById("consultar-id").value;
    const result = document.getElementById("consultar-result");

    try {
        const response = await fetch(`${API_URL}/producto/${id}`);
        const data = await response.json();
        result.textContent = JSON.stringify(data, null, 2);
    } catch (err) {
        result.textContent = "Error al consultar producto.";
    }
});

// Agregar Producto
document.getElementById("agregar-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const id = document.getElementById("agregar-id").value;
    const nombre = document.getElementById("agregar-nombre").value;
    const cantidad = document.getElementById("agregar-cantidad").value;
    const result = document.getElementById("agregar-result");

    try {
        const response = await fetch(`${API_URL}/producto`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ id_producto: parseInt(id), nombre, cantidad: parseInt(cantidad) }),
        });
        const data = await response.json();
        result.textContent = JSON.stringify(data, null, 2);
    } catch (err) {
        result.textContent = "Error al agregar producto.";
    }
});

// Actualizar Stock
document.getElementById("actualizar-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const id = document.getElementById("actualizar-id").value;
    const cantidad = document.getElementById("actualizar-cantidad").value;
    const result = document.getElementById("actualizar-result");

    try {
        const response = await fetch(`${API_URL}/producto/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ cantidad: parseInt(cantidad) }),
        });
        const data = await response.json();
        result.textContent = JSON.stringify(data, null, 2);
    } catch (err) {
        result.textContent = "Error al actualizar stock.";
    }
});
