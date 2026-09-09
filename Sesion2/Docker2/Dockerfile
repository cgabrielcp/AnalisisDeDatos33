# imagen Base
FROM python:3.9-slim 

# Definir nuestro espacio trabajo
WORKDIR /app

# Copiamos las librerias
COPY requirements.txt ./

# Installamos las librerias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo a la imagen
COPY . .

# Exposicion
EXPOSE 5000

CMD [ "python", "app.py" ]
