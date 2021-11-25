from os import listdir
import json
import os
from discord.ext import commands, tasks
import discord.ext

from os.path import isfile, join
client = discord.Client()
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await chatbox.start()

@tasks.loop(seconds=300)
async def chatbox():
    channel = client.get_channel(912697343864877076)
    
    mypath=r"/home/kf2/KFGame/Logs/"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for log in onlyfiles:
        if log[:6]!="Launch"and log[:2]!="no"and log[:3]!="KF2":
            data=json.load(open(log))
            os.remove(log)
        
            

            mapName=data['mapName']
            spawnCycle=data['spawnCycle']
            maxMonsters=data['maxMonsters']
            cohortSize=data['cohortSize']
            zedsType=data['zedsType']
            stats=data['stats']
            KFMapName=f"KF-{mapName}"
            print(KFMapName)
            KFMapList=["KF-Airship","KF-AshwoodAsylum","KF-Biolapse","KF-BioticsLab","KF-BlackForest","KF-BurningParis",
                       "KF-Catacombs","KF-ContainmentStation","KF-Desolation","KF-DieSector",
                       "KF-Dystopia2029","KF-Elysium","KF-EvacuationPoint","KF-Farmhouse","KF-HellmarkStation","KF-HostileGrounds",
                       "KF-InfernalRealm","KF-KrampusLair","KF-Lockdown","KF-MonsterBall","KF-Moonbase","KF-Netherhold","KF-Nightmare",
                       "KF-Nuked","KF-Outpost","KF-PowerCore_Holdout","KF-Prison","KF-Sanitarium","KF-SantasWorkshop","KF-ShoppingSpree",
                       "KF-Spillway","KF-SteamFortress","KF-TheDescent","KF-TragicKingdom","KF-VolterManor","KF-ZedLanding"]
            filename=""

            if KFMapName in KFMapList:
                    filename=f"http://45.76.163.207:8080/images/maps/{KFMapName}.jpg"
            elif KFMapName not in KFMapList:
                    filename="http://45.76.163.207:8080/images/maps/noimage.png"
            print(filename)
            embed2 = discord.Embed(
                title='CDSG STATS',
                description=f'{mapName} {spawnCycle} MaxMonsters:{maxMonsters} CohortSize:{cohortSize} ZedType:{zedsType}'
                ,colour=discord.Colour.red()
            )
            embed2.set_footer(text='WIN')
            embed2.set_image(url=f"{filename}")
            embed2.set_author(name='Made by Patrick')
            Gunslinger="<:GUNSLINGER:913020399837663262>"
            Commando="<:COMMANDO:913020392694763570>"
            Medic="<:MEDIC:913020406816981032>"
            Sharpshooter="<:SHARPSHOOTER:913020412319916043>"
            Support="<:SUPPORT:913020421031473202>"
            Swat="<:SWAT:913020428090474546>"
            for player in stats:
                if player['perk']=="Gunslinger":
                    embed2.add_field(name=f"{player['alias']} <:GUNSLINGER:912995755088810024> ",value=f"DamageDealt:{player['damageDealt']} LargeKills:{player['largeKills']} FP/SC/HU:{player['fleshpounds']}/{player['scrakes']}/{player['husks']} HealsGiven:{player['healsGiven']} Headshots:{player['headshots']} HeadshotAccuracy:{player['headshotAccuracy']} Accuracy:{player['accuracy']}",inline=False)
                elif player['perk']=="Commando":
                    embed2.add_field(name=f"{player['alias']} <:COMMANDO:912995755139141652> ",
                                     value=f"DamageDealt:{player['damageDealt']} LargeKills:{player['largeKills']} FP/SC/HU:{player['fleshpounds']}/{player['scrakes']}/{player['husks']} HealsGiven:{player['healsGiven']} Headshots:{player['headshots']} HeadshotAccuracy:{player['headshotAccuracy']} Accuracy:{player['accuracy']}",
                                     inline=False)
                elif player['perk'] == "Field Medic":
                    embed2.add_field(name=f"{player['alias']} <:MEDIC:912995755365629992> ",
                                     value=f"DamageDealt:{player['damageDealt']} LargeKills:{player['largeKills']} FP/SC/HU:{player['fleshpounds']}/{player['scrakes']}/{player['husks']} HealsGiven:{player['healsGiven']} Headshots:{player['headshots']} HeadshotAccuracy:{player['headshotAccuracy']} Accuracy:{player['accuracy']}",
                                     inline=False)
                elif player['perk'] == "Sharpshooter":
                    embed2.add_field(name=f"{player['alias']} <:SHARPSHOOTER:912995754820378625> ",
                                     value=f"DamageDealt:{player['damageDealt']} LargeKills:{player['largeKills']} FP/SC/HU:{player['fleshpounds']}/{player['scrakes']}/{player['husks']} HealsGiven:{player['healsGiven']} Headshots:{player['headshots']} HeadshotAccuracy:{player['headshotAccuracy']} Accuracy:{player['accuracy']}",
                                     inline=False)
                elif player['perk'] == "Support":
                    embed2.add_field(name=f"{player['alias']} <:SUPPORT:912995755147530260> ",
                                     value=f"DamageDealt:{player['damageDealt']} LargeKills:{player['largeKills']} FP/SC/HU:{player['fleshpounds']}/{player['scrakes']}/{player['husks']} HealsGiven:{player['healsGiven']} Headshots:{player['headshots']} HeadshotAccuracy:{player['headshotAccuracy']} Accuracy:{player['accuracy']}",
                                     inline=False)
                elif player['perk'] == "Swat":
                    embed2.add_field(name=f"{player['alias']} <:SWAT:912995754874925087> ",
                                     value=f"DamageDealt:{player['damageDealt']} LargeKills:{player['largeKills']} FP/SC/HU:{player['fleshpounds']}/{player['scrakes']}/{player['husks']} HealsGiven:{player['healsGiven']} Headshots:{player['headshots']} HeadshotAccuracy:{player['headshotAccuracy']} Accuracy:{player['accuracy']}",
                                     inline=False)



            await channel.send(embed=embed2)




client.run('')
