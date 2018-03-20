import pzgram

bot = pzgram.Bot("BOTKEY")


def scrivi_riga(messaggio):
    file = open("diario.txt", "a")
    file.write("\n" + messaggio)
    file.close()


def leggi_riga(numero_riga):
    file = open("diario.txt", "r")
    righe = file.readlines()
    return righe[numero_riga]


def registra_command(message, chat):  # /registra Frase da registrare
    testo = message.text
    testo = testo.replace("/registra ", "")
    scrivi_riga(testo)
    chat.send("Messaggio Registrato!")


def visualizza_command(chat, message):  # /visualizza 2
    testo = message.text
    numero_riga = int(testo.replace("/visualizza ", ""))
    riga = leggi_riga(numero_riga)
    chat.send(riga)


comandi = {"visualizza": visualizza_command, "registra": registra_command}
bot.set_commands(comandi)
bot.run()
