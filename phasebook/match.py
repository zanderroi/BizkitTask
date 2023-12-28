import time
from flask import Blueprint, jsonify

from .data.match_data import MATCHES

bp = Blueprint("match", __name__, url_prefix="/match")

@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return jsonify({"message": "Invalid match id"}), 404

    start = time.time()
    msg = "Match found" if is_match(MATCHES[match_id][0], MATCHES[match_id][1]) else "No match"
    end = time.time()

    return jsonify({"message": msg, "elapsedTime": end - start})

def is_match(fave_numbers_1, fave_numbers_2):
   
    return set(fave_numbers_1).intersection(fave_numbers_2)
