from django.contrib import admin
from game.models import Gamepost


# class GamepostAdmin(admin.ModelAdmin):
#     list_display = ['gamename', 'gamedate', 'gold']

admin.site.register(Gamepost)

