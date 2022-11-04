import random


class T2Cup:
    allTeam = []
    def entry_team(self,teamObj):
        self.allTeam.append(teamObj)

class Team(T2Cup):
    def __init__(self,name):
        self.teamNmme = name
        self.playerListOfObject = []
        super().entry_team(self)

    def entry_player(self,player): #player type player Object
        self.playerListOfObject.append(player)
    def __repr__(self):
        return f'From Object.Team Name:{self.teamName}'

class Player:
    def __init__(self,name,teamObj):
        self.playername = name
        self.strikerate = 0.0
        self.runrate  = 0
        self.ballUsed = 0
        self.fours = 0
        self.sixes = 0
        self.runbowl = 0
        self.wickettaken = 0
        self.ballsboeler = 0
        teamObj.playerListOfObject.append(self)

    def __repr__(self):
        return f'From player object name:{self.playername}'

class Innings:
    def __init__(self,team1,team2,battingTeam,bollingTeam):
        self.teamoneobj = team1
        self.teamtwoobj = team2
        self.battingteam = battingTeam
        self.bollingteam = bollingTeam
        self.totalrun = 0
        self.totalover = 0
        self.currentball = 0
        self.currentbattinglist = [battingTeam.playerListOfObject[0],battingTeam.playersListOfObject[1]]
        self.striker = battingTeam.playersListOfObject[0]
        self.currentbowler=None
        self.currentoverstatus = []

    def show_score_board(self):
        print(f'*{self.currentbatinhlist[0].playername}-{self.currentbattinglist[0].ranBat}({self.currentbattinglist[0].ballused}',end='\t')
        print(f'*{self.currentbatinhlist[1].playername}-{self.currentbattinglist[1].ranBat}({self.currentbattinglist[1].ballused}')
        print(f'{battingteamobj.teamnmae[:3].upper()} | {self.totalrun}-{self.totalwicket}')
        print(f'overs:{self.totalover}.{self.currentball}')
        if self.currentbowler is not None:
            print(f'{self.currentbowler.playername}-{self.currentbowler.runbowl}/{self.currentbowler.wicketstaken}')

    def set_bowler(self,bowlerobj):
        self.currentbowler=bowlerobj
    def bowl(self,status):
        self.totalrun+= status
        self.striker.runbat += status
        self.striker.ballUsed += 1
        self.currentball+=1

        
cup=T2Cup()
bangladesh = Team("Bangladesh")
india = Team("India")
tamim = Player("Tamim Iqbal",bangladesh)
shakib = Player("Shakib Al Hasan",bangladesh)
mustafiz = Player("Mustafizur Rahman",bangladesh)
kohli = Player("Virat Kohli",india)
rohit = Player("Rohit Sharma",india)
bumra = Player("Bumra",india)

while True:
    print("Select team to be played")
    for i,val in enumerate(cup.allTeam):
        print(f'{i+1}.{val.teamNmme}')

        teamoneindex,teamtwoindex = map(int,input("Enter two team indexes: ").split(" "))
        teamoneindex -= 1
        teamtwoindex -= 1
        teamoneobj = cup.allTeam[teamoneindex]
        teamtwoobj = cup.allTeam[teamtwoindex]
        tosswin = random.choice([teamoneindex,teamtwoindex])
        print(f'{cup.allTeam[tosswin].teamname} win toss')

        if tosswin==teamoneindex:
            toselose = teamtwoindex

        else:
            toselose = teamoneindex

        rand = random.choice([0,1])

        if rand == 0:
            #Winner Team Choose Bowling
            print(f'{cup.allteams[tosswin].teamname} chose bowling')
            battingteamobj = cup.allTeam[toselose]
            bowlingteamobj = cup.allTeam[tosswin]
        
        else:
        ## Winner Team Choose Batting
            print(f'{cup.allteams[tosswin].teamname} chose batting')
            battingteamobj = cup.allTeam[toselose]
            bowlingteamobj = cup.allTeam[tosswin]

        firstInnings = Innings(teamoneobj,teamtwoobj,battingteamobj,bowlingteamobj)
        firstInnings.show_score_board()
        print('choise bowler: ')
        for i,val in enumerate(bowlingteamobj.playersListOfObject):
            print(f'{i+1}.{val.playerName}')
        bowlerindex = int(input("Enter bowler index: "))
        bowlerindex -= 1
        bowlerobj = bowlingteamobj.playersListOfObject[bowlerindex]
        firstInnings.set_bowler(bowlerobj)
        print('\n')
        firstInnings.bowl(6)
        firstInnings.show_score_board()
        break


        
    