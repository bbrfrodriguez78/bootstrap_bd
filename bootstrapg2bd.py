from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base_datos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Añade esta línea
db = SQLAlchemy(app)

from models import User, Comentario

@app.route('/index')
def index():
#    user_email = session.get('user_email')
#    return render_template('index.html', user_email=user_email)
    user_email = session.get('user_email')
    if not user_email:
        return redirect(url_for('login'))
    
    # Recuperar todos los comentarios
    comentarios = Comentario.query.all()  
    
    # Recuperar los comentarios del usuario autenticado
    # comentarios = Comentario.query.filter_by(email=user_email).all()
    return render_template('index.html', user_email=user_email, comentarios=comentarios)

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            # Guardar el correo electrónico del usuario en la sesión
            session['user_email'] = user.email
            # Usuario autenticado, redirige a la página de inicio u otra página
            return redirect(url_for('index'))
        else:
            flash('Invalido email o password', 'danger')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if password == confirm_password:
            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                flash('¡Usuario ya registrado con email!', 'danger')
            else:
                hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
                new_user = User(first_name=first_name, 
                                last_name=last_name, 
                                email=email, 
                                password=hashed_password)
                db.session.add(new_user)
                db.session.commit()
                flash('¡Cuenta creada satisfactoriamente!', 'success')
                return redirect(url_for('login'))
        else:
            flash('¡Contraseña no coincide!', 'danger')
    
    return render_template('register.html')

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_email', None)
    return redirect(url_for('login'))

@app.route('/buttons')
def buttons():
    return render_template('buttons.html')

@app.route('/add_comment', methods=['POST'])
def add_comment():
    if 'user_email' not in session:
        return jsonify({'error': 'User not logged in'}), 401
    
    email = session['user_email']
    comentario = request.form['comentario']
    fecha = datetime.now().strftime('%Y-%m-%d')
    hora = datetime.now().strftime('%H:%M:%S')

    nuevo_comentario = Comentario(email=email, 
                                  comentario=comentario, 
                                  fecha=fecha, 
                                  hora=hora)
    db.session.add(nuevo_comentario)
    db.session.commit()

    return jsonify({'success': 'Comment added successfully'}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
