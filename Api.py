import requests


def api_request(botkey, method, param=None):
    data = requests.post("https://api.telegram.org/bot" + botkey + "/" + method, data=param)
    data = data.json()
    if not data['ok']:
        # TODO: Manage errors
        pass
    return data['result']
