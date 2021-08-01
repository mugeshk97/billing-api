from flask import Flask, request, jsonify
from connection import get_sql_connection
from product import get_all_products, insert_product, delete_product
import json
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
cnx = get_sql_connection()

@app.route('/getProducts', methods=['GET'])
def get_products():
    products = get_all_products(cnx)
    response =  jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertProduct', methods=['POST'])
def insert_prod():
    request_payload = json.loads(request.form['data'])
    print(request_payload)
    product_id = insert_product(cnx, request_payload)
    response = jsonify(
        {'product_id': product_id}
    )
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/deleteProduct', methods=['POST'])
def delete_prod():
    request_payload = json.loads(request.form['product_id'])
    return_id = delete_product(cnx, request_payload['product_id'])
    response = jsonify(
        {'product_id': return_id}
    )
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=5050, debug= True)