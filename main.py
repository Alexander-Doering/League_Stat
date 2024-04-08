## TO-DO BLOCK ##
#TODO: Use API Calls 
#TODO: Make Matchfinder by User-iD (User -> PUUID -> Matches)
#TODO: Option to select Tournament or other Queue Type
#TODO: Update current version to use scrim results (timeline isn't availible here)
#TODO: Add Option to add team-lists to match Flex-Queue 
#TODO: Database connectivity
#TODO: Reporting
import json
import os
from shutil import move 
import csv
import math
# V A R I A B L E S
id_array=[]
topdata=[]
jngdata=[]
middata=[]
adcdata=[]
supdata=[]
gamedata=[]
importdirectory = os.path.join(os.getcwd(),"Import")
exportdirectory = os.path.join(os.getcwd(),"Done")
datadirectory = os.path.join(os.getcwd(),"Export")
filterName = "AG Emperor" #TODO: Swap to PUUID
## F U N C T I O N S
def DataReader():
    for filename in os.listdir(importdirectory):
       with open(os.path.join(importdirectory, filename), 'r') as f:
            # Open File 
            text = f.read()
            data=json.loads(text)
            # Find out game Data
            gameid=data['matchId']
            id_array.append(gameid)
            patch=data['gameVersion']
            time=float(data['gameDuration']/(1000*60))
            win=data['participants'][0]['win']
            # Gamedata Array
            row=[gameid,patch,time]
            gamedata.append(row)  
            # Find out which Team own team.
            for x in range(0,10):
                if(data['participants'][x]['name'] == filterName):
                    if x < 5:
                        lower = 0
                        upper = 5
                    else:
                        lower = 5
                        upper = 10
            # Playerdata Array
            for x in range (lower,upper):          #TODO: Variable Range           
                assists=data['participants'][x]['assists']
                baronKills=data['participants'][x]['baronKills']
                kills=data['participants'][x]['championsKilled']            
                dragonKills=data['participants'][x]['dragonKills'] 
                xpm=round(float(int(data['participants'][x]['exp'])/time))
                gpm=round(float(int(data['participants'][x]['goldEarned'])/time))
                item1=data['participants'][x]['item0']
                item2=data['participants'][x]['item1']
                item3=data['participants'][x]['item2']
                item4=data['participants'][x]['item3']
                item5=data['participants'][x]['item4']
                item6=data['participants'][x]['item5']
                item7=data['participants'][x]['item6']
                level=data['participants'][x]['level']
                baronKills=data['participants'][x]['baronKills']
                farm=int(data['participants'][x]['minionsKilled'])+int(data['participants'][x]['neutralMinionsKilled'])
                name=data['participants'][x]['name']
                deaths=data['participants'][x]['numDeaths']
                selfCamps=math.floor(float((int(data['participants'][x]['neutralMinionsKilledYourJungle']))/4))
                enemyCamps=math.floor(float((int(data['participants'][x]['neutralMinionsKilledEnemyJungle']))/4))
                objectiveSteals=data['participants'][x]['objectivesStolen']
                perk1=data['participants'][x]['perk0']
                perk2=data['participants'][x]['perk1']
                perk3=data['participants'][x]['perk2']
                perk4=data['participants'][x]['perk3']
                perk5=data['participants'][x]['perk4']
                perk6=data['participants'][x]['perk5']
                champ=data['participants'][x]['skin']
                statPerk1=data['participants'][x]['statPerk0']
                statPerk2=data['participants'][x]['statPerk1']
                statPerk3=data['participants'][x]['statPerk2']
                if(data['participants'][x]['team']=="100"):
                    team="blue"
                else:
                    team="red"
                teamPosition=data['participants'][x]['teamPosition']
                damageChamps=data['participants'][x]['totalDamageDealtToChampions']
                damageObjective=data['participants'][x]['totalDamageDealtToObjectives']
                shieldingAlly=data['participants'][x]['totalDamageShieldedOnTeammates']
                healingAlly=data['participants'][x]['totalHealOnTeammates']
                turretsKilled=data['participants'][x]['turretsKilled']
                visionWardsBoughtInGame=data['participants'][x]['visionWardsBoughtInGame']
                wardKilled=data['participants'][x]['wardKilled']
                wardPlaced=data['participants'][x]['wardPlaced']
                vsmin=round(float(int(data['participants'][x]['visionScore'])/time),2)
                win=data['participants'][x]['win']
                currow=[gameid,name,champ,teamPosition,win,kills,assists,deaths,gpm,xpm,farm,selfCamps,enemyCamps,objectiveSteals,vsmin,wardKilled,wardPlaced,damageChamps,damageObjective,turretsKilled,dragonKills,baronKills,shieldingAlly,healingAlly,perk1,perk2,perk3,perk4,perk5,perk6,statPerk1,statPerk2,statPerk3,item1,item2,item3,item4,item5,item6,item7]
                if teamPosition == "TOP":
                    topdata.append(currow)
                if teamPosition == "JUNGLE":
                    jngdata.append(currow)
                if teamPosition == "MIDDLE":
                    middata.append(currow)
                if teamPosition == "BOTTOM":
                    adcdata.append(currow)
                if teamPosition == "UTILITY":
                    supdata.append(currow)
#CSV Data Writer
def CsvDataWriter(name, data):
    with open(os.path.join(datadirectory, name), 'w') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)
#DB Writer

## S C R I P T
DataReader()
CsvDataWriter("top", topdata)
CsvDataWriter("jng", jngdata)
CsvDataWriter("mid", middata)
CsvDataWriter("bot", adcdata)
CsvDataWriter("sup", supdata)
CsvDataWriter("game", gamedata)
