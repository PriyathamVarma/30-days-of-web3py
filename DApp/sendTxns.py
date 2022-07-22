# This script is for sending transactions from the blockchain

# Imports
from web3 import Web3
import os

# Imports for Environment variables
from dotenv import load_dotenv
load_dotenv()

# For middleware
from web3.middleware import geth_poa_middleware

# Variables

alchemy_api_key = os.getenv('ALCHEMY_API_KEY')
# metamask address
wallet_address  = os.getenv('WALLET_ADDRESS')

# Connect to the blockchain
web3Object = Web3(Web3.HTTPProvider(alchemy_api_key))
# Add the middleware
web3Object.middleware_onion.inject(geth_poa_middleware, layer=0)


'''
web3Object.eth.send_transaction({
  'to': '0xd3CdA913deB6f67967B99D67aCDFa1712C293601', # who recieves the transaction
  'from': wallet_address,                             # who sends the transaction          
  'value': 12345,                                     # amount of ether to send
  'gas': 21000,                                       # gas limit
  'gasPrice': web3Object.toWei(50, 'gwei'),           # gas price --> amount of gas willing to pay for each gas unit
}) # this method doesnt work because alchemy doesnt hold private keys '''

# Include private networks from env file

private_key = os.getenv('PRIVATE_KEY')
print(private_key)

# Send the transaction using the private key
txn = web3Object.eth.send_transaction({
  'to': '0xd3CdA913deB6f67967B99D67aCDFa1712C293601', # who recieves the transaction
  'from': wallet_address,                             # who sends the transaction          
  'value': 12345,                                     # amount of ether to send
  'gas': 21000,                                       # gas limit
  'gasPrice': web3Object.toWei(50, 'gwei'),           # gas price --> amount of gas willing to pay for each gas unit
}) 

web3Object.eth.account.sign_transaction(txn, private_key)


