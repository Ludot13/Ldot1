from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user


app = Flask(__name__)
app.secret_key = "your_secret_key"  # Секретный ключ для подписи данных сессии

login_manager = LoginManager()
login_manager.init_app(app)
@app.route("/")
def index():
    return render_template("index.html")

# Роут для регистрации
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Ваш код для сохранения данных пользователя

        flash("Регистрация успешно завершена.", "success")
        return redirect("/")
    return render_template("register.html")

# Роут для авторизации
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Ваш код для проверки данных пользователя

        flash("Авторизация успешна.", "success")
        return redirect("/")
    return render_template("login.html")

# Роут для выхода
@app.route("/logout")
def logout():
    # Ваш код для выхода из учетной записи

    flash("Выход из учетной записи.", "info")
    return redirect("/")

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

if __name__ == "__main__":
    app.run()