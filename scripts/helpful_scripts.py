from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 20000000000

FORKED_LOCAL_ENVIRONMMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIROMMENTS = ["development", "ganache-local"]


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIROMMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_keys"])


def deploy_mocks():
    print("Active network is {}".format(network.show_active()))
    print("Deploying mocks....")
    if len(MockV3Aggregator) >= 0:
        MockV3Aggregator.deploy(
            DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from": get_account()}
        )

    print("Mocks deploy")
