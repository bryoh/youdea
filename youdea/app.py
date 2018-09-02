''' App for youdea '''
from flask import Flask, render_template_string, redirect
from sqlalchemy import create_engine, MetaData
from flask_login import UserMixin, LoginManager, login_user, logout_user
from flask_blogging import SQLAStorage, BloggingEngine

youdea_app = Flask(__name__)
youdea_app.config["SECRET_KEY"] = "secret"  # for WTF-forms and login
youdea_app.config["BLOGGING_URL_PREFIX"] = "/blog"
youdea_app.config["BLOGGING_DISQUS_SITENAME"] = "test"
youdea_app.config["BLOGGING_SITEURL"] = "http://localhost:8000"
youdea_app.config["BLOGGING_SITENAME"] = "My Site"
youdea_app.config["BLOGGING_TWITTER_USERNAME"] = "@me"
youdea_app.config["FILEUPLOAD_IMG_FOLDER"] = "fileupload"
youdea_app.config["FILEUPLOAD_PREFIX"] = "/fileupload"
youdea_app.config["FILEUPLOAD_ALLOWED_EXTENSIONS"] = ["png", "jpg", "jpeg", "gif"]

# extensions
engine = create_engine('sqlite:////tmp/blog.db')
meta = MetaData()
sql_storage = SQLAStorage(engine, metadata=meta)
blog_engine = BloggingEngine(youdea_app, sql_storage)
login_manager = LoginManager(youdea_app)
meta.create_all(bind=engine)


class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

    def get_name(self):
        return "John Doe"  # For now ... 

@login_manager.user_loader
@blog_engine.user_loader
def load_user(user_id):
    return User(user_id)

index_template = """
<!DOCTYPE html>
<html>
    <head> </head>
    <body>
        {% if current_user.is_authenticated %}
            <a href="/logout/"> Logout </a>
        {% else %}
            <a href="/login/"> Login </a>
        {% endif %}
        &nbsp&nbsp<a href="/blog/"> Blog </a>
        &nbsp&nbsp<a href="/blog/sitemap.xml">Sitemap</a>
        &nbsp&nbsp<a href="/blog/feeds/all.atom.xml">ATOM</a>
        &nbsp&nbsp<a href="/fileupload/">FileUpload</a>
    </body>
</html>
"""

@youdea_app.route("/")
def index():
    return render_template_string(index_template)

@youdea_app.route("/login/")
def login():
    user = User("testuser")
    login_user(user)
    return redirect("/blog")

@youdea_app.route("/logout/")
def logout():
    logout_user()
    return redirect("/")


if __name__ == "__main__":
    youdea_app.run(debug=True, port=8000, use_reloader=True)
