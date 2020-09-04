import os, requests
from flask import Flask, request, jsonify
from invalid_usage import InvalidUsage

app = Flask(__name__)

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

CHOWLY_API_KEY = '4b5559f8b264e776'

@app.route('/api/chowly', methods=['POST'])
def chowly_callback():
    print(request.get_json())
    return request.get_json()

@app.route('/api/menu', methods=['POST'])
def chowly_menu():
    input = request.get_json()
    print(request.get_json())
    api_key = input.get("API_KEY", None)
    if api_key == None:
        raise InvalidUsage('API key not found')
    
    url = 'https://api.chowlyinc.com/api/toos/v2/menus'
    headers = {'api-key': api_key}
    res = requests.get(url, headers=headers)

    return res.json()