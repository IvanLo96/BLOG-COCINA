from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recetas_database.db'
app.config['SECRET_KEY'] = 'tu_clave_secreta'
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'index'

class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)


class Receta(db.Model):     
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    contenido = db.Column(db.Text, nullable=False)
    imagen = db.Column(db.String(255))  


@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

# CRUD

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Usuario.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            return redirect('/home')
        else:
            return 'Datos incorrectos'

    return render_template('login.html')

@app.route('/read/<int:id>')
def read(id):
    receta = Receta.query.get(id)
    return render_template('read.html', receta=receta)

# Solo el administrador del blog puede realizar las siguientes operaciones

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        titulo = request.form['titulo']
        contenido = request.form['contenido']
        imagen = request.form['imagen']

        nueva_receta = Receta(titulo=titulo, contenido=contenido, imagen=imagen)
        db.session.add(nueva_receta)
        db.session.commit()
        return redirect('/home')
    return render_template('create.html')


from flask import request

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    receta = Receta.query.get(id)

    if request.method == 'POST':
        receta.titulo = request.form.get('titulo', receta.titulo)
        receta.contenido = request.form.get('contenido', receta.contenido)
        receta.imagen = request.form.get('imagen', receta.imagen)
        
        db.session.commit()
        return redirect(url_for('read', id=id))

    # Manejar los valores predeterminados para cargar el formulario
    titulo_default = request.args.get('titulo', receta.titulo)
    imagen_default = request.args.get('imagen', receta.imagen)
    contenido_default = request.args.get('contenido', receta.contenido)

    return render_template('update.html', receta=receta, titulo_default=titulo_default, imagen_default=imagen_default, contenido_default=contenido_default)







@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    receta = Receta.query.get(id)

    if request.method == 'POST':
        db.session.delete(receta)
        db.session.commit()
        return redirect(url_for('admin'))

    return render_template('delete.html', receta=receta)







@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Verifica si el usuario ya existe
        if Usuario.query.filter_by(username=username).first():
            return 'El nombre de usuario ya está en uso. Por favor, elige otro.'

        nuevo_usuario = Usuario(username=username, password=password)
        db.session.add(nuevo_usuario)
        db.session.commit()

        login_user(nuevo_usuario)  # Inicia sesión después del registro
        return redirect('/')

    return render_template('registro.html')



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')
    
    

@app.route('/home')
def home():
    recetas = Receta.query.all()
    print(recetas)
    return render_template('home.html', recetas=recetas)

@app.route('/admin')
def admin():
    recetas = Receta.query.all()
    return render_template('admin.html', recetas=recetas)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)