# This script is for getting account details from the blockchain

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

print(alchemy_api_key)
print(wallet_address)

# Connect to the blockchain
web3Object = Web3(Web3.HTTPProvider(alchemy_api_key))


# Get the balance of the wallet
balance = web3Object.eth.getBalance(wallet_address)
print(balance)

# Get the transaction details
print(web3Object.eth.getTransaction('0xf776ea3410a5a7c4aea43f876e298be41e6659131557aab941975957b845121f'))



