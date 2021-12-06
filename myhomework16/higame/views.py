from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView

from higame.forms import GameForm
from higame.models import Game


def game_list(request: HttpRequest) -> HttpResponse:
    qs = Game.objects.all()

    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(gamename__icontains=query)

    context_data = {
        "game_list": qs,
    }
    return render(request, "higame/game_list.html", context_data)

def game_detail(request: HttpRequest, pk:int) ->HttpResponse:
    game = Game.objects.get(pk=pk)
    context_data = {
        "game": game,
    }
    return render(request, "higame/game_detail.html", context_data)


game_new = CreateView.as_view(
    model=Game,
    form_class=GameForm,
    success_url="/higame/",
)