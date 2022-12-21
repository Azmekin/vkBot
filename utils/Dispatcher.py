import hiden_params


class Dispatcher:
    def getMessage(slov):
        slov=slov["object"]
        slov=slov["message"]
        message_info={}
        message_info["user_id"]=slov["from_id"]
        #message_info["message_id"]=slov["id"]
        message_info["message_text"]=slov["text"]
        message_info["token"] = hiden_params.token
        message_info["v"]="5.131"
        return message_info

