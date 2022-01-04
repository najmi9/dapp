from brownie import SolidityStorage, accounts, network


def main():
    print(network.show_active())
    # requires brownie account to have been created
    if network.show_active()=='development':
        # add these accounts to metamask by importing private key
        owner = accounts[0]
        SolidityStorage.deploy({'from':accounts[0]})
    elif network.show_active() == 'rinkeby':
        # add these accounts to metamask by importing private key
        owner = accounts.load("rinkeby")
        SolidityStorage.deploy({'from':owner})
