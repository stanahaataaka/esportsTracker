from django.contrib import admin
from .models import Team, Game, Player, Match
# Register your models here.
admin.site.register(Team)
admin.site.register(Game)
admin.site.register(Player)
admin.site.register(Match)
