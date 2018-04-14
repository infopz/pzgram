# Manage Message

`pzgram` offers some functions to manage the messages that aren't a commands. By default these functions do nothing.

When the bot receives a message, it will pass to a function called `processAll` whether it contains command or not. 

After, `pzgram` checks the command's nature: if it is a command, `pzgram` will call the related function, if it is a "normal" message, and
there isn't a function set in `set_next`, this message will be pass to 'processMessage' function.

These two function can receive the same parameters as the command functions, except for `args`. ([Visit the previous page](https://infopz.github.io/pzgram/guide2))
