from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from website import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('O login foi um sucesso!', category='success')
                login_user(user, remember=True)
                
                return redirect(url_for('views.profile'))
            else:
                flash('senha incorreta, tente de novo.', category='error')
        else:
            flash('O email não existe', category='error')
    
    return render_template("login.html", boolean=True, user="Usuário", password="Senha")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))




@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('O email já foi usado', category='error')

        elif len(email) < 5:
            flash('O email deve ter mais de 5 caracteres', category='error')
            pass
        elif len(first_name) < 2:
            flash('Seu nome deve ter mais de 2 caracteres', category='error')
        elif password1 != password2:
            flash('A senha não é a mesma', category='error')
        elif len(password1) != 12:
            flash('A senha deve ter 12 números', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash('pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Conta criada!', category='success')
            return redirect(url_for('views.home'))
    
    return render_template("sign_up.html")