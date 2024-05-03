
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

@login_required
def admin_tracker(request):
    return render(request, "admin_tracker.html")

class TeamListView(generic.ListView):
    model = Team
    paginate_by = 10

class TeamDetailView(generic.DetailView):
    model = Team

class PlayerListView(generic.ListView):
    model = Player
    paginate_by = 10

class MatchDetailView(generic.DetailView):
    model = Match

class MatchListView(generic.ListView):
    model = Match
    paginate_by = 10

class PlayerDetailView(generic.DetailView):
    model = Player

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

class PlayerCreate(PermissionRequiredMixin, CreateView):
    model = Player
    fields = ['username', 'name', 'team', 'age', 'kills', 'deaths', 'assists', 'KDA', 'datePlayed']
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
