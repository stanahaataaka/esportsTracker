from django.contrib import admin
from .models import Team, Game, Player, Opponent, Match, MatchPlayers

# Register your models here.
admin.site.register(Team)
admin.site.register(Game)
admin.site.register(Player)
admin.site.register(Opponent)
admin.site.register(Match)
admin.site.register(MatchPlayers)