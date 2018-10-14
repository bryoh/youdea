from flask import Flask, render_template_string, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, AdminIndexView
from flask_bcrypt import Bcrypt
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, LoginManager, login_user, logout_user, current_user

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"  # for WTF-forms and login
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///blog.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login = LoginManager(app)


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id =db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

class MyModelView(ModelView):
    def is_accesible(self):
        return current_user.is_authenticated
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))

admin = Admin(app)
admin.add_view(MyModelView(User, db.session))


@app.route('/login')
def login():
    user = User.query.get(1)
    login_user(user)
    return 'logged in'

@app.route('/logout')
def logout():
    logout_user()
    return 'loggout'

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
