# Create your Bot
<br>

## Obtain the API key
In order to use your bot, you need to write a message to [@botfather](https://t.me/botfather), which is a bot designed to allow you create your own bots.
Once this is done, you'll be prompted with a series of questions. As soon as you've answered them all, you'll be given the API key:
This is personal, so don't publish it anywhere unless you desire misery and tragedy.

## Write the program
In order to use `pzgram` on your python program, you need to import it.

```import pzgram```

After this, you have to create the `Bot` object, passing it the BotKey as a string. This will create an object, rappresenting your bot in all of his aspect. For more information, please visit [this page](https://infopz.github.io/pzgram/objects)

```bot = pzgram.Bot("BOTKEY") ```

Now your bot is ready to be runned, as the last line of your program, write

``` bot.run()```

This will start your bot.
