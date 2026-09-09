# AnalisisDeDatos33

# Flujo Comun de Git

1. Traer los cambios
   ```bash
   git fetch

   git pull origin main 

2. Estado actual del repositorio local
   ```bash
   git status

3. Agregar los cambios a capa staggin
    ```bash
   git add .

4. Generar el Commit
    ```bash
   git commit -m "Mi primer commit en github"

5. Empujar los cambios
    ```bash
   git push origin main


# Flujo Docker Comandos


0. navegar a la carpeta
   ```bash
   cd Sesion2/Docker1

1. Crear una imagen docker
   ```bash
   docker build --no-cache -t jupyter_notebook .

2. Listar las iamgenes
   ```bash
   docker images

3. ejecutar o levantar el contenedor
   ```bash
   docker run -d -p 8000:8888 --name jupyter jupyter_notebook 

4. listar los contenedores

   ```bash
   docker ps

5. Comandos adicionales
   ```bash
   docker rm -f jupyter # Eliminar contenedor
   docker rmi -f 222f5d7d304c # Eliminar imagen
