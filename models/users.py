from sqlalchemy import Column, Integer, String, Boolean
from werkzeug.security import generate_password_hash, check_password_hash

import database as sql_db

class User(sql_db.Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    hashed_password = Column(String(100))
    is_admin = Column(Boolean)

    def __init__(self, *args, **kwargs):
        password = kwargs.pop('password')
        super(User,self).__init__(*args,**kwargs)
        if password:
            self.set_password(password)

    def __repr__(self):
        return '<User %r>' % (self.username)

    def get_photo_url(self):
        if not self.photo_url:
            return "http://api.adorable.io/avatars/285/{}".format(self.username)
        return self.photo_url

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)