from django.db import models

#Game Model: holds information for whaat games are avalible for any given season.
#Variables for the leagueFormat and leagueStructure, for more info reguarding this section, refer to section 2: https://www.mnvl.org/spring-rules .

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
    gameName = models.CharField(max_length=25, unique=True)
    #The team size feild holds the number of players allowed on 1 team for the defined game.
    teamSize = models.IntegerField()
    #The leagueFormat and leagueStructure feilds pull from the choices defined in the leagueFormatChoices and leagueStructureChoices variables.
    leagueFormat = models.CharField(choices=leagueFormatChoices, default=roundRobin)
    leagueStructure = models.CharField(choices=leagueStructureChoices, default=jv)

    #ToString:
    def __str__(self):
        return self.gameName
    
#Team Model:
class Team(models.Model):
    teamName = models.CharField(max_length=25, unique=True)
    playerCount = models.IntegerField()
    game = models.ManyToManyField(Game)
    #players = models.ManyToManyField(Player, max_length=playerCount)

    #ToString:
    def __str__(self):
        return self.teamName
    

