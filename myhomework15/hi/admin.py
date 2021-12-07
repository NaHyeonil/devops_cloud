from django.contrib import admin
from hi.models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
	pass