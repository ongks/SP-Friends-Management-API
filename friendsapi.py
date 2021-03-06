from flask import Flask, request, jsonify
from jsonschema import ValidationError
from data import friends, block, get_updates
import schemas, managefriends


app = Flask(__name__)

@app.route('/api/v0/addfriend', methods=['GET', 'POST'])
def add_friend():
    json_req = request.json
    try:
        schemas.validate_friends_pair(json_req)
        json_resp = managefriends.add_friend_request(json_req, friends, get_updates, block)
        return jsonify(json_resp)
    except ValidationError:
        return jsonify({"success": False, "message": "Invalid JSON request."})

@app.route('/api/v0/listfriends', methods=['GET', 'POST'])
def list_friends():
    json_req = request.json
    try:
        schemas.validate_single_email(json_req)
        json_resp = managefriends.list_friends_request(json_req, friends)
        return jsonify(json_resp)
    except ValidationError:
        return jsonify({"success": False, "message": "Invalid JSON request."})

@app.route('/api/v0/mutualfriends', methods=['GET', 'POST'])
def list_mutual_friends():
    json_req = request.json
    try:
        schemas.validate_friends_pair(json_req)
        json_resp = managefriends.list_mutual_friends_request(json_req, friends)
        return jsonify(json_resp)
    except ValidationError:
        return jsonify({"success": False, "message": "Invalid JSON request."})

@app.route('/api/v0/subscribeupdates', methods=['GET', 'POST'])
def sub_updates():
    json_req = request.json
    try:
        schemas.validate_requestor_target(json_req)
        json_resp = managefriends.sub_updates_request(json_req, get_updates, block)
        return jsonify(json_resp)
    except ValidationError:
        return jsonify({"success": False, "message": "Invalid JSON request."})

@app.route('/api/v0/blockupdates', methods=['GET', 'POST'])
def block_updates():
    json_req = request.json
    try:
        schemas.validate_requestor_target(json_req)
        json_resp = managefriends.block_updates_request(json_req, get_updates, block)
        return jsonify(json_resp)
    except ValidationError:
        return jsonify({"success": False, "message": "Invalid JSON request."})

@app.route('/api/v0/listrecipients', methods=['GET', 'POST'])
def list_recipients():
    json_req = request.json
    try:
        schemas.validate_sender_text(json_req)
        json_resp = managefriends.list_recipients_request(json_req, friends, get_updates, block)
        return jsonify(json_resp)
    except ValidationError:
        return jsonify({"success": False, "message": "Invalid JSON request."})

if __name__ == '__main__':
    app.run()