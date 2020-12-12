from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

bcrypt = Bcrypt()

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
    __tablename__ = "users"
    
    username = db.Column(db.VARCHAR(20), primary_key=True)

    password = db.Column(db.Text, nullable=False)

    email = db.Column(db.VARCHAR(50), nullable=False)

    first_name = db.Column(db.VARCHAR(30), nullable=False)

    last_name = db.Column(db.VARCHAR(30), nullable=False)

    @classmethod
    def register(cls, username, password, email, first_name, last_name):
        """
            Registers the new user
            type username: str
            type password: str
            type email: str
            type first_name: str
            type last_name: str
            rtype: User
        """
        hashed = bcrypt.generate_password_hash(password)
        hashed_utf = hashed.decode("utf8")

        return cls(username=username, password=hashed_utf, email=email, \
            first_name=first_name, last_name=last_name)

    @classmethod
    def authenticate(cls, username, password):
        """
            Checks the user's credentials. If they are correct, returns the
            user.
        """
        # get the user and hashed password based on username
        user = cls.query.filter_by(username=username).one_or_none()
        if user:
            hashed = user.password

            # verify hashed password matched password submitted by user
            if bcrypt.check_password_hash(hashed, password):
                return user