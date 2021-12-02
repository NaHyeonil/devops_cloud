from django.contrib import admin
from catube.models import Video

class VideoAdimin(admin.ModelAdmin):
    pass

admin.site.register(Video, VideoAdimin)