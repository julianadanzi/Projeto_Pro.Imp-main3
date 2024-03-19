from flask import Blueprint, render_template, request, flash, redirect, url_for

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean=True, user="Usuário", password="Senha")

@auth.route('/logout')
def logout():
    return render_template("home.html")
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 5:
            flash('O email deve ter mais de 5 caracteres', category='error')
            pass
        elif len(firstName) < 2:
            flash('Seu nome deve ter mais de 2 caracteres', category='error')
        elif password1 != password2:
            flash('A senha não é a mesma', category='error')
        elif len(password1) != 12:
            flash('A senha deve ter 12 números', category='error')

        else:
            flash('Conta criada!', category='success')

    return render_template("sign_up.html")