# Inline Keyboard

Telegram allows to create two types of keyboards: "normal" keyboards and inline keyboards.

To create and manage normal keyboard, you can visit [this page](https://infopz.github.io/pzgram/guide5)

The inline keyboard are connected to a particular message, and when a user will press one of the buttons, a special type
of message, called query, will be sent to the bot.
Unlike the normal keyboard, the data that is inside a query can be different from the text that the user see in the button.
Moreover, a button can open a website, in that case, the bot will not receive a query.

To create an inline keyboard, first of all, you have to create the buttons.
To create a button, you have to use the `pzgram.create_button` function. It receives two parameters, the first it the
text fo the button, the second must be one of the following parameters:
* data: the data inside the query that the bot will receive if a user will press that button
* url: the website's url that the button have to open if pressed.

For example:
```python
button1 = pzgram.create_button("Command1", data="com1")
button2 = pzgram.create_button("WebSite", url="www.website.com")
```

Once you have done this, you have to create and array of arrays of buttons. The smaller arrays rappresent a row of the
keyboard, tha bigger one, rappresents the entire keyboard.
To obtain the keyboard object, you have to pass the created array to the function `pzgram.create_inline`, this will return
an object that you have to pass as `reply_markup` in methods like `chat.send`.

For example:
```python
k = [[button1, button2]]
keyboard = pzgram.create_keyboard(k)
chat.send("Press a Button!", reply_markup=keyboard)
```

