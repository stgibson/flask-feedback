from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, Optional

class NewUserForm(FlaskForm):
    """
        Template for the form to create a new user. Has inputs for a username,
        password, email, first name, and last name.
    """
    username = StringField("Username", validators=[InputRequired(), \
        Length(min=1, max=20)])

    password = PasswordField("Password", validators=[InputRequired()])

    email = StringField("Email", validators=[InputRequired(), Email(), \
        Length(min=1, max=50)])

    first_name = StringField("First name", validators=[InputRequired(), \
        Length(min=1, max=30)])

    last_name = StringField("Last name", validators=[InputRequired(), \
        Length(min=1, max=30)])

class LoginUserForm(FlaskForm):
    """
        Template for the form for a user to login. Has inputs for a username
        and password.
    """
    username = StringField("Username", validators=[InputRequired(), \
        Length(min=1, max=20)])

    password = PasswordField("Password", validators=[InputRequired()])

class FeedbackForm(FlaskForm):
    """
        Template for adding a new feedback. Has inputs for title and content.
    """
    title = StringField("Title", validators=[InputRequired(), \
        Length(min=1, max=100)])

    content = StringField("Content", validators=[InputRequired()])