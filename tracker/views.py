from django.shortcuts import render
from django.views import generic
from .models import Team, Game, Player

def index(request):
    #IOU needed homepage info
    return render(request, "index.html")

class TeamListView(generic.ListView):
    model = Team
    paginate_by = 10

class TeamDetailView(generic.DetailView):
    model = Team

<<<<<<< HEAD
def admin_tracker(request):
    return render(request, "admin_tracker.html")
=======
class PlayerListView(generic.ListView):
    model = Player
    paginate_by = 10
>>>>>>> main
