from django.contrib import admin

from higame.models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass