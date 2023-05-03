from time import sleep
from ppadb.client import Client as AdbClient
import os
import sys
file = input('enter path of your wordlist: ')
def connect(l):
    client = AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037
    devices = client.devices()

    if len(devices) == 0:
        print('No devices')
        quit()

    device = devices[0]
    print(f'Connected to {device}')
    x = 0
    for i in l:
        if x <= 5:
            x += 1
            device.shell('input text {}'.format(i))
        elif x == 6:
            print('wating 30 seconds!...')
            sleep(30)
            x += 1
        elif x == 7 or x <= 10:
            device.shell('input text {}'.format(i))
            x += 1
        elif x >= 11:
            x += 1
            device.shell('input text {}'.format(i))
            sleep(30)
if os.path.exists(file) == True:
    f = open(file,'r+')
    li = f.readlines()
    connect(li)
else:
    print('the wordlist is not existing')
    sys.exit(0)
