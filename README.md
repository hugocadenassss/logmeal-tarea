LogMeal Take-Home Project


Este proyecto es un ejemplo mínimo de una aplicación full-stack que permite:

- Subir imágenes.
- Listar imágenes subidas.
- Analizar imágenes (formato, tamaño y peso en bytes).
- Generar un enlace público compartible válido por 10 minutos.

El backend está desarrollado con **Python Flask**, y el frontend con **HTML + JavaScript**.  
Todo el proyecto se ejecuta mediante **Docker** y **docker-compose**, sin necesidad de instalar dependencias adicionales.


Enlace Público GitHub: https://github.com/hugocadenassss/logmeal-tarea


Estructura de carpetas

logmeal-takehome/
│
├─ backend/
│ ├─ app.py # Código del backend Flask
│ ├─ requirements.txt
│ ├─ Dockerfile
│ └─ uploads/ # Carpeta para imágenes subidas
│
├─ frontend/
│ ├─ index.html
│ ├─ app.js
│ ├─ styles.css # Opcional
│ └─ Dockerfile
│
├─ docker-compose.yml
└─ README.md

Requisitos

- Docker Desktop (Windows / Mac) o Docker + docker-compose (Linux)
- Git (opcional, para clonar el repositorio)


Cómo ejecutar

1. Abrir la terminal y navegar a la carpeta del proyecto:

cd ruta/a/logmeal-takehome


2. Levantar los contenedores con Docker Compose:
docker-compose up --build
- Esto construye y ejecuta backend (puerto 8000) y frontend (puerto 3000).


3. Abrir el frontend en el navegador:
http://localhost:3000


4. Comprobar que el backend funciona:
http://localhost:8000
- Debe mostrar: Backend OK


Endpoints disponibles
Backend API

Método	Endpoint		Descripción
POST	/api/upload_image	Subir una imagen
GET	/api/list_images	Listar todas las imágenes subidas
POST	/api/analyse_image	Analizar una imagen por ID
POST	/api/share_image	Generar un enlace público temporal
GET	/s/<token>		Página pública con la imagen compartida


Notas

Las imágenes se guardan en backend/uploads dentro del contenedor y en tu carpeta local (volumen Docker).
El proyecto cumple todos los requisitos mínimos.


Clonar proyecto GitHub

git clone https://github.com/hugocadenassss/logmeal-tarea.git