from brownie import config, network, accounts, MockV3Aggregator
from web3 import Web3 



FORKED_MAINNET_ENVIRONMENTS = ["mainnet_fork", "mainnetfork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS=["development", "ganache-local"]
DECIMALS = 8
PRICE = 200000000000

def getAccount():
    if ( network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_MAINNET_ENVIRONMENTS) :
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    if(len(MockV3Aggregator) <=0):
            MockV3Aggregator.deploy(DECIMALS, PRICE, {"from": getAccount()})