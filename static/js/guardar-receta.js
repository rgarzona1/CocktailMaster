function getCookie(name) {

    let cookieValue = null;

    if (document.cookie && document.cookie !== "") {

        const cookies = document.cookie.split(";");

        for (let cookie of cookies) {

            cookie = cookie.trim();

            if (cookie.startsWith(name + "=")) {

                cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1)
                );

                break;
            }
        }
    }

    return cookieValue;
}


document.addEventListener("DOMContentLoaded", () => {

    const botonGuardar = document.getElementById("btn-guardar-receta");

    if (!botonGuardar) {
        return;
    }

    botonGuardar.addEventListener("click", async () => {

        const cocktailId = botonGuardar.dataset.cocktailId;
        const nombre = botonGuardar.dataset.nombre;
        const categoria = botonGuardar.dataset.categoria;
        const tipo = botonGuardar.dataset.tipo;
        const instrucciones = botonGuardar.dataset.instrucciones;
        const imagen = botonGuardar.dataset.imagen;

        const datos = {
            cocktaildb_id: cocktailId,
            nombre: nombre,
            categoria: categoria,
            tipo_bebida: tipo,
            instrucciones: instrucciones,
            imagen: imagen
        };

        try {

            const response = await fetch("/perfil/api/recetas-guardadas/", {
                method: "POST",

                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCookie("csrftoken")
                },

                body: JSON.stringify(datos)
            });

            if (response.ok) {

                alert("Receta guardada correctamente.");

                botonGuardar.textContent = "Receta guardada";
                botonGuardar.disabled = true;

            } else {

                const error = await response.text();

                console.error("Error:", error);

            }

        } catch (error) {

            console.error("Error al guardar la receta:", error);

        }
    });
});