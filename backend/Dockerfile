# Imagen base de Python ligera
FROM python:3.10-slim

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de dependencias
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código del backend al contenedor
COPY . .

# Exponemos el puerto 8000
EXPOSE 8000

# Comando para arrancar Flask
CMD ["python", "app.py"]
