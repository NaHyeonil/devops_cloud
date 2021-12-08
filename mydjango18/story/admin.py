from django.contrib import admin

from story.models import Storyboard, Comment, Tag


@admin.register(Storyboard)
class StoryboardAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class StoryboardAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class StoryboardAdmin(admin.ModelAdmin):
    pass
