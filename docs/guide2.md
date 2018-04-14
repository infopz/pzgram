# Add Commands

All telegram bots work with a list of commands.

All commands are composed by `/` followed by a word. If the user sends some other words after the command, those words will be interpreted as parameters of that command.

`pzgram` connects a function to each command.

```python
def ping_command(chat, message, sender):
    print(sender.first_name, message.text)
    chat.send("Pong!")
    
commands = {"ping": ping_command}
bot.set_commands(commands)
```

As you can see the `ping_command` function,
is a simple function that prints the first name of the message sender and the text of the message and then it sends the message "Pong!" to the user that triggered the function.

In order to connect a command to a function, you need to create a dictionary containing, as key, the name of the command (`ping`) and the function that needs to be triggered (`ping_command`). This dictionary will be then given as parameter to the `set_command` method.

## Possible Parameters

You can give to the functions that represent the command (`ping_command`, for example) the parameters listed below:

* **message**: {Message Object} Data about the received message
* **chat**: {Chat Object} Chat in wich the message was sent
* **sender**: {User Object} User that sent the message
* **args**: {List} List of all words writed after the command name
* **bot**: {Bot Object}: The bot that received the message

## Set Next function

Usually, when a user writes a command, the bot asks him for some additional information. In order to catch these reply message you can use the `set_next` method of the bot.

When the bot will receive a message from that chat, it will be sent to this particular function,
`set_next`, which requires 2 parameters: the Chat object of that particular chat and the name of the function that receives the next message.

Example:

You need a bot that asks the phone number to a user after he writes '/start'.
```python
def start_command(chat):
    chat.send("Plese provide your phone number")
    bot.set_next(chat, receive_number)
  
def receive_number(message):
    print(message.text)
    
bot.set_commands({"start": start_command})
bot.run()
```
In this simple example, when an user writes `/start`, the bot replies asking for his phone number. After that, with the method
`bot.set_next`, the bot knows that he has to send the next message received from that chat to the function `receive_number`.

When the user writes his phone number and sends the message to the bot, the message is caught and send to function `receive_number` that prints it.

All other messages received will be managed as normal messages ([see the next page](https://infopz.github.io/pzgram/guide3))

## /start and /help

`pzgram` contains a default reply function to answer to the commands `/start` and `/help`

These default replies can be easily overwritten by giving a function to `bot.set_commands` as a normal command.

The default `/help` replying message contains a list of all commands that the bot has configured.
If you want to add more information about a command, you can write it as [docstring](http://www.pythonforbeginners.com/basics/python-docstrings) and it will appear in the reply message of `/help`

<div style="float: right;background-color: #fc0;padding: 6px;border-radius: 7px;"><a href="https://infopz.github.io/pzgram/guide3" style="text-decoration: none;color: #252525;">Next Page</a></div>
