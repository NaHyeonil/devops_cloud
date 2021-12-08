from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from story.models import Daily


def daily_list(request: HttpRequest) -> HttpResponse:
    qs = Daily.objects.all()

    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(title__icontains=query)

    return render(request, "story/daily_list.html", {
        "daily_list": qs
    })


def daily_detail(request: HttpRequest, pk= int) -> HttpResponse:
    daily = Daily.objects.get(pk=pk)
    comment_list = daily.comment_set.all()
    tag_list = daily.tag_set.all()
    return render(request, "story/daily_detail.html", {
        "daily": daily,
        "comment_list": comment_list,
        "tag_list": tag_list
    })