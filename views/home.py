import os

from flask import Blueprint, render_template, request, session, redirect, url_for, abort
from werkzeug import secure_filename

from database import db_session
from views import utils

home = Blueprint('home', __name__)

@home.route("/")
def index():
    return render_template("home.html")

@home.route("/search")
def search():
    query = request.args.get('q', '')
    if query:
        return utils.render_react('search', query=query)
    return utils.render_react('search')

@home.route("/search/results", methods=["POST"])
@utils.jsonify_response
def search_results():
    query = request.form.get('query')
    if not query:
        return {'results': []}
    sections = [{"title": "Ohh yeah"}]
    return {'results': sections}