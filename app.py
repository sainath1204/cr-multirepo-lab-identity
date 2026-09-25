import base64, json
from flask import Flask, request, jsonify
app = Flask(__name__)
@app.post('/verify')
def verify():
    token = request.json['token']
    payload = token.split('.')[1]
    claims = json.loads(base64.urlsafe_b64decode(payload + '=' * (-len(payload) % 4)))
    return jsonify(user_id=claims['sub'], role=claims.get('role', 'user'))
