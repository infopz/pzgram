# Manage Message

`pzgram` offers some functions to manage the messages that aren't a commands. By default these functions do nothing.

When the bot receive a message, both command and not, it will pass to a function called `processAll`. 

After, `pzgram` check if the message is a command or not, if it is a command, `pzgram` will call the related function, if it is a "normal" message, and
there isn't a function set in `set_next`, this message will be pass to 'processMessage' function.

These two function can receive the same parameters as the command functions, except for `args`. ([Visit the previous page](https://infopz.github.io/pzgram/guide2))
