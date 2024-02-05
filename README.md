# Blog-de-Cocina
Este es un blog personal en el que subo recetas de cocina,.

## DESCRIPCION DEL PROYECTO

Este proyecto se basa en un blog personal en el que subo recetas de cocina, Flavor Fusion, es una aplicación web diseñada para permitir a los administradores ir subiendo contenido de forma sencilla.
A traves de la interfaz el administrador ( para lo cual se accede desde la direccion /admin) uno puede visualizar la pagina web de forma bastante parecida a como pueden ver otros usuarios, pero con la diferencia que uno puede editar y eliminar publicaciones previamente realizadas.
Este proyecto fue desarrollado con Python, utiliza el framework Flask, SQLAlchemy para la gestión de la base de datos, y HTM con Tailwind CSS y CSS puro para la parte de front.


## ENFOQUE Y METODOLOGIA 

El enfoque de la pagina es el de mostrar a los usuarios una variada lista de recetas de cocina, y la metodologia inluye la creacion de una base de datos que contiene una tabla de usuarios ( ya que posee un login y registro de usuario funcionales, o sea que posee validacion de datos) ademas de una tabla que incluye los datos de cada receta (titulo, contenido e imagen) . Tambien se implemento un CRUD para las recetas, el cual es muy util para el administrador de la pagina, ya que se debera encargar de crear el contenido,poder leerlo, actualizarlo y en ciertos casos eliminarlos.
Para editar y/o eliminar contenido existente : no se llego a implementar una validacion especifica del administrador, por ende se debera ingresar por medio de la direccion /admin.
Para crear contenido : Como lo mencione anteriormente, no se hizo validacion como tal del administrador, entonces se debera acceder por medio de la direccion : /create
Para Leer :

### Planificación

Se inició esta fase para definir los requisitos del proyecto, priorizar las funcionalidades y planificar las vistas.

### Desarrollo

El desarrollo se basó en principios de programación, manteniendo el código bien organizado y facilitando la escalabilidad del proyecto.

- Modelos de SQLAlchemy definen la estructura de la base de datos.
- La parte del front se realizo con HTML y CSS.
- Se utilizo una libreria de Flask para hacer el login (flask-login).
- Se utilizo Flask para la generacion de rutas.
- Se utilizo Flask_SQLALCHEMY para la interaccion con la base de datos.

### Pruebas

Se realizaron para asegurar la calidad del código. Esto incluyó pruebas en los modelos de datos y las funcionalidades clave de la aplicación.        


## TECNOLOGIAS UTILIZADAS

- *Flask*: Un framework de Python para desarrollar aplicaciones web. Utilizado para manejar las solicitudes del servidor, las rutas, y la lógica de la pagina.
- *SQLAlchemy*: Utilizado para interactuar con la base de datos de manera más eficiente.
- *HTML*: Utilizado para estructurar el contenido de la página web.
- *Tailwind CSS*: Se utilizó para estilizar la interfaz de la tienda online personalizada.
- flask-login se utilizo para facilitar la creacion del login.


## EJECUCION DEL PROYECTO 

Este proyecto se ejecuta de la siguiente manera:

### Requisitos Previos
- Crear y activar un entorno virtual
- Python 3.
- pip para la instalación de paquetes
- Flask_SQLALCHEMY
- libreria flask-login
- Framework Flask

### Instalación

1. Clonar el repositorio.
2. Instalar todo lo mencionado arriba. 



## ARQUITECTURA 
/static 
- Archivos estáticos como imágenes de las comidas.
/templates 
- Plantillas HTML para las pestanhas.
app.py 
- El archivo principal de la aplicación Flask que configura la aplicación y define las rutas, gestionando las actualizaciones del administrador.


