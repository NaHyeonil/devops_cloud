from django.contrib import admin

from story.models import Daily, Comment, Tag


@admin.register(Daily)
class DailyAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class DailyAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class DailyAdmin(admin.ModelAdmin):
    pass