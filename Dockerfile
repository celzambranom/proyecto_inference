# Usa una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de la aplicación al contenedor
COPY . /app

# Instala las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que la aplicación Flask va a escuchar
EXPOSE 5001

# Define la variable de entorno para Flask
ENV FLASK_APP=send_image.py

# Comando para ejecutar la aplicación cuando se inicie el contenedor
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5001"]
