# Manage Message

`pzgram` offers some functions to manage the messages that aren't a commands. By default these functions do nothing.

When the bot receives a message, it will pass to a function called `processAll` whether it contains command or not. 

After, `pzgram` checks the command's nature: if it is a command, `pzgram` will call the related function, if it is a "normal" message, and
there isn't a function set in `set_next`, this message will be pass to `processMessage` function.

These two function can receive the same parameters as the command functions, except for `args`. ([Visit the previous page](https://infopz.github.io/pzgram/guide2))

To connect a function to this method, you have to edit the bot attibute called as the function

`bot.processMessage = your_function`

**Example**
```python
def start_command(chat):
    chat.send("Send `ping` to call the command", parse_mode="markdown")
    
def process_message(message):
    if message.text == "ping":
        do_something()

bot.set_commands({"start": start_command})
bot.processMessagge = process_message
bot.run()
```

In this example, when the user sends the `/start` command, it replies saying that the user have to write `ping` to call a command.

When a new message arrives, it is sent to the function connected to `processMessage`, that is `process_message`. It receives this new message and check if the text is equals to `ping`.

This became useful with [Customized Keyboard](https://infopz.github.io/pzgram/guide5)

## Start & End Function

`pzgram` allows you to connect a function that will be called at the start or at the end of the bot running.

`startFunc` is the name of the attribute of the bot object, and as the `processMessage` function, if you want to connect a function to it, you have to write `bot.startFunc = your_function`. It will be called before the bot start checking for new messages.

`endFunc` is the same, but it will be called when the bot stopping itself, so when the user quit the program.

## Edited Messages

`editFunc` is a function that permits you to manage the edited messages.

As the other functions in this page, it can receive all parameters that command functions receives exept for `args`.

To connect a function, you have to write `bot.editFunc = your_function`

<div style="float: right;background-color: #fc0;padding: 6px;border-radius: 7px;"><a href="https://infopz.github.io/pzgram/guide4" style="text-decoration: none;color: #252525;">Next Page</a></div>
