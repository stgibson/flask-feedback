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

@app.route("/register", methods=["GET", "POST"])
def show_register_page():
    """
        Shows a form for user to register. When the form is submitted,
        registers the user with the input the user submitted.
        rtype: str
    """
    form = NewUserForm()

    if form.validate_on_submit():
        # get data submitted
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        # register user
        user = User.register(username, password, email, first_name, last_name)
        db.session.add(user)
        db.session.commit()

        return redirect("/secret")

    return render_template("register.html", form=form)
