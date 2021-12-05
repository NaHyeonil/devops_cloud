from django.contrib import admin
from hi.models import Game

class GameAdmin(admin.ModelAdmin):
		list_display = ["id", "gamename", "gamedate", "gold"]
		list_display_links = ["gamename"]


admin.site.register(Game, GameAdmin)