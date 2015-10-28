from bson.objectid import ObjectId
from flask import Flask, render_template, session, g
from werkzeug.routing import BaseConverter

from database import db_session
from models.users import User
from views import blueprints

app = Flask(__name__)
app.debug = True

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.before_request
def load_user():
    if "user_id" in session:
        g.user = User.query.filter(User.id == session["user_id"]).first()
    else:
        g.user = None

class ObjectIdConverter(BaseConverter):

    def to_python(self, value):
        return ObjectId(value)

    def to_url(self, value):
        return super(ObjectIdConverter, self).to_url(str(value))

app.url_map.converters['oid'] = ObjectIdConverter

for blueprint in blueprints:
	app.register_blueprint(blueprint)

app.secret_key = b'Please dont use this'

if __name__ == "__main__":
    app.run(host= '0.0.0.0')