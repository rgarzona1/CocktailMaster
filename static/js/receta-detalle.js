
// Obtener ID desde la URL

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // ¿Coincide el nombre?
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const pathParts = window.location.pathname.split("/");
const recetaId = pathParts[pathParts.length - 2]; 

if (!recetaId) {
    alert("No se especificó la receta.");
    window.location.href = "/perfil/dashboard/";
}


//Cargar receta desde API

async function cargarReceta() {
    try {
        const token = localStorage.getItem("access");

        const resp = await fetch(`/perfil/api/recetas-creadas/${recetaId}/`, {
            headers: {
                "Authorization": `Bearer ${token}`
            }
        });

        if (!resp.ok) {
            throw new Error("Error al obtener la receta");
        }

        const data = await resp.json();

        document.getElementById("titulo").textContent = data.nombre;
        document.getElementById("descripcion").textContent = data.descripcion;
        document.getElementById("ingredientes").textContent = data.ingredientes;
        document.getElementById("preparacion").textContent = data.preparacion;
        document.getElementById("fecha").textContent = new Date(data.fecha_creacion).toLocaleDateString();

        // Imagen
        if (data.imagen) {
            const img = document.getElementById("imagen");
            img.src = data.imagen;
            img.style.display = "block";
        }

    } catch (e) {
        console.error(e);
        alert("No se pudo cargar la receta.");
    }
}

// 3. Botón Editar

document.getElementById("btnEditar").addEventListener("click", () => {
    window.location.href = `/perfil/recetas-creadas/${recetaId}/editar/`;  //CAMBIAR REDIRECCIÓN A PÁGINA DE EDICIÓN
});

// 4. Botón Eliminar

document.getElementById("btnEliminar").addEventListener("click", async () => {
    if (!confirm("¿Seguro que deseas eliminar esta receta?")) return;

    const token = localStorage.getItem("access");
    const csrftoken = getCookie("csrftoken");


    const resp = await fetch(`/perfil/api/recetas-creadas/${recetaId}/`, {
        method: "DELETE",
        headers: {
            "X-CSRFToken": csrftoken,
        }
    });

    if (resp.status === 204) {
        alert("Receta eliminada con éxito.");
        window.location.href = "/perfil/dashboard/";
    } else {
        alert("Hubo un problema al eliminar la receta.");
    }
});

// Inicializar
cargarReceta();
