from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt
import data_user as us

app = Flask(__name__)

@app.route('/update', methods=['PUT'])
def update_user():
    # Get the user's information from the request
    username = request.form.get('username')
    new_password = request.form.get('new_password')
    new_name = request.form.get('new_name')

    # Check if the user exists in the database
    _user = us.find_username(username)

    if _user:
        # Use an update query to update the user's information
        us.update_user(username, new_password, new_name)
        return jsonify({'message': 'User updated successfully'}), 200
    else:
        return jsonify({'message': 'User not found'}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True) #127.0.0.1

