from flask import Blueprint, request, jsonify

from .data.search_data import USERS

bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    search_results = search_users(request.args.to_dict())
    return jsonify(search_results), 200


def search_users(args):
    filtered_users = []

    # Id filter
    if 'id' in args:
        user_id = args['id']
        user = next((user for user in USERS if str(user.get('id', '')) == str(user_id)), None)
        if user:
            filtered_users.append(user)

    # name filter
    if 'name' in args:
        name_value = args['name'].lower() 
        filtered_users += [user for user in USERS if name_value in user.get('name', '').lower()]

    # occupation filter
    if 'occupation' in args:
        occupation_value = args['occupation'].lower()  
        filtered_users += [user for user in USERS if occupation_value in user.get('occupation', '').lower()]

    # age filter
    if 'age' in args:
        try:
            age = int(args['age'])
            filtered_users += [user for user in USERS if age - 1 <= user.get('age', 0) <= age + 1]
        except ValueError:
            pass

    unique_users = {user['id']: user for user in filtered_users}.values()

    formatted_result = [
        {"id": user["id"], "name": user["name"], "age": user["age"], "occupation": user["occupation"]}
        for user in unique_users
    ]

    return formatted_result