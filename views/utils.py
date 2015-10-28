from functools import wraps
import itertools

from flask import render_template, g, jsonify, session, redirect, url_for, request

letters = 'abcdefghijklmnopqrstuvwxyz'

def js_call(module, function, *parameters):
	if not hasattr(g, 'js_modules'):
		g.js_modules = []
		g.js_module_aliases = {}
	if module not in g.js_modules:
		g.js_module_aliases[module] = letters[len(g.js_modules)]
		g.js_modules.append(module)
	if not hasattr(g, 'js_calls'):
		g.js_calls = []
	g.js_calls.append((g.js_module_aliases[module], function, parameters))

def render_react(react_component, html_template='react-base.html', **props):
	if len(props) > 0:
		return render_template(html_template, component=react_component, props=props)
	return render_template(html_template, component=react_component)

def jsonify_response(func):
	@wraps(func)
	def wrapped(*args, **kwargs):
		try:
			res = func(*args, **kwargs)
			return jsonify({"error": False, "data": res})
		except Exception as err:
			return jsonify({"error": True, "message": str(err)})
	return wrapped

def login_required(func):
	@wraps(func)
	def wrapped(*args, **kwargs):
		if 'user_id' in session:
			return func(*args, **kwargs)
		return redirect(url_for('user.login', next=request.path))
	return wrapped