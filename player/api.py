from app import app
from . import players
from flask import jsonify
from flask_security import login_required


@app.route('/players')
@login_required
def list():
    return jsonify(players.all())

