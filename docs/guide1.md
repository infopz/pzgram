# Create your Bot
<br>

## Obtain the API key
In order to use your bot, you need to write a message to [@botfather](https://t.me/botfather), which is a bot designed to allow you create your own bots.
Once this is done, you'll be prompted with a series of questions. As soon as you've answered them all, you'll be given the API key:
This is personal, so don't publish it anywhere unless you desire misery and tragedy.

## Write the program
In order to use `pzgram` on your python program, you need to import it.

```python
import pzgram
```

After this, you have to create the `Bot` object, passing it the BotKey as a string. This will create an object, rappresenting your bot in all of his aspects. For more information, please visit [this page](https://infopz.github.io/pzgram/objects).

```python
bot = pzgram.Bot("BOTKEY")
```

Write the following code as last line of your program to start it.

```python
bot.run()
```

Follow the instruction on the next page to add features to your bot.

<div style:"float: right;"><a href="https://infopz.github.io/pzgram.guide2" style="text-decoration: none">Prossima Pagina</a></div>
