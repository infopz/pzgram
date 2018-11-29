# Timers

`pzgram` allows you to create some functions that can be repeated every amount of time, these functions are called `timers`.

In order to create a timer, you have to write a function, that must have 0 parameter.

To connect this function with bot you have to use the `set_timers` method of the `Bot` object, passing it a dictionary containing as
keys the amount of time (in seconds) in wich the function have to be repeated, and ad values the function name.

Example:
```python
def hello():
    pzgram.Chat(bot, USER_ID).send("Hi")
    
timers = {60: hello}
bot.set_commands(timers)
```

In this example the function `hello` will be repated every 60 seconds.

<div style="float: right;background-color: #fc0;padding: 6px;border-radius: 7px;"><a href="https://infopz.github.io/pzgram/guide5" style="text-decoration: none;color: #252525;">Next Page</a></div>
