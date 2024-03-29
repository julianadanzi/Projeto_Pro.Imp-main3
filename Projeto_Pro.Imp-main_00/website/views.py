from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, logout_user, current_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/profile')
@login_required
def profile():
    return render_template("profile.html", user=current_user)

