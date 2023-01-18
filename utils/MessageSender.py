from random import random

import requests

import hiden_params


class MessageSender:
    def send_message(message_info):

        r = requests.post("https://api.vk.com/method/"
                          "messages.send", message_info)
        print(r.text)
    def test_send_mess(message_info):

        a = {"user_id": "137413706", "message": message_info["message_text"], "random_id": str(int(random()*100)),
             "access_token": "vk1.a.URLQjKYG7GoTX7xmKES9RyXPrNU8CcDknfKNulIvvPdv7cIWU0IhyiiEczl_scMXek8o_uKOVP0Uo_D18fqvzLUQqrbUpgMHDDf91-9DvUsDRdorqZYJd5_q1paV72FQ1YyIiu-nLJ4FUbGNE5fNslvgzcQFk8SeRx0tUtta2w6NkLit5baCHWegwusZQsOMF_OqphS0g5yteVSOndPuVQ",
             "v": "5.131"
             }
        r = requests.post("https://api.vk.com/method/"
                          "messages.send", a)
        print(r.text)