from flask import Blueprint, jsonify
import requests

# Define a blueprint for the crypto API
crypto_bp = Blueprint('crypto', __name__)

# CoinGecko API URL to get real-time prices for Bitcoin, Ethereum, and Litecoin
COINGECKO_API_URL = 'https://api.coingecko.com/api/v3/simple/price'

@crypto_bp.route('/<string:crypto>', methods=['GET'])
def get_crypto_price(crypto):
    try:
        # Make a request to the CoinGecko API to get prices for multiple cryptocurrencies
        response = requests.get(f'{COINGECKO_API_URL}?ids={crypto}&vs_currencies=usd')
        data = response.json()

        # Check if the requested cryptocurrency exists in the response
        if crypto not in data:
            return jsonify({'error': 'Cryptocurrency not found'}), 404

        # Return the price of the requested cryptocurrency
        return jsonify({crypto: data[crypto]}), 200

    except Exception as e:
        # Return error message if something goes wrong
        return jsonify({'error': str(e)}), 500
