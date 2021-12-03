from brownie import FundMe, MockV3Aggregator, network,config
from scripts.helper import getAccount, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3

def deploy_fund_me():
    account=getAccount()

    if(network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS):
        priceFeedAddress = config["networks"][network.show_active()]["eth_usd_priceFeed"]    
    else:
        deploy_mocks()
        priceFeedAddress=MockV3Aggregator[-1].address
  
    fund_me=FundMe.deploy(
            priceFeedAddress,
            {"from": account}, 
            publish_source=config["networks"][network.show_active()].get("verify"))
    
    return fund_me # pt test


def main():
    deploy_fund_me()