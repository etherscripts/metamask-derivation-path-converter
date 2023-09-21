# Coded by: https://t.me/CryptoResearchLab

from web3 import Web3


def convert_mnemonic(range_input, mnemonic_input):
    try:
        w3 = Web3(Web3.HTTPProvider(""))
        w3.eth.account.enable_unaudited_hdwallet_features()

        for r in range(range_input):
            account = w3.eth.account.from_mnemonic(mnemonic_input, account_path=f"m/44'/60'/0'/0/{r}")
            account_address = account.address
            account_private_key = w3.to_hex(account._private_key)
            print(f"(R:{r}) | A: {account_address} | PK: {account_private_key}")
    except Exception as e:
        print(e)


def start():
    try:
        user_range_input = int(input("Введите номер диапазона мнемонической деривации: "))
        user_mnemonic_input = input("Введите мнемоническую фразу Metamask: ")

        convert_mnemonic(user_range_input, user_mnemonic_input)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    start()

# Coded by: https://t.me/CryptoResearchLab
