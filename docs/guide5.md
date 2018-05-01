# Custom Keyboard

Telegram allows the bot to change the default keyboard, replacing it with a new one created bey the programmer, and the users can use
it to send "pre-writed" messages to the bot.

A custom keyboard is an array of array of keyboards button. Each small arrays rappresent a row, and the big array rapprents the entire keyboard.

A keyboard button can be a string if it only have to send that text to the bot, but it can be a dict if some actions are required.

Possbile attributes of the dict:
* text : String, required, the text of the button
* request_contact : Bool, ask user to send a contact
* request_location : Bool, ask user to send the current position

In order to create a keyboard, in `pzgram` you have to write:
```python
keyboard_array = [["Button1", "Button2"],["Button3"]]
keyboard = pzgram.create_keyboard(keyboard_array)
```

`create_keyboard` will return an object that you have to pass to `chat.send` as `reply_markup` object.
`create_keyboard` can receive, over the array, 2 parameters:
* one : Bool, default False, if is True, when user press a button the keyboard disappers
* resize : Bool, default True, if is True, telegram adapts the keyboard to use less space.

In order to send the keyboard, you have to write:
```python
chat.send("Press a button", reply_markup=keyboard)
```

This is an example of how to use the keyboard:
```python

def start_command(chat):
  keyboard = pzgram.create_keyboard([["Command1", "Command2"]])
  chat.send("Select a command", reply_markup=keyboard)
  
def process_message(message, chat):
  if message.text == "Command1":
    function1()
  elif message.text == "Command2":
    function2()  
```

<div style="float: right;background-color: #fc0;padding: 6px;border-radius: 7px;"><a href="https://infopz.github.io/pzgram/guide6" style="text-decoration: none;color: #252525;">Next Page</a></div>
