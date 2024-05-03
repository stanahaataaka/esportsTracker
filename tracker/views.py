from django.shortcuts import render
from django.views import generic
from .models import Team, Game, Player
<<<<<<< HEAD
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.urls import reverse
=======
from django.contrib.auth.decorators import login_required
>>>>>>> 7b92129f49bb8b00167465e96cc9e1c00ef79506

def index(request):
    #IOU needed homepage info
    return render(request, "index.html")

class TeamListView(generic.ListView):
    model = Team
    paginate_by = 10

class TeamDetailView(generic.DetailView):
    model = Team

<<<<<<< HEAD
=======
@login_required
>>>>>>> 7b92129f49bb8b00167465e96cc9e1c00ef79506
def admin_tracker(request):
    return render(request, "admin_tracker.html")

class PlayerListView(generic.ListView):
    model = Player
    paginate_by = 10
<<<<<<< HEAD

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
=======
>>>>>>> 7b92129f49bb8b00167465e96cc9e1c00ef79506
