"""Utility functions for mysite"""
from .libs.telebot import telebot


def send_telegram(text: str) -> dict:
    """Use this function to send a telegram message"""
    text = "<b>New Session</b>"
    text += f"<b>Info</b>: {text}\n\n"
    telebot.send_message(text)


def get_client_ip(request):
    """Use this function to get a client IP"""
    data = request.META.get('HTTP_X_FORWARDED_FOR')
    if data:
        clinent_ip = data.split(',')[0]
    if not data:
        clinent_ip = request.META.get('REMOTE_ADDR')
    return clinent_ip
