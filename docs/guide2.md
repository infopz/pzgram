# Add Commands
<br>

All telegram bots work with a list of commands.

All commands are structured in this way: `/` followed by a word. If the user send some other words after the command, they will be interpreted as parameters of the command.

`pzgram` connects to each command a function.

```python
def ping_command(chat, message, sender):
    print(sender.first_name, message.text)
    chat.send("Pong!")
    
commands = {"ping": ping_command}
bot.set_commands(commands)
```

As you can see, i wrote the `ping_command` function, 
that is a simple function that prints the first name of the message sender and the text of the message and send to the chat the message "Pong!".

To connect this funcion to the command `/ping`, i pass to the `set_commands` method of the bot, a dictionary containing as a key, the string with the name of the command,
and as the value, the funcion name (without the round brackets)

## Possible Parameters

You can write as function parameters the ones listed below:

* **message**: {Message Object} Data about the received message
* **chat**: {Chat Object} Chat in wich the message was sent
* **sender**: {User Object} User that sent the message
* **args**: {List} List of all words writed after the command name
* **bot**: {Bot Object}: The bot that received the message

## Set Next

Usually, when a user write a command, the bot ask him some additional information, to catch these reply message, with `pzgram`, you can use the `set_next` method of the bot.
This function requires 2 parameters: the Chat object of that chat and the name of the function that receive the next message.

Example:

I need a bot that ask the phone number to a user after he write '/start'.
```python
def start_command(chat):
    chat.send("Plese give me your phone number")
    bot.set_next(chat, receive_number)
  
def receive_number(message):
    print(message.text)
    
bot.set_commands({"start": start_command})
bot.run()
```
In this simple example, when an user wrote `/start`, the bot reply asking for his phone number. After, with the method
`bot.set_next`, the bot knows that he have to pass the next message received from that chat, to the function `receive_number`.

When the user write his phone number and send the message to the bot, the message is caught and send to function `receive_number` that print it.

## /start and /help

`pzgram` contains the default reply function to answer to command `/start` e `/help`

These default replies can be overwritten by passing a function to `bot.set_commands` as a normal command.

The default `/help` replying message contains a list of all commands that the bot has configured.

<div style="float: right;background-color: #fc0;padding: 6px;border-radius: 7px;"><a href="https://infopz.github.io/pzgram/guide3" style="text-decoration: none;color: #252525;">Next Page</a></div>
