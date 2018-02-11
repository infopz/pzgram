import requests


def api_request(key, method, param=None):
    data = requests.post("https://api.telegram.org/bot" + key + "/" + method, data=param)
    data = data.json()
    if not data['ok']:
        # TODO: Manage errors
        pass
    return data['result']
