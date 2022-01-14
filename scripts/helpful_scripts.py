import imp
from brownie import network, accounts, config

"""
If the network is in development, we use the fake account from ganace, else we use the account from our metamask wallet
when testing on Rinkeby network.
"""


def getAccount():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
