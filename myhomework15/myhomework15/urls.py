from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from hi.views import game_list, game_detail, game_new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hi/',game_list),
    path('hi/<int:pk>/', game_detail),
    path('hi/new', game_new),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]