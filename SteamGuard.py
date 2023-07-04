import os
import time
import hmac
import json
import struct
import base64
import requests
from hashlib import sha1
import platform

BAR_LEN = 37
elements = ['-', '\\', '|', '/']

def getQueryTime():
    try:
        request = requests.post('https://api.steampowered.com/ITwoFactorService/QueryTime/v0001', timeout=30)
        json_data = request.json()
        server_time = int(json_data['response']['server_time']) - time.time()
        return server_time
    except:
        return 0


def getGuardCode(shared_secret):
    code = ''
    timestamp = time.time() + getQueryTime()
    _hmac = hmac.new(base64.b64decode(shared_secret), struct.pack('>Q', int(timestamp/30)), sha1).digest()
    _ord = ord(_hmac[19:20]) & 0xF
    value = struct.unpack('>I', _hmac[_ord:_ord+4])[0] & 0x7fffffff
    for i in range(5):
        code += symbols[value % len(symbols)]
        value = int(value / len(symbols))
    return code


def run_code():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    mafiles_dir = os.path.join(script_dir, 'maFiles')
    if not os.listdir(mafiles_dir):
        print("Directory is empty")
        return

    with os.scandir(mafiles_dir) as files:
        for file in files:
            if file.is_file() and file.name.endswith('.maFile'):
                with open(file, 'r') as file:
                    data = json.loads(file.read())
                    print(
                        f"Username: {data['account_name']}\n"
                        f"SteamId: {data['Session']['SteamID']}\n"
                        f"GuardCode: {getGuardCode(data['shared_secret'])}\n"
                    )

    time.sleep(1)  # Wait for 1 second before displaying the progress bar

    print("Press 'Ctrl+C' to stop the program.\n")

    # Progress bar
    for i in range(BAR_LEN+1):
        frame = i % len(elements)
        print(f'\r[{elements[frame]*i:=^{BAR_LEN}}]', end='', flush=True)

        time.sleep(0.2)
        
        i += 1
    if i > BAR_LEN:
        i = 0    

    print("\n")  # Line break after the progress bar
    clear_console()


def clear_console():
    # Clear the console based on the operating system
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


symbols = '23456789BCDFGHJKMNPQRTVWXY'

while True:
    clear_console()
    try:
        run_code()
    except KeyboardInterrupt:
        break
