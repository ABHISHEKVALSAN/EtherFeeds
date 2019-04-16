import json
import web3
import time
import pickle
from eth_account import Account
from web3 import Web3, HTTPProvider
from solcx import compile_source
from web3.contract import ConciseContract


dbfile = open('/home/abhiavk/git/EtherFeeds/etherfeeds/contract_abi', 'rb')
contract_abi=pickle.load(dbfile)
dbfile.close()

dbfile = open('/home/abhiavk/git/EtherFeeds/etherfeeds/contract_addr', 'rb')
contract_addr=pickle.load(dbfile)
dbfile.close()

w3 = Web3(HTTPProvider('https://ropsten.infura.io/v3/0d917ac7376a4526a3a9cb9306bfec30'))
w3.eth.enable_unaudited_features()

contract = w3.eth.contract(
    address=contract_addr,
    abi=contract_abi,
)

acct = Account()
acct = w3.eth.account.privateKeyToAccount('CDD46AA3C0F33B3283CEC649C0C09BC374D90999683077373A843BA0363B162F')
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

def addQu(questionAsker,newUser,q_hash):
	txn_dict={'from': acct.address,
	'nonce': w3.eth.getTransactionCount(acct.address),
	'gas': 2000000,
	'gasPrice': w3.toWei('50', 'gwei')}
	tx_hash=contract.functions.addMember(newUser).buildTransaction(txn_dict)
	signed = acct.signTransaction(tx_hash)
	txn_hash=w3.eth.sendRawTransaction(signed.rawTransaction)
	tx_receipt = w3.eth.waitForTransactionReceipt(txn_hash)
	return tx_receipt
