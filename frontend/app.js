const API = "http://localhost:8000/api";

async function uploadImage() {
    const file = document.getElementById("upload").files[0];
    if (!file) {
        alert("Selecciona un archivo primero");
        return;
    }

    const form = new FormData();
    form.append("image", file);

    const res = await fetch(`${API}/upload_image`, {
        method: "POST",
        body: form
    });

    const data = await res.json();
    alert(`Imagen subida con ID: ${data.id}`);
}

async function listImages() {
    const res = await fetch(`${API}/list_images`);
    const data = await res.json();

    const list = document.getElementById("imageList");
    list.innerHTML = "";

    data.forEach(img => {
        const li = document.createElement("li");
        li.textContent = `${img.id} - ${img.filename}`;
        list.appendChild(li);
    });
}

async function analyseImage() {
    const id = document.getElementById("analyseId").value;
    if (!id) {
        alert("Introduce un ID de imagen");
        return;
    }

    const res = await fetch(`${API}/analyse_image`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ id: id })
    });

    const data = await res.json();
    document.getElementById("analysis").textContent =
        JSON.stringify(data, null, 2);
}

async function shareImage() {
    const id = document.getElementById("shareId").value;
    if (!id) {
        alert("Introduce un ID de imagen");
        return;
    }

    const res = await fetch(`${API}/share_image`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ id: id })
    });

    const data = await res.json();
    document.getElementById("shareResult").textContent =
        JSON.stringify(data, null, 2);

    // Abrir automáticamente la URL pública
    if (data.url) {
        window.open(`http://localhost:8000${data.url}`, "_blank");
    }
}
