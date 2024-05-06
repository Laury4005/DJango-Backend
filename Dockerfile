# Usando la imagen base de Python
FROM python:3.12.3

# Estableciendo el directorio de trabajo en /app
WORKDIR /app

# Copiando el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instalando las dependencias
RUN pip install -r requirements.txt

# Copiando todo el contenido del directorio actual al directorio de trabajo en el contenedor
COPY . .

# Exponiendo el puerto 8000
EXPOSE 8000

# Configurando la variable de entorno para el archivo de configuración de Django
ENV DJANGO_SETTINGS_MODULE=DJango.settings

# Ejecutando Gunicorn cuando se inicia el contenedor
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "modelDJango.wsgi:application"]
