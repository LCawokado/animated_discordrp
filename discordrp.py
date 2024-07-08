import os
try:
    import psutil
    from pypresence import Presence
    import time
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from colorama import Fore, Style, init
    from pystyle import Write, Colors
    import json
except:
    os.system('pip install psutil')
    os.system('pip install pypresence')
    os.system('pip install selenium')
    os.system('pip install colorama')
    os.system('pip install pystyle')
    from pystyle import Write, Colors
    import psutil
    from pypresence import Presence
    import time
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from colorama import Fore, Style, init
    import json

init()
chois = input(f'Load settings from ./config/config.json? (y/n) ~> ')
if chois == 'y' or chois == 'Y':
    with open('config/config.json', 'r') as f:
        config = json.load(f)
    client_id = config["client_id"]
    details = config["details"]
    state = config["state"]
    texttoedit = config["texttoedit"]
    images = config["images"]
    buttons = config["buttons"]
else:
    client_id = input('Enter your application`s id ~> ')
    details = input('Enter first string of activity ~> ')
    state = input('Enter second string of activity ~> ')
    texttoedit = input('Enter unstatic application name ~> ')
    photos = input('Including images? (y/n) ~> ')
    images = []

    if photos == 'y' or photos == 'Y':
        num = int(input('Hmany images we will use? ~> '))
        for i in range(num):
            images.append(input(f"{i+1} photo name ~> "))
    buttons = None
    but = input('Including buttons? (y/n) ~> ')
    if but == 'y' or but == 'Y':
        num = int(input('Hmany buttons? (max 2) ~> '))
        buttons = []
        for i in range(num):
            buttons.append({"label": input(f'Button {i+1} text ~> '), "url": input(f'Button {i+1} url ~> ')})
    configuration = {
        "client_id": client_id,
        "details": details,
        "state": state,
        "texttoedit": texttoedit,
        "images": images,
        "buttons": buttons
    }
    with open("config/config.json", "w") as outfile:
        outfile.write(json.dumps(configuration, indent=4))
url = f'https://discord.com/developers/applications/{client_id}/information'
def auth(token: str) -> None:
    """Auth in discord via token"""
    url_login = url
    driver.get(url_login)
    time.sleep(2)
    driver.execute_script(
        f"setImmediate(() => document.body.appendChild(document.createElement('iframe')).contentWindow.localStorage.token = '\"{token}\"');"
        )
    driver.refresh()


more = True
vmore = False
driver = webdriver.Chrome()
driver.get(url)


auth(input('Token ~> '))
print('Autharised')
time.sleep(10)
a = 0
text = texttoedit[0]
while True:  # The presence will stay on as long as the program is running
    a += 1
    input_field = driver.find_element(By.XPATH,'//*[@id="app-mount"]/div/div/div[2]/div[3]/div/div/form/div[2]/div/div/div[2]/div/div[1]/div/div/input')
    input_field.clear()
    if more:
        text += f'{texttoedit[1:][a%len(texttoedit[1:])-1]}'
        if len(text) == len(texttoedit):
            more = False
            vmore = True
    else:
        text = text[:-1]
        if len(text) == 2:
            more = True
            vmore = False
    input_field.send_keys(text)
    time.sleep(1)
    save_button = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div[3]/div/div/div/div/div/div[2]/button[2]')
    save_button.click()
    time.sleep(2)
    if a%2 ==0:
        RPC = Presence(client_id, pipe=0)  # Initialize the client class
        RPC.connect()  # Start the handshake loop
        if len(images) == 0:
            RPC.update(details=details, state=state, buttons=buttons)  # Set the presence
        else:
            RPC.update(details=details, state=state, large_image=images[a%len(images)])  # Set the presence
        try:
            RPC1.close()
        except:
            pass
    else:
        RPC1 = Presence(client_id, pipe=0)  # Initialize the client class
        RPC1.connect()  # Start the handshake loop
        if len(images) == 0:
            RPC1.update(details=details, state=state, buttons=buttons)  # Set the presence
        else:
            RPC1.update(details=details, state=state, large_image=images[a % len(images)])  # Set the presence
        try:
            RPC.close()
        except:
            pass
    Write.Print(f'Updated application name to ', color=Colors.purple_to_blue, interval=0.000); Write.Print(f'{text}\n', color=Colors.red_to_yellow, interval=0.000)
    time.sleep(10)  # Can only update rich presence every 15 seconds