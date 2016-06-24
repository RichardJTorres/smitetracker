from app import app
from . import players
from flask import jsonify, request
from flask_security import login_required


@app.route('/players')
@login_required
def player_list():
    player_name = request.args.get('name')
    if player_name:
        player = players.search(player_name)
        return jsonify(player)

    return jsonify(players.all())
