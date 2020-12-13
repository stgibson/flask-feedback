from flask import Flask, redirect, render_template, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User
from forms import NewUserForm, LoginUserForm
from sqlalchemy.exc import IntegrityError

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
def register():
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
        session["username"] = user.username
        db.session.add(user)
        
        # might break if username has already been used
        try:
            db.session.commit()
        except IntegrityError:
            form.username.errors.append("That username already exists")
            return render_template("register.html", form=form)

        return redirect(f"/users/{username}")

    return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    """
        Shows a form for user to login. When the form is submitted, if the user
        typed in his or her correct credentials, goes to the secret page.
        rtype: str
    """
    form = LoginUserForm()

    if form.validate_on_submit():
        # get data submitted
        username = form.username.data
        password = form.password.data

        # authenticate user
        user = User.authenticate(username, password)
        if user:
            session["username"] = user.username
            return redirect(f"/users/{username}")
        flash("Incorrect credentials. Please try again.", "danger")

    return render_template("login.html", form=form)

@app.route("/logout")
def logout():
    """
        Logs user out so they can no longer access the features of the app
        rtype: str
    """
    if session.get("username", None):
        session.pop("username")
    return redirect("/")

@app.route("/users/<username>")
def show_user_page(username):
    """
        Shows the user's information along with a list of their feedback
        type username: str
        rtype: str
    """
    # make sure user is accessing his/her own page
    current_username = session.get("username", None)
    if current_username and current_username == username:
        current_user = User.query.filter_by(username=current_username).one()
        return render_template("user.html", user=current_user)
    return redirect("/")

@app.route("/users/<username>/delete", methods=["POST"])
def delete_user(username):
    """
        Deletes user and then logs user out
        type username: str
        rtype: str
    """
    # can only delete own account
    current_username = session.get("username", None)
    if current_username and current_username == username:
        current_user = User.query.filter_by(username=current_username).one()
        db.session.delete(current_user)
        db.session.commit()
        # logout to remove user from session
        return redirect("/logout")
    return redirect(f"/users/{username}")