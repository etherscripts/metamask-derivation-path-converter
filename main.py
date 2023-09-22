# Coded by: https://t.me/CryptoResearchLab

from web3 import Web3

w3 = Web3(Web3.HTTPProvider(""))
w3.eth.account.enable_unaudited_hdwallet_features()


def single_convert(range_input, mnemonic_input):
    try:
        for r in range(range_input):
            account = w3.eth.account.from_mnemonic(mnemonic_input, account_path=f"m/44'/60'/0'/0/{r}")
            account_address = account.address
            account_private_key = w3.to_hex(account._private_key)
            print(f"A: {account_address} | PK: {account_private_key}")
    except Exception as error:
        print(f"Возникла ошибка: {error}.")


def mass_convert(range_input):
    try:
        mnemonics_input_file = "data/input_mnemonics.txt"
        accounts_output_file = "data/output_accounts.txt"
        with open(mnemonics_input_file, 'r') as mnemonics_file, open(accounts_output_file, 'w') as accounts_file:
            for mnemonics in mnemonics_file:
                mnemonic = mnemonics.strip()
                for r in range(range_input):
                    account = w3.eth.account.from_mnemonic(mnemonic, account_path=f"m/44'/60'/0'/0/{r}")
                    account_address = account.address
                    account_private_key = w3.to_hex(account._private_key)
                    print(f"A: {account_address} | PK: {account_private_key}")
                    accounts_file.write(f"{account_address} | {account_private_key}\n")
            print("Результат сохранен в output_accounts.txt.")

    except Exception as error:
        print(f"Возникла ошибка: {error}.")


def start_single_converter():
    try:
        user_range_input = int(input("Введите номер диапазона мнемонической деривации: "))
        user_mnemonic_input = str(input("Введите мнемоническую фразу Metamask: "))

        single_convert(user_range_input, user_mnemonic_input)
    except Exception as error:
        print(f"Возникла ошибка: {error}.")


def start_mass_converter():
    try:
        user_range_input = int(input("Введите номер диапазона мнемонической деривации: "))

        mass_convert(user_range_input)
    except Exception as error:
        print(f"Возникла ошибка: {error}.")


def start():
    try:
        print(
            "Режимы работы: 1. Одиночная конвертация мнемонической фразы., 2. Массовая конвертация мнемонических фраз.")
        user_mode_input = int(input("Введите номер режима работы конвертора: "))
        if user_mode_input == 1:
            start_single_converter()
        elif user_mode_input == 2:
            start_mass_converter()
        else:
            print("Возникла ошибка: Неверный метод режима работы.")
    except Exception as error:
        print(f"Возникла ошибка: {error}.")


if __name__ == '__main__':
    start()
