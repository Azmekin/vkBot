# This is a sample Python script.
import json
from time import sleep

import requests
from utils.Dispatcher import Dispatcher
from utils.MessageSender import MessageSender
import hiden_params

import asyncio
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def  askServer():
    params=hiden_params.key_getter()
    r = requests.get(f"{params['server']}"
                     f"?act=a_check&key={params['key']}"
                     f"&ts={params['ts']}&wait=1")
    obj = json.loads(r.text)
    print(obj)
    for i in obj["updates"]:
        #MessageSender.test_send_mess(Dispatcher.getMessage(i))
        MessageSender.send_message(Dispatcher.getMessage(i))




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    r1={}
    while True:
        askServer()
  #      sleep(1)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
