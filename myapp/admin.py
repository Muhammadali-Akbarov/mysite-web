from django.contrib import admin

from .models import(
    Comments,
    MyResume,
    MyYouTube,
    ProjectCategory,
    MyProjects,
    MyBots,
    GetInTouch
    )

admin.site.register([Comments,MyProjects,MyResume,ProjectCategory,MyBots,GetInTouch,MyYouTube])

