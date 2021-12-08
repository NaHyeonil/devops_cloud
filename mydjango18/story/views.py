from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from story.models import Storyboard


def storyboard_list(request: HttpRequest) -> HttpResponse:
    qs = Storyboard.objects.all()

    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(title__icontains=query)

    return render(request, "story/storyboard_list.html", {
        "storyboard_list": qs
    })


def storyboard_detail(request: HttpRequest, pk=int) -> HttpResponse:
    storyboard = Storyboard.objects.get(pk=pk)
    comment_list = storyboard.comment_set.all()
    tag_list = storyboard.tag_set.all()
    return render(request, "story/storyboard_detail.html", {
        "storyboard": storyboard,
        "comment_list": comment_list,
        "tag_list": tag_list,
    })
