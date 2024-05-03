
from django.shortcuts import render
from django.views import generic
from .models import Team, Game, Player, Match
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    #IOU needed homepage info
    return render(request, "index.html")

class MatchListView(generic.ListView):
    model = Match
    paginate_by = 10

class MatchDetailView(generic.DetailView):
    model = Match

class MatchCreate(PermissionRequiredMixin, CreateView):
    model = Match
    fields = '__all__'
    permission_required = 'tracker.add_match'

class MatchUpdate(PermissionRequiredMixin, UpdateView):
    model = Match
    fields = '__all__'
    permission_required = 'tracker.change_match'

class MatchDelete(PermissionRequiredMixin, DeleteView):
    model = Match
    success_url = reverse_lazy('matches')
    permission_required = 'tracker.delete_match'

    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        except Exception as e:
            return HttpResponseRedirect(
                reverse("match-delete", kwargs={"pk": self.object.pk})
            )

class TeamListView(generic.ListView):
    model = Team
    paginate_by = 10

class TeamDetailView(generic.DetailView):
    model = Team

class TeamCreate(PermissionRequiredMixin, CreateView):
    model = Team
    fields = ['teamName', 'game']
    permission_required = 'tracker.add_team'

class TeamUpdate(PermissionRequiredMixin, UpdateView):
    model = Team
    fields = '__all__'
    permission_required = 'tracker.change_team'

class TeamDelete(PermissionRequiredMixin, DeleteView):
    model = Team
    success_url = reverse_lazy('teams')
    permission_required = 'tracker.delete_team'

    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        except Exception as e:
            return HttpResponseRedirect(
                reverse("team-delete", kwargs={"pk": self.object.pk})
            )

class PlayerListView(generic.ListView):
    model = Player
    paginate_by = 10

class PlayerDetailView(generic.DetailView):
    model = Player

class PlayerCreate(PermissionRequiredMixin, CreateView):
    model = Player
    fields = ['username', 'name', 'team', 'age']
    permission_required = 'tracker.add_player'

class PlayerUpdate(PermissionRequiredMixin, UpdateView):
    model = Player
    fields = '__all__'
    permission_required = 'tracker.change_player'

class PlayerDelete(PermissionRequiredMixin, DeleteView):
    model = Player
    success_url = reverse_lazy('players')
    permission_required = 'tracker.delete_player'

    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        except Exception as e:
            return HttpResponseRedirect(
                reverse("player-delete", kwargs={"pk": self.object.pk})
            )

@login_required
class GameListView(generic.ListView):
    model = Game

class GameListView(generic.ListView):
    model = Game

class GameDetailView(generic.DetailView):
    model = Game

class GameCreate(PermissionRequiredMixin, CreateView):
    model = Game
    fields = '__all__'
    permission_required = 'tracker.add_game'

class GameUpdate(PermissionRequiredMixin, UpdateView):
    model = Game
    fields = '__all__'
    permission_required = 'tracker.change_game'

class GameDelete(PermissionRequiredMixin, DeleteView):
    
    model = Game
    success_url = reverse_lazy('admin_tracker')
    permission_required = 'tracker.delete_game'

    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        except Exception as e:
            return HttpResponseRedirect(
                reverse("game-delete", kwargs={"pk": self.object.pk})
            )

class PlayerDetailView(generic.DetailView):
    model = Player