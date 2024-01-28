from flask import Flask, render_template, request, jsonify
from web3 import Web3

app = Flask(__name__)

# Connect to a local Ethereum node (update the URL accordingly)
web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Set the address of your smart contract
contract_address = '0x1234567890123456789012345678901234567890'
contract_abi = [...]  # Include the ABI of your smart contract

# Load the smart contract
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/verify', methods=['POST'])
def verify():
    document_hash = request.form['document_hash']

    # Verify the document by calling a function in the smart contract
    result = contract.functions.verifyDocument(document_hash).call()

    if result:
        return jsonify({'status': 'success', 'message': 'Document is verified'})
    else:
        return jsonify({'status': 'error', 'message': 'Document verification failed'})

if __name__ == '__main__':
    app.run(debug=True)
