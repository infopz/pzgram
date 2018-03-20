# pzgram
A pz-way to create your Telegram Bot

```python
import pzgram
bot = pzgram.Bot(BOTKEY)

def hello(chat, message):
    chat.send("Messaggio ricevuto")
    print(message.text)
    
bot.set_commands({"hello": hello})
bot.run()
```

pzgram is a python library that allows you to create your personal Telegram bot, in a very easy way.


Italian documentation [here](https://github.com/infopz/pzgram/wiki)

For more information contact me:
* telegram: @infopz
* email: casari.giovanni@gmail.com
* website: [infopz.hopto.org](http://infopz.hopto.org)

**Supported Version**: Python 3.x

**License**: Apache License 2.0
