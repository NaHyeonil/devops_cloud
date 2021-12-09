from django.urls import path
from diary import views


app_name = "diary"


urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
    path("new/", views.post_new, name="post_new"),
    path("tags/<str:tag_name>/", views.tag_detail, name="tag_detail"),
]