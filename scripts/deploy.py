from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import (
    deploy_mocks,
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIROMMENTS,
)


def deploy_fund_me():
    account = get_account()
    # if we are in a persistance network, otherwise deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIROMMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    print("Contract deployed to {}".format(fund_me.address))
    return fund_me


def main():
    deploy_fund_me()
