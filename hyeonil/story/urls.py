from django.urls import path

from . import views

app_name = "story"

urlpatterns = [
    path("", views.daily_list, name="daily_list"),
    path("<int:pk>/", views.daily_detail, name="daily_detail"),
]