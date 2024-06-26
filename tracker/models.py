from django.db import models
from django.urls import reverse

#Game Model: holds information for whaat games are avalible for any given season.
#Variables for the leagueFormat and leagueStructure: for more info reguarding this section, refer to section 2: https://www.mnvl.org/spring-rules .

#League Format:
#Variables:
swiss = "Swiss"
roundRobin = "Round Robin"
doubleRoundRobin = "Double Round Robin"
#Choice Variable:
leagueFormatChoices = (
    (swiss, "Swiss"),
    (roundRobin, "Round Robin"),
    (doubleRoundRobin, "Double Round Robin"),
)

#League Structure:
#Variables:
open = "Open"
varsity = "Varsity"
jv = "Junior Varsity"
club = "Club"
#Choice Variable:
leagueStructureChoices = (
    (open, "Open"),
    (varsity,"Varsity"),
    (jv, "Junior Varsity"),
    (club, "Club"),
)
#Game Model:
class Game(models.Model):
    gameName = models.CharField(max_length=30)
    #The team size feild holds the number of players allowed on 1 team for the defined game.
    teamSize = models.IntegerField(default=0)
    #The leagueFormat and leagueStructure feilds pull from the choices defined in the leagueFormatChoices and leagueStructureChoices variables.
    leagueFormat = models.CharField(choices=leagueFormatChoices, default=roundRobin, max_length=25)
    leagueStructure = models.CharField(choices=leagueStructureChoices, default=jv, max_length=25)

    def get_absolute_url(self):
        return reverse('game-detail', args=[str(self.id)])

    #ToString:
    def __str__(self):
        return self.gameName
    
# Player Model:
class Player(models.Model):
    username = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    team = models.ForeignKey('Team', on_delete=models.RESTRICT, null=True)
    age = models.IntegerField()
    kills = models.IntegerField(default=0)
    deaths = models.IntegerField(null=True, default=0)
    assists = models.IntegerField(null=True, default=0)
    KDA = models.CharField(max_length=11,null=True, default="0/0/0")
    #datePlayed = models.DateField(("Date Played"), auto_now=False, auto_now_add=False,null=True)   

    def get_absolute_url(self):
        return reverse('player-detail', args=[str(self.id)])

    #ToString:
    def __str__(self):
        return self.username
    
#Team Model:
class Team(models.Model):
    teamName = models.CharField(max_length=25, unique=True)
    game = models.ForeignKey('Game', on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse('team-detail', args=[str(self.id)])

    #ToString:
    def __str__(self):
        return self.teamName

#Game Name:
#Variables:
completed = "Completed"
upcoming = "Upcoming"
#Choice Variable:
matchStautsChoices = (
    (completed, "Completed"),
    (upcoming, "Upcoming"),
)
class Match(models.Model):
    #matchID = models.AutoField(primary_key=True)
    date = models.DateField()
    team = models.ForeignKey('Team', on_delete=models.RESTRICT, null=True)
    players = models.ManyToManyField("Player")
    homeScore = models.IntegerField(null=True)
    opponentScore = models.IntegerField(null=True)
    opponentAcronym = models.CharField(max_length=5,default="null")
    status = models.CharField(choices=matchStautsChoices, default=completed, max_length=10)

    def get_absolute_url(self):
        return reverse('match-detail', args=[str(self.id)])

    def __str__(self):
        return self.opponentAcronym
    
        
