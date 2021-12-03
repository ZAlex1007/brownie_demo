from brownie import network
from brownie.network import account
from scripts.helper import LOCAL_BLOCKCHAIN_ENVIRONMENTS, getAccount
from scripts.deploy import deploy_fund_me
from brownie import network, accounts, exceptions
import pytest


def test_fund_and_withdraw():
    account = getAccount()
    fundMe = deploy_fund_me()
    entrance_fee=fundMe.getEntranceFee() +100
    tx = fundMe.fund({'from': account, "value": entrance_fee})
    tx.wait(1)
    assert fundMe.addressToAmountFunded(account.address) == entrance_fee
    tx2= fundMe.withdraw({'from': account})
    tx2.wait(1)
    assert fundMe.addressToAmountFunded(account.address) == 0

def test_onlyOwnerCanWithdraw():
    if(network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS):
        pytest.skip()
    fundMe = deploy_fund_me()
    secondAcc = accounts.add() # new acc
    with pytest.raises(exceptions.VirtualMachineError):
        fundMe.withdraw({'from': secondAcc})
