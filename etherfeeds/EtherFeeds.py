import json
import web3
import time
import pickle
from eth_account import Account
from web3 import Web3, HTTPProvider
from solcx import compile_source
from web3.contract import ConciseContract
import sys

PATH="/home/abhiavk/git/EtherFeeds/"

try:
	dbfile = open('/home/abhiavk/git/EtherFeeds/etherfeeds/contract_abi', 'rb')
	contract_abi=pickle.load(dbfile)
	dbfile.close()

	dbfile = open('/home/abhiavk/git/EtherFeeds/etherfeeds/wallet_signature', 'rb')
	wallet_signature=pickle.load(dbfile)
	dbfile.close()

	dbfile = open('/home/abhiavk/git/EtherFeeds/etherfeeds/contract_addr', 'rb')
	contract_addr=pickle.load(dbfile)
	dbfile.close()
except:
	print("Change the PATH variable in EtherFeeds.py your directory")
	exit(0)

w3 = Web3(HTTPProvider('https://ropsten.infura.io/v3/0d917ac7376a4526a3a9cb9306bfec30'))
w3.eth.enable_unaudited_features()

contract = w3.eth.contract(
    address=contract_addr,
    abi=contract_abi,
)

acct = Account()
acct = w3.eth.account.privateKeyToAccount(wallet_signature)
def authUser(user):
	return contract.functions.isMemberOf(user).call()
def addUser(oldUser,newUser):
	txn_dict={'from': acct.address,
	'nonce': w3.eth.getTransactionCount(acct.address),
	'gas': 1728712,
	'gasPrice': w3.toWei('21', 'gwei')}
	tx_hash=contract.functions.addMember(newUser).buildTransaction(txn_dict)
	signed = acct.signTransaction(tx_hash)
	txn_hash=w3.eth.sendRawTransaction(signed.rawTransaction)
	tx_receipt = w3.eth.waitForTransactionReceipt(txn_hash)
	return tx_receipt

def addQu(questionAsker,questionid,q_hash):
	txn_dict={'from': acct.address,
	'nonce': w3.eth.getTransactionCount(acct.address),
	'gas': 2000000,
	'gasPrice': w3.toWei('50', 'gwei')}
	tx_hash=contract.functions.addMember(questionid).buildTransaction(txn_dict)
	signed = acct.signTransaction(tx_hash)
	txn_hash=w3.eth.sendRawTransaction(signed.rawTransaction)
	tx_receipt = w3.eth.waitForTransactionReceipt(txn_hash)
	return tx_receipt
