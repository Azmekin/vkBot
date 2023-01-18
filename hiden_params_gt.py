import json

import requests

token=""
group_id=207820607
def key_getter():
    r=requests.post("https://api.vk.com/method/groups.getLongPollServer",{"group_id":group_id,"access_token":token,"v":"5.131"})
    print(r.text)
    r1 = json.loads(r.text)
    try:
        r1=r1["response"]

        r1["server"]=r1["server"].replace("\\", "")
    except Exception as e:
        print(e)
    print(r1)
    return r1