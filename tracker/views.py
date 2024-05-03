from django.shortcuts import render
from django.views import generic
from .models import Team, Game, Player, Match

def index(request):
    #IOU needed homepage info
    return render(request, "index.html")

class TeamListView(generic.ListView):
    model = Team
    paginate_by = 10

class TeamDetailView(generic.DetailView):
    model = Team

class PlayerListView(generic.ListView):
    model = Player
    paginate_by = 10

class MatchListView(generic.ListView):
    model = Match
    paginate_by = 10

class MatchDetailView(generic.DetailView):
    model = Match