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

pzgram is a library that allows you to create your personal Telegram bot.
