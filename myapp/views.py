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

def homeView(request):
    if settings.APP_ENV == 'production':
        text: str = "New visitor\n\n"
        text += request.META.get('HTTP_USER_AGENT')
        telebot.send_message(text)
        
    return render(request, 'myapp/home.html')


def aboutView(request):
    
    
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


def commentRemove(request, pk):
    comment = Comments.objects.get(id=pk)

    comment.delete()

    return redirect('about-my-self')


def myResumeDownloadView(request):

    filename = './static/resume.pdf'

    response = FileResponse(open(filename, 'rb'))
    return response


def myProjectsView(request):

    projects = MyProjects.objects.all()
    context = {
        "projects": projects
    }
    return render(request, 'myapp/my-projects.html', context)


def myPojectsViewBot(request):
    projects = MyBots.objects.all()
    context = {
        'projects': projects
    }

    return render(request, 'myapp/my-projects-bot.html', context)


def contactPage(request):

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
                messages.success(
                    request, "Xabar yuborishda muammo yuzaga keldi, iltimos keyinroq harakar qilib ko'ring ")

            return redirect('contact-me')

    else:
        form = GetInTouchForm()

    context = {
        "form": form
    }

    return render(request, 'myapp/contact-me.html', context)
