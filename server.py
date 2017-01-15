from os import getenv
from flask import Flask, request, Response
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from werkzeug.exceptions import HTTPException
from models import Catalog, Choice


class AuthException(HTTPException):

    def __init__(self, message):
        super().__init__(message, Response(
            "You could not be authenticated. Please refresh the page.", 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}
        ))


class MyModelView(ModelView):

    def check_auth(self, username, password):
        return username == getenv('login') and password == getenv('passwd')

    def is_accessible(self):
        auth = request.authorization
        print(auth)
        if not auth or not self.check_auth(auth.username, auth.password):
            raise AuthException('Not authenticated.')
        return True


app = Flask(__name__)
app.config['SECRET_KEY'] = '123456790'
engine = create_engine(getenv('db_uri'))
Session = sessionmaker(bind=engine)
session = Session()
admin = Admin(app, name='pizza-bot', template_mode='bootstrap3')
admin.add_view(MyModelView(Catalog, session))
admin.add_view(MyModelView(Choice, session))


if __name__ == '__main__':
    app.run()
