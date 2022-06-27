from django.urls import path
from .views import contactPage, homeView,aboutView,commentRemove, myPojectsViewBot,myResumeDownloadView,myProjectsView

urlpatterns = [

    path('',homeView,name='home'),
    path('about-my-self/',aboutView,name='about-my-self'),
    path('about-my-self/<str:pk>/',commentRemove,name='about-my-self-comment-remove'),
    path('download-resume/',myResumeDownloadView,name='download-resume'),
    path('my-projects/',myProjectsView,name='my-projects'),
    path('my-projects-bot/',myPojectsViewBot,name='my-projects-bot'),
    path('contact-me/',contactPage,name='contact-me'),
    
]

