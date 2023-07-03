import json
import os
from shutil import move 
import csv
#import pyodbc 

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
for filename in os.listdir(importdirectory):
   with open(os.path.join(importdirectory, filename), 'r') as f:
        # Open File 
        text = f.read()
        data=json.loads(text)
        # Find out game Data
        team=data['participants'][0]['TEAM']
        gameid=data['matchId']
        id_array.append(gameid)
        time=float(data['gameDuration']/(1000*60))
        win=data['participants'][0]['win']
        totalkills=int(data['participants'][0]['championsKilled'])+int(data['participants'][1]['championsKilled'])+int(data['participants'][2]['championsKilled'])+int(data['participants'][3]['championsKilled'])+int(data['participants'][4]['championsKilled'])
        totalassists=int(data['participants'][0]['assists'])+int(data['participants'][1]['assists'])+int(data['participants'][2]['assists'])+int(data['participants'][3]['assists'])+int(data['participants'][4]['assists'])
        totaldeaths=int(data['participants'][0]['numDeaths'])+int(data['participants'][1]['numDeaths'])+int(data['participants'][2]['numDeaths'])+int(data['participants'][3]['numDeaths'])+int(data['participants'][4]['numDeaths'])
        if totalkills+totalassists == 0 or totaldeaths == 0:
                team_kda=0
        else:
            team_kda=(totalassists+totalkills)/totaldeaths
        if (totalkills == 0) or (totalassists == 0):
            assists_over_kills=0
        else:
                assists_over_kills=totalassists/totalkills
        total_dmg=int(data['participants'][0]['totalDamageDealtToChampions'])+int(data['participants'][1]['totalDamageDealtToChampions'])+int(data['participants'][2]['totalDamageDealtToChampions'])+int(data['participants'][3]['totalDamageDealtToChampions'])+int(data['participants'][4]['totalDamageDealtToChampions'])
        # Gamedata Writer
        row=[gameid,time,win,totalkills,totalassists,totaldeaths,assists_over_kills,team_kda,total_dmg]
        gamedata.append(row)
        for x in range (0,5):                     
            name=data['participants'][x]['name']
            champ=data['participants'][x]['skin']
            kills=data['participants'][x]['championsKilled']
            assists=data['participants'][x]['assists']
            deaths=data['participants'][x]['numDeaths']
            vsmin=float(data['participants'][x]['visionScore']/time)
            farm=int(data['participants'][x]['minionsKilled'])+int(data['participants'][x]['neutralMinionsKilled'])
            gpm=float(data['participants'][x]['goldEarned']/time)
            if totalkills == 0:
                killpart=0
            else:
                killpart=float(int(data['participants'][x]['championsKilled'])/totalkills)
            dmgdealtpercent=float(int(data['participants'][x]['totalDamageDealtToChampions'])/total_dmg)
            currow=[gameid,name,champ,kills,assists,deaths,vsmin,farm,gpm,killpart,dmgdealtpercent]
            if x == 0:
                topdata.append(currow)
            if x == 1:
                jngdata.append(currow)
            if x == 2:
                middata.append(currow)
            if x == 3:
                adcdata.append(currow)
            if x == 4:
                supdata.append(currow)
                   
            
# Lane Data Writer
with open(os.path.join(datadirectory,"top"), 'w') as f:
    writer = csv.writer(f) 
    for row in topdata:
        writer.writerow(row)
with open(os.path.join(datadirectory,"jng"), 'w') as f:
    writer = csv.writer(f) 
    for row in jngdata:
        writer.writerow(row)
with open(os.path.join(datadirectory,"mid"), 'w') as f:
    writer = csv.writer(f) 
    for row in middata:
        writer.writerow(row)
with open(os.path.join(datadirectory,"adc"), 'w') as f:
    writer = csv.writer(f) 
    for row in adcdata:
        writer.writerow(row)
with open(os.path.join(datadirectory,"sup"), 'w') as f:
    writer = csv.writer(f) 
    for row in supdata:
        writer.writerow(row)
with open(os.path.join(datadirectory,"game"), 'w') as f:
    writer = csv.writer(f) 
    for row in gamedata:
        writer.writerow(row)            

print(id_array)


#for id in id_array:
#    ExportFile=os.path.abspath(os.path.join(exportdirectory,str(id)))
#    ImportFile=os.path.abspath(os.path.join(importdirectory,str(id))) 
#   move(ImportFile,ExportFile)
    
