import pzgram

bot = pzgram.Bot("BOTKEY")
pool_message = ""

# Create Pool Keyboard
button1 = pzgram.create_button("1", "choice1")
button2 = pzgram.create_button("2", "choice2")
k = [[button1, button2]] # Format button like "normal" keyboards
pool_keyboard = pzgram.create_inline(k)


def pool_command(chat):
    global pool_message, pool_keyboard
    pool_message = "What is your favourite number?"
    # Send the pool message, attaching the inline keyboard
    chat.send(pool_message, reply_markup=pool_keyboard)


def catch_results(query, data, message, sender):
    global pool_message, pool_keyboard
    # Convert query data to the "original" choice
    if data == "choice1":
        choice = "1"
    elif data == "choice2":
        choice = "2"
    # Edit the message text
    pool_message += "\n" + sender.first_name + ": " + choice  # Ex. infopz: 1
    message.edit(pool_message, reply_markup=pool_keyboard)
    # Send a notification to client
    query.reply("Choice registered correctly")


commands = {"pool": pool_command}
bot.set_commands(commands)

queries = {"choice1": catch_results, "choice2": catch_results}
bot.set_query(queries)

bot.run()
