import pzgram
import requests

bot = pzgram.Bot("BOTKEY")
old_ip = "not_set"
adminId = 123456789 # Change with your user id


def get_my_ip():
    p = requests.get("http://ipinfo.io/ip")
    return p.text


def ip_command(chat, message):
    if message.sender.id != adminId:
        chat.send("Non sei autorizzato a eseguire questo comando")
    else:
        ip = get_my_ip()
        messaggio = "Il tuo ip e' " + ip
        chat.send(messaggio)


def check_for_changes():
    global old_ip
    new_ip = get_my_ip()
    if old_ip == "not_set":
        pzgram.Chat(bot, adminId).send("Il tuo ip e' " + new_ip)
        old_ip = new_ip
    elif new_ip != old_ip:
        messaggio = "Il tuo ip e' cambiato\nQuello nuovo e': " + new_ip
        pzgram.Chat(bot, adminId).send(messaggio)
        old_ip = new_ip


comandi = {"ip": ip_command}
bot.set_commands(comandi)
bot.timers = {60: check_for_changes}
bot.run()
