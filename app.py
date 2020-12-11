from flask import Flask, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User
from forms import NewUserForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "kubrick"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///feedback"
app.config["SLQALCHEMY_TRACK_MODIFICATIONS"] = False

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def go_to_register_page():
    """
        Redirects to register page
        rtype: str
    """
    return redirect("/register")

@app.route("/register")
def show_register_page():
    """
        Shows form for user to register
        rtype: str
    """
    form = NewUserForm()

    return render_template("register.html", form=form)