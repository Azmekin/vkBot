import requests

import hiden_params


class MessageSender:
    def send_message(message_info):

        r = requests.post("https://api.vk.com/method/"
                          "messages.send", message_info)
        print(r.text)
    def test_send_mess(message_info):
        a = {"user_id": "137413706", "message": message_info["message_text"], "random_id": "50",
             "access_token": "vk1.a.-f8AfZYrXdup14hugzLmgGPSAMMYaRuZkHjhirckvk7Q6GkBCjPKEgSMqkCTDZ915vontp5ySBRGnG6hUYFHu8nP6IH0ByZIpimpUiZLdmVmfWCQomfwL5TuyIO6Rd6Cj6nosM7xfikL4a6T988x6WeO__h3a_-KYgosFZXf8TmIDuUQcuXO84DlFRc0U9A5DF-Xk2zdgsZYOdloSVTbDw",
             "v": "5.131"
             }
        r = requests.post("https://api.vk.com/method/"
                          "messages.send", a)
        print(r.text)