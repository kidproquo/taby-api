import os, requests, json, datetime
from flask import Flask, request, jsonify
from invalid_usage import InvalidUsage

app = Flask(__name__)

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

CHOWLY_API_KEY = '4b5559f8b264e776'

callback_data = []

@app.route('/api/chowly', methods=['POST', 'GET'])
def chowly_callback():
    global callback_data

    if request.method == 'POST':
        callback_time = datetime.datetime.utcnow().isoformat()
        data = request.json()
        callback_data.append({'time': callback_time, 'data': data})
        return data

    return jsonify(callback_data)

@app.route('/api/order', methods=['POST', 'GET'])
def chowly_order():
    url = 'https://api.chowlyinc.com/api/toos/v2/orders'
    headers = {'api-key': CHOWLY_API_KEY}
    if request.method == 'POST':
        input = request.get_json()
        order = input.get("order")
        if order == None:
            raise InvalidUsage('Order details not found')
        
        
        res = requests.post(url, headers=headers, json=order)
        return res.json()
    
    order_id = request.args.get('orderId')
    if order_id == None:
            raise InvalidUsage('Order id not found')
    res = requests.get("{}/{}".format(url, order_id), headers=headers)
    return res.json()


@app.route('/api/menu', methods=['GET'])
def chowly_menu():
    url = 'https://api.chowlyinc.com/api/toos/v2/menus'
    headers = {'api-key': CHOWLY_API_KEY}
    res = requests.get(url, headers=headers)

    return res.json()

