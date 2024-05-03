from django.db import models

#Game Model: holds information for whaat games are avalible for any given season.
#Variables for the leagueFormat, leagueStructure, and gameName: for more info reguarding this section, refer to section 2: https://www.mnvl.org/spring-rules .

#Game Name:
#Variables:
rocketLeague = "Rocket League"
minecraft = "Minecraft"
valorant = "Valorant"
#Choice Variable:
gameNameChoices = (
    (rocketLeague, "Rocket League"),
    (minecraft, "Minecraft"),
    (valorant, "Valorant"),
)

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
    gameID = models.IntegerField(unique=True,primary_key=True,auto_created=True)
    gameName = models.CharField(choices=gameNameChoices, default=minecraft, max_length=25)
    #The team size feild holds the number of players allowed on 1 team for the defined game.
    teamSize = models.IntegerField(default=0)
    #The leagueFormat and leagueStructure feilds pull from the choices defined in the leagueFormatChoices and leagueStructureChoices variables.
    leagueFormat = models.CharField(choices=leagueFormatChoices, default=roundRobin, max_length=25)
    leagueStructure = models.CharField(choices=leagueStructureChoices, default=jv, max_length=25)

    #ToString:
    def __str__(self):
        return self.gameName
    
# Player Model:
class Player(models.Model):
    playerID = models.IntegerField(unique=True,primary_key=True,auto_created=True)
    team = models.ForeignKey('Team', on_delete=models.RESTRICT, null=True)
    name = models.CharField("Username", max_length=20)
    username = models.CharField("Username", max_length=10)
    age = models.IntegerField("Age")
    kills = models.IntegerField("Kills")
    deaths = models.IntegerField("Deaths")
    assists = models.IntegerField("Assists")
    KDA = models.CharField('KDA', max_length=11)
    datePlayed = models.DateField(("Date Played"), auto_now=False, auto_now_add=False)   

    #ToString:
    def __str__(self):
        return self.username
    
#Team Model:
class Team(models.Model):
    teamName = models.CharField(max_length=25, unique=True, primary_key=True)
    game = models.ForeignKey('Game', on_delete=models.RESTRICT, null=True)

    #ToString:
    def __str__(self):
        return self.teamName
    
#Match Models
class Opponent(models.Model):
    opponentID = models.AutoField(primary_key=True)
    opponentName = models.CharField(max_length=40)
    opponentAcronym = models.CharField(max_length=5)

    def __str__(self):
        return self.opponentName

#Game Name:
#Variables:
live = "Live"
final = "Final"
upcomming = "Upcomming"
#Choice Variable:
matchStautsChoices = (
    (live, "Live"),
    (final, "Final"),
    (upcomming, "Upcomming"),
)
class Match(models.Model):
    matchID = models.AutoField(primary_key=True)
    date = models.DateField()
    gameName = models.CharField(choices=gameNameChoices, default=minecraft, max_length=25)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    homeScore = models.IntegerField(null=True)
    opponentScore = models.IntegerField(null=True)
    opponentID = models.ForeignKey(Opponent, on_delete=models.SET_NULL, null=True)
    status = models.CharField(choices=matchStautsChoices, default=upcomming, max_length=10)

