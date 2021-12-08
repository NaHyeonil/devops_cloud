from django.urls import path

from . import views


app_name = "story"
urlpatterns = [
    path("", views.storyboard_list, name="storyboard_list"),
    path("<int:pk>/", views.storyboard_detail, name="storyboard_detail"),
]