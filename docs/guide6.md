# Groups and Channels

## Groups

All messages that come from a group, are managed from `pzgram` as a normal messages. To distinguish messages from private
chat and mesages from groups you can check the `type` attribute of the `Chat` object connected to that particular
message. This attributes can assume 4 values: private, group, supergroup and channel.

Also, `pzgram`, offers many functions that allows Bot to manage groups, most of them are methods of the `Chat` class, 
for example `get_members_count`, `kick_user` or `set_title`.

To get the complete list of these functions and to get more detail, view [this page](https://infopz.github.io/pzgram/objects).

## Channels

If you want to receive messages from a channel, you have to create a function, that can receive as parameters 
`message` and/or `chat`. To connect this function to the bot, you have to set it as the `channelPostFunc` attribute of the
Bot object.

For example, to forward all message from a channel to another user.
```python
def forward_post(message, chat):
    pzgram.Chat(bot, USER_ID).send("New message from channel " + chat.title)
    pzgram.Chat(bot, USER_ID).send(message.text)
    
bot.channelPostFunc = forward_post
```

To manage channels, you can use the same functions explained before for groups.

<div style="float: right;background-color: #fc0;padding: 6px;border-radius: 7px;"><a href="https://infopz.github.io/pzgram/guide7" style="text-decoration: none;color: #252525;">Next Page</a></div>
