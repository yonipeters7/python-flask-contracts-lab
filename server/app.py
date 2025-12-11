#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)

@app.route('/contract/<int:id>', methods=['GET'])
def get_contract(id):
    # Loop through contracts to find one with matching id
    for contract in contracts:
        if contract["id"] == id:
            # Contract found! Return its information with 200
            return make_response(contract, 200)

    # If we get here, no contract was found
    return make_response({"message": "Contract not found"}, 404)

@app.route('/customer/<string:customer_name>', methods=['GET'])
def get_customer(customer_name):
    # Check if customer_name exists in customers list
    if customer_name in customers:
        # Customer found! Return 204 (no content) with empty body
        return make_response('', 204)
    else:
        # Customer not found
        return make_response({"message": "Customer not found"}, 404)

if __name__ == '__main__':
    app.run(port=5555, debug=True)