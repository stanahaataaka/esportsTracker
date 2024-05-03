from django.shortcuts import render
from django.views import generic
from .models import Team, Game, Player
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.urls import reverse

def index(request):
    #IOU needed homepage info
    return render(request, "index.html")

class TeamListView(generic.ListView):
    model = Team
    paginate_by = 10

class TeamDetailView(generic.DetailView):
    model = Team

def admin_tracker(request):
    return render(request, "admin_tracker.html")

class PlayerListView(generic.ListView):
    model = Player
    paginate_by = 10

class TeamCreate(PermissionRequiredMixin, CreateView):
    model = Team
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    initial = {'date_of_death': '11/11/2023'}
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
