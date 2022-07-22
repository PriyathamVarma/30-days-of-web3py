# This script is for getting txn details and various key:value pairs with the transaction

# Imports
from web3 import Web3
import os

# Imports for Environment variables
from dotenv import load_dotenv
load_dotenv()

# Variables

alchemy_api_key = os.getenv('ALCHEMY_API_KEY')
# metamask address
wallet_address  = os.getenv('WALLET_ADDRESS')

# Connect to the blockchain
web3Object = Web3(Web3.HTTPProvider(alchemy_api_key))

# Get the transaction details
# see to it that txn is in polygon testnet
txnDetails = web3Object.eth.get_transaction('0x2580e1b6453fe2cd6e941197aa6d9ac93de182e0d7df8ad00bcd0456a74a04d5')
print(type(txnDetails)) # Class type <class 'dict'>

# Accessing dictionary keys
print(txnDetails['blockHash'])

# Accessing dictionary values
print(txnDetails['blockNumber'])

# Accessing data from the dictionary
print(txnDetails['from'])



