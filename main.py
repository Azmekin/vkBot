# This is a sample Python script.
import json

import requests
from utils.Dispatcher import Dispatcher
from utils.MessageSender import MessageSender
import hiden_params

import asyncio
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def  askServer():

    r = requests.get(f"{hiden_params.server}"
                     f"?act=a_check&key={hiden_params.key_getter()}"
                     f"&ts={hiden_params.ts}&wait=1")
    obj = json.loads(r.text)
    print(obj)

    """   if r1!=r:
            for i in obj["updates"]:
            MessageSender.test_send_mess(Dispatcher.getMessage(i))
"""



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    r1={}
    while True:
        askServer()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
