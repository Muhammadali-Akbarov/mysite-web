from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.http.response import FileResponse

from .forms import CommentForm
from .forms import GetInTouchForm

from .models import MyBots
from .models import Comments
from .models import MyProjects

from .libs.telebot import telebot

from .utils import get_client_ip
from .utils import send_telegram


def home_view(request):
    """The Home View"""
    if settings.APP_ENV == 'production':
        client_ip, user_agent = get_client_ip(request)
        send_telegram(**{
            "client_ip": client_ip,
            "user_agent": user_agent,
        })

    return render(request, 'myapp/home.html')


def about_view(request):
    """Th About View"""
    items = Comments.objects.all()

    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()

            return redirect('about-my-self')

    else:
        form = CommentForm()

    context = {
        "form": form,
        "items": items,
    }
    return render(request, 'myapp/about.html', context)


def comment_remove_view(request, primary_key):
    """The Comment Remove View"""
    if request:
        comment = Comments.objects.get(id=primary_key)
        comment.delete()

    return redirect('about-my-self')


def my_resume_download_view(request):
    """The My Resume Download View
        uses for download resume."""
    if request:
        filename = './static/resume.pdf'
        response = FileResponse(open(filename, 'rb'))

        return response


def my_projects_view(request):
    """The My Projects View
        uses for see projects."""
    projects = MyProjects.objects.all()
    context = {
        "projects": projects
    }
    return render(request, 'myapp/my-projects.html', context)


def my_bot_projects_view(request):
    """The My Bot Projects View
        uses for see my bot projects
    """
    projects = MyBots.objects.all()
    context = {
        'projects': projects
    }

    return render(request, 'myapp/my-projects-bot.html', context)


def contact_page_view(request):
    """The Contact Page View
        uses for contact with me
    """
    if request.POST:
        form = GetInTouchForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            text = f"Xabar yuborgan shaxs: {obj}\nEmail: {obj.email}\nXabar matni: {obj.body}"
            resp = telebot.send_message(text)
            if resp.status_code == 200:
                messages.success(
                    request, 'Xabaringiz muofaqqiyati yuborildi, tez oraqa sizga javob beramiz!')
            else:
                mess: str = "Xabar yuborishda muammo yuzaga keldi,"
                mess += " iltimos keyinroq harakar qilib ko'ring"
                messages.error(request, mess)

            return redirect('contact-me')

    else:
        form = GetInTouchForm()

    context = {
        "form": form
    }

    return render(request, 'myapp/contact-me.html', context)
