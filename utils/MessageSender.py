from random import random

import requests

import hiden_params


class MessageSender:
    def send_message(message_info):
        a = {"user_id": message_info["user_id"], "message": message_info["message_text"], "random_id": str(int(random() * 100)),
             "access_token": hiden_params.token,
             "v": "5.131"
             }
        r = requests.post("https://api.vk.com/method/"
                          "messages.send", a)
        print(r.text)
    def test_send_mess(message_info):

        a = {"user_id": "137413706", "message": message_info["message_text"], "random_id": str(int(random()*100)),
             "access_token": hiden_params.token,
             "v": "5.131"
             }
        r = requests.post("https://api.vk.com/method/"
                          "messages.send", a)
        print(r.text)