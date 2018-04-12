# HomePage

* [HomePage](https://infopz.github.io/pzgram/)
* [Guide](https://infopz.github.io/pzgram/guide0)
  * [Install pzGram](https://infopz.github.io/pzgram/install)
  * [Create your Bot](https://infopz.github.io/pzgram/guide1)
  * [Add Commands](https://infopz.github.io/pzgram/guide2)
  * [Manage Messages](https://infopz.github.io/pzgram/guide3)
  * [Timers](https://infopz.github.io/pzgram/guide4)
  * [Custom Keyboards](https://infopz.github.io/pzgram/guide5)
  * [Groups & Channels](https://infopz.github.io/pzgram/guide6)
  * [Inline Keyboard](http://infopz.github.io/pzgram/guide7)
* [Objects](https://infopz.github.io/pzgram/objects)
* [Changelogs](https://infopz.github.io/pzgram/changelogs)

**pzGram** is a Python3 library that allows you to create your Telegram bot focusing on what the bot has to do and not on how the bot works.

```python
import pzgram
bot = pzgram.Bot(BOTKEY)

def hello(chat, message)
    chat.send("Message Received")
    print(message.text)
    
bot.set_commands({"hello": hello})
bot.run()
```

The current version of pzGram support all types of messages, from users, groups and channels, but it does not support payments and games yet.

pzGram is an open-source project, created by Giovanni Casari.

For more information contact me:
* Telegram: @infopz
* Email: casari.giovanni@gmail.com
* Website: [infopz.hopto.org](http://infopz.hopto.org/)

**Supported Version:** Python 3.x

**License:** Apache 2.0
