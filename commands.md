<h1>Comandos para GIT

<h2>Subir código.


1.-Iniciar GIT. \
$ git init

2.-Añadir archivos, "." todos o nombre de archivo en directorio. \
$ git add .

3.-Hacer cambion, se agrega comentario de cambio. \
$ git commit -m 'esto es un comentario'

4.-Conectarse a repositorio. \
$ git remote add origin https://github.com/yamlfullsan/cursopython.git

5.-Si hay error --> fatal: remote origin already exists -- tecleamos lo siguiente y repetimos paso anterior. \
$ git remote rm origin

6.-Subimos código. \
$ git push -u origin master
