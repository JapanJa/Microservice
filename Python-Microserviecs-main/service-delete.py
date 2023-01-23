from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt
import data_user as us

app = Flask(__name__)

@app.route('/delete', methods=['POST'])

def login():
    username = request.form.get('username')
    _user = us.find_username(username)

    if _user:
        us.delete_user(username)
        return jsonify({'message': 'User deleted successfully'}), 200
    else: 
        return jsonify({'message': 'User Not Found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True) #127.0.0.1