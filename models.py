from flask-sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """
        Connects app to db
        type app: Flask
    """
    db.app = app
    db.init_app(app)

class User(db.Model):
    """
        Creates schema for users. Includes the user's username, password,
        email, first name, and last name.
    """
    __tablename = "users"
    
    username = db.Column(db.VARCHAR(20), primary_key=True)

    password = db.Column(db.Text, nullable=Flase)

    email = db.Column(db.VARCHAR(50), nullable=False)

    first_name = db.Column(db.VARCHAR(30), nullable=False)

    last_name = db.Column(db.VARCHAR(30), nullable=False)