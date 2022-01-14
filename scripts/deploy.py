from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import getAccount


def deployFundMe():
    # First we need to get account
    account = getAccount()
    # pass the price feed into the deploy as we have now added the constructor.
    # if we are on persistent network (rinekby) use the associated address otherwise deploy mocks.
    if network.show_active() != "development":
        priceFeedAddress = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    fundMe = FundMe.deploy(
        priceFeedAddress,
        {"from": account},
        publish_source=True,
    )
    print(f"Contract deployed to {fundMe.address}")


def main():
    deployFundMe()
