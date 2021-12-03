from brownie import FundMe
from brownie import FundMe
from scripts.helper import getAccount
def fund():
    fundMe= FundMe[-1]
    account= getAccount()
    entrance_fee=fundMe.getEntranceFee()
    fundMe.fund({'from': account, "value": entrance_fee})


def withdraw():
    fundMe= FundMe[-1]
    account= getAccount()
    fundMe.withdraw({'from': account})


def main():
    fund()
    # withdraw()