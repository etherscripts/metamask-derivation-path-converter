
# 🦊 Metamask Derivation Path Converter  
  
ℹ️ Данный скрипт разработан для конвертации Ethereum кошельков, использующий мнемоническую фразу **Metamask** для получения **нескольких кошельков** и отображения их адресов и закрытых ключей, предоставляет возможность иметь несколько Ethereum-аккаунтов используя **одну мнемоническую фразу**, позволяет **восстановить** уже созданные кошельки Metamask.  
  
📨 Канал Telegram: https://t.me/CryptoResearchLab  
  
💬 Чат Telegram: https://t.me/CryptoResearchLabChat  
  
💸 Донат (EVM): 0x000D34b907D21C416b9A457C9AA08b7390F8021c  
  
# ⚙️ Установка
  

    git clone https://github.com/etherscripts/metamask-derivation-path-converter 
    cd metamask-derivation-path-converter
    pip install -r requirements.txt

# 🚀 Использование 

    python main.py

После запуска программы используя cli интерфейс вам будет необходимо выбрать режим работы скрипта: 

 - Одиночная конвертация мнемонической фразы.
 - Массовая конвертация мнемонических фраз.

В варианте массовой конвертации вам необходимо заполнить файл input_mnemonics.txt, добавив необходимые мнемонические фразы. Результат конвертации будет сохранен в output_accounts.txt.