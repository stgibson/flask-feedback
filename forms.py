from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired

class NewUserForm(FlaskForm):
    """
        Template for the form to create a new user. Has inputs for a username,
        password, email, first name, and last name.
    """
    username = StringField("Username", validators=[InputRequired()])

    password = PasswordField("Password", validators=[InputRequired()])

    email = StringField("Email", validators=[InputRequired()])

    first_name = StringField("First name", validators=[InputRequired()])

    last_name = StringField("Last name", validators=[InputRequired()])

class LoginUserForm(FlaskForm):
    """
        Template for the form for a user to login. Has inputs for a username
        and password.
    """
    username = StringField("Username", validators=[InputRequired()])

    password = PasswordField("Password", validators=[InputRequired()])

class FeedbackForm(FlaskForm):
    """
        Template for adding a new feedback. Has inputs for title and content.
    """
    title = StringField("Title", validators=[InputRequired()])

    content = StringField("Content", validators=[InputRequired()])