from django.contrib import admin
from .models import Team, Game, Player

# Register your models here.
admin.site.register(Team)
admin.site.register(Game)
admin.site.register(Player)