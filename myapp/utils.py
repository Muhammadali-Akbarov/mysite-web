"""Utility functions for mysite"""
from .libs.telebot import telebot


def send_telegram(*args, **kwargs) -> dict:
    """Use this function to send a telegram message"""
    text = "New Session\n"
    text += f"IP: {kwargs.get('client_ip')}\n\n"
    text += f"Info {kwargs.get('user_agent')}\n"
    telebot.send_message(text)


def get_client_ip(request):
    """Use this function to get a client IP"""
    data = request.META.get('HTTP_X_FORWARDED_FOR')
    user_agent = request.META.get('HTTP_USER_AGENT')
    if data:
        clinent_ip = data.split(',')[0]
    if not data:
        clinent_ip = request.META.get('REMOTE_ADDR')

    return clinent_ip, user_agent
