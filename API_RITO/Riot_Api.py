from riotwatcher import LolWatcher, ApiError
import string
# import configparser
# import requests

api_key = 'RGAPI-b21e4b07-c52f-4f8b-9bff-8510be7ba2b6'
watcher = LolWatcher(api_key)
my_region = 'euw1'
GameVersion = "13.6.1"
headers = {
    "Origin": "https://developer.riotgames.com",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Riot-Token": api_key,
    "Accept-Language": "en-us",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15"
}


# me = watcher.summoner.by_name('euw1', 'StraightAphelios')
# print(me)
# "Impossible de trouver l'ID de '" + name + "' dans la region '" + region+"'"
# z = watcher._champion_mastery.by_summoner_by_champion('euw1',me["id"],'234')
#----------------------------------------------------------------------------------------------------------------
#Renvoie un lien vers l'icone de l'utilisateur
def GetProfileIconUrlByIdAndRegion(summoner_id, region):
    me = watcher.summoner.by_id(region, summoner_id)
    link = "https://ddragon.leagueoflegends.com/cdn/"+GameVersion+"/img/profileicon/"+str(me["profileIconId"])+".png"
    print(link)
    return link
#----------------------------------------------------------------------------------------------------------------
#Renvoie un lien vers l'icone de l'utilisateur
def GetProfileIconUrlByNameAndRegion(summoner_name, region):
    me = watcher.summoner.by_name(region, summoner_name)
    link = "https://ddragon.leagueoflegends.com/cdn/"+GameVersion+"/img/profileicon/"+str(me["profileIconId"])+".png"
    print(link)
    return link
#----------------------------------------------------------------------------------------------------------------
#Certain champin aillant des nom compliqué, nous modifions les informations pour quelle n'entre pas en conflit avec l'api
def RegisterGoodName(champion_name):
    champion_name = string.capwords(champion_name)
    #------------
    if champion_name == "Reksai" or champion_name == "Rek'sai" or champion_name == "Rek Sai":
        champion_name = "Rek'Sai"
    #------------
    if champion_name == "Kogmaw" or champion_name == "Kog'maw" or champion_name == "Kog Maw":
        champion_name = "Kog'Maw"
    #------------
    if champion_name == "Velkoz" or champion_name == "Vel'koz" or champion_name == "Vel Koz":
        champion_name = "Vel'Koz"
    #------------
    if champion_name == "Dr.mundo":
        champion_name = "Dr. Mundo"
    #------------
    if champion_name == "Kaisa" or champion_name == "Kai'sa" or champion_name == "Kai Sa":
        champion_name = "Kai'Sa"
    #------------
    if champion_name == "Chogath" or champion_name == "Cho'gath" or champion_name == "Cho Gath":
        champion_name = "Cho'Gath"
    #------------
    if champion_name == "Belveth" or champion_name == "Bel'veth" or champion_name == "Bel Veth":
        champion_name = "Bel'Veth"
    #------------
    if champion_name == "Khazix" or champion_name == "Kha'Zix" or champion_name == "Kha Zix":
        champion_name = "Kha'Zix"
    #------------
    return champion_name
#----------------------------------------------------------------------------------------------------------------
#Permet de trouver l'id d'un joueur en fonction de son nom et de sa région
def GetIDByNameAndRegion(name, region):
    try:
        me = watcher.summoner.by_name(GetRealRegionName(region), name)
        Data = me["id"]
    except:
        Data = None
        pass
    return Data
#----------------------------------------------------------------------------------------------------------------
#Renvoie le rank d'un joueur en fonction de son nom (faible taux de précision)
def GetRankByName(summonner_Name, region, queue_name):
    try:
        me = watcher.league.by_summoner(GetRealRegionName(region), GetIDByNameAndRegion(summonner_Name, GetRealRegionName(region)))
        queue_type = GetQueueIdByName(queue_name)
        Infos = GetRightQueue(me, queue_type)
        if Infos == None:
            Data = "This player is Unranked in " + queue_type
        else :
            Data = Infos
            # Data = "There is the rank of '"+str(Infos['summonerName'])+"' in '"+ queue_type +"' :\n .Rank : "+str(Infos['tier'])+"\n .Division : "+str(Infos['rank'])+"\n .LPs : "+str(Infos['leaguePoints'])+"\n .Wins : "+str(Infos['wins'])+"\n .Losses : "+str(Infos['losses'])+"\n .Winrate : "+str(round(Infos['wins']/(Infos['wins']+Infos['losses'])*100,2))
        return Data
    except:
        Data = "Make sure the region and the summoner name are correct"
        pass
        return Data
#----------------------------------------------------------------------------------------------------------------
#Renvoie le rank d'un joueur en fonction de son id (haut taux de précision)
def GetRankById(summonner_Id, region, queue_name):
    try:
        me = watcher.league.by_summoner
        me = watcher.league.by_summoner(GetRealRegionName(region), summonner_Id)
        queue_type = GetQueueIdByName(queue_name)
        Infos = GetRightQueue(me, queue_type)
        if Infos == None:
            Data = "This player is Unranked in " + queue_type
        else :
            Data = Infos
            # Data = "There is the rank of '"+str(Infos['summonerName'])+"' in '"+ queue_type +"' :\n .Rank : "+str(Infos['tier'])+"\n .Division : "+str(Infos['rank'])+"\n .LPs : "+str(Infos['leaguePoints'])+"\n .Wins : "+str(Infos['wins'])+"\n .Losses : "+str(Infos['losses'])+"\n .Winrate : "+str(round(Infos['wins']/(Infos['wins']+Infos['losses'])*100,2))
        return Data
    except:
        Data = "Make sure the region and the summoner name are correct"
        pass
        return Data
#----------------------------------------------------------------------------------------------------------------
#Permet d'envoyer les données d'un joueur sur un personnage en particulié
def GetMasteryByChampionName(summonner_Name, region,champion_name):
    try:

        me = watcher.champion_mastery.by_summoner(GetRealRegionName(region), GetIDByNameAndRegion(summonner_Name, GetRealRegionName(region)))
        champion_id = GetChampionIdByIsName(champion_name)
        if champion_id != None:
            for Ids in me:
                if int(Ids["championId"]) == int(champion_id):
                    return Ids
            Data = "'"+str(summonner_Name)+"' Have not buyed or never played '"+str(champion_name)
            return Data
        else:
            Data = "Make sure to enter a valid champion name"
            return Data
    except:
        Data = "Make sure the region and the summoner name are correct"
        pass
        return Data
#----------------------------------------------------------------------------------------------------------------
#Les personnages du jeu sont tous référencez grace à un id, gràce à leur nom il nous est possible de transformer cette information
def GetChampionIdByIsName(champion_name):
    champion_name = RegisterGoodName(champion_name)
    latest = watcher.data_dragon.versions_for_region(my_region)['n']['champion']
    k = watcher._data_dragon.champions(latest, True, 'en_US')
    for key in k['data']:
        row = k['data'][key]
        if row['name'] == champion_name: 
            try:
                Data = row['key']
                return Data
            except:
                Data = None
                pass
                return Data
# print(row['name'] + " - " + str(row['key']))
#----------------------------------------------------------------------------------------------------------------
#Chaque queue possède un id précis qui est indenté ici
def GetQueueIdByName(queue_name):
    if queue_name == "soloq": Data = "soloq"
    if queue_name == "solo": Data = "soloq"
    elif queue_name == "flexq": Data = "flexq"
    elif queue_name == "flex": Data = "flexq"
    elif queue_name == "rankedsoloq": Data = "soloq"
    elif queue_name == "rankedflexq": Data = "flexq"
    else: Data = "soloq"
    return Data
#----------------------------------------------------------------------------------------------------------------
#Le nom des régions peut varié, mais nous le normalisons grace à la fonction suivante
def GetRealRegionName(region):
    region = region.lower()
    if region == "euw": Data = "euw1"
    elif region == "eune": Data = "eun1"
    elif region == "na": Data = "na1"
    elif region == "br": Data = "br1"
    elif region == "jp": Data = "jp1"
    elif region == "kr": Data = "kr"
    elif region == "la": Data = "la1"
    elif region == "las": Data = "la2"
    elif region == "oc": Data = "oc1"
    elif region == "tr": Data = "tr1"
    elif region == "ru": Data = "ru"
    elif region == "pbe": Data = "pbe1"
    else: Data = region
    return Data
#----------------------------------------------------------------------------------------------------------------
#Il existe différent type de match making dans LoL il faut donc s'assurer de la bonne indentation des informations
def GetRightQueue(me, queue_type):
    try:
        if queue_type == "soloq":
            if me[0] != None and me[0]['queueType'] == "RANKED_SOLO_5x5":
                return me[0]
            elif me[1] != None and me[1]['queueType'] == "RANKED_SOLO_5x5":
                return me[1]

        if queue_type == "flexq":
            if me[0] != None and me[0]['queueType'] == "RANKED_FLEX_SR":
                return me[0]
            elif me[1] != None and me[1]['queueType'] == "RANKED_FLEX_SR":
                return me[1]
    except:
        return None
    
# print(GetRankByName("StraightAphelios","EUW","soloq"))
# print(GetRankById("_FEayuuviVm92hz_qqhcgeaufs5hFKszZgx9z9xAoWFqHoQ","euw1","soloq"))
# print(GetProfileIconUrlByIdAndRegion("_FEayuuviVm92hz_qqhcgeaufs5hFKszZgx9z9xAoWFqHoQ","euw1"))
# print(GetIDByNameAndRegion("I AM RANK 1 NUNU",'euw1'))
