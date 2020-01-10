import apiai, json, vk_api, time, random

def vkListener():
    token = "5b64b6cb8d398393a6b0c6dd17fa96bb396d9b152addd1f320c48601ace291fdbbffdcbff7de3be58daa8"
    vk = vk_api.VkApi(token=token)
    vk._auth_token()
    while True:
        try:
            messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
            if messages["count"] >= 1:
                id = messages["items"][0]["last_message"]["from_id"]
                body = messages["items"][0]["last_message"]["text"]
                vk.method("messages.send", {"peer_id": id, "message": textMessage(body),
                                            "random_id": random.randint(1, 2147483647)})
                print(body)
        except Exception as E:
            time.sleep(1)

def textMessage(s):
    request = apiai.ApiAI('d43efda4b9bb46c49e37e1bf45e3830e').text_request()
    request.lang = 'en'
    request.session_id = 'smartbot'
    request.query = s
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']
    if response:
        return response
    else:
        return 'Я Вас не понял.'

vkListener()