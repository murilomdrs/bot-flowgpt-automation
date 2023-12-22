"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""


# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

url_gpt = 'https://flowgpt.com/chat'
prompt = "Você poderia gerar no formato json com o nome 'produtos' os dados de 3 produtos eletrônicos contendo as informações de nome, categoria, codigo, identificador, descricao, preco e quantidade?"

def coletar_dados():

    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME

    # Acessando o site para iniciar o chat
    bot.browse(url_gpt)
    bot.maximize_window()

    welcome_modal = bot.find_element("//div[@class='chakra-stack css-15zvycm']", By.XPATH)
    bot.wait_for_element_visibility(welcome_modal)
    if welcome_modal:
        print('[DEBUG] welcome modal:', welcome_modal)
        lets_go_btn = bot.find_element("//button[contains(text(), 'go!')]", By.XPATH)
        lets_go_btn.click()

    input_chat_field = bot.find_element("//textarea[@data-testid='chat-input-textarea']", By.XPATH)
    input_chat_field.send_keys(prompt)
    send_btn = bot.find_element("//button[@aria-label='Send']", By.XPATH)
    send_btn.click()
    bot.wait(2000)

    send_attribute = send_btn.get_attribute('disabled')
    print('[DEBUG] send_attribute:', send_attribute)

    while send_btn.get_attribute('disabled') == 'true':
        print("[INFO] get_attribute('disabled'): aguardando os dados serem gerados.")
        bot.wait(2000)

    try:
        dados_gerados = bot.find_element("language-json", By.CLASS_NAME).get_attribute('textContent')
        print('[DEBUG] dados_gerados:', dados_gerados)

    except Exception as ex:
        print('[DEBUG] Exception:', ex)

    input("Ok para continuar")

    bot.stop_browser()

def main():
    coletar_dados()

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()
