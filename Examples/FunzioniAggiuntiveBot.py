import pzgram

bot = pzgram.Bot("BOTKEY")


def print_all_message(message, chat):
    print(message.text)
    chat.send("Messaggio Ricevuto dalla prima funzione")


def print_only_message(message, chat):
    print(message.text)
    chat.send("Messaggio Ricevuto dalla seconda funzione")


def prova_command(message, chat):
    print(message.text)
    chat.send("Comando ricevuto dalla seconda funzione")


bot.processAll = print_all_message
bot.processMessage = print_only_message
comandi = {"prova": prova_command}
bot.set_commands(comandi)
bot.run()

# Spiegazione
#
# Ciascun messaggio quando arriva passa dalla funzione processAll,
# a questo punto, se e' un comando viene eseguita la corrispettiva funzione,
# altrimenti viene richiamata la funzione processMessage
