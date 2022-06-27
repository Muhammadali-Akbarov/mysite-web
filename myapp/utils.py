from .libs.telebot import telebot

def sendTelegram(request):
    text = f"<b>New Session</b>"
    text += f"<b>Home</b>:  {request.META.get('HOME')}\n\n"
    text += f"<b>User-Agent</b>: {request.META.get('HTTP_USER_AGENT')}"
    telebot.send_message(text)