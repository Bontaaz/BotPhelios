import os
import discord
import random
import asyncio
import typing
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import Discord.Otherfunction
import BDD.bdd
import Discord.COMMANDS as COMMANDS
import Discord.Admincommand as ADMIN
from discord import Embed
from discord.ext import commands, tasks
from discord import app_commands
from dotenv import load_dotenv
import API_RITO.Riot_Api
import interactions
#POINT IMPORTANT: Les fonction ci-dessous sont appelé par les commandes dans COMMANDS.py, pour plus de détails merci de regarder les commentaires présent là bas
#Embed est un modèle d'encryptage de message reservé au bot, il permet de styliser des messages et ainsi les rendre uniques




def Opgg(name, region, queue):
    Infos = API_RITO.Riot_Api.GetRankByName(name, region, queue)
    if type(Infos) == str:
        embed=discord.Embed(title="", url="https://BotPhelios.errorRank", description=API_RITO.Riot_Api.GetRankByName(name, region, queue), color=0x0084ff)
        embed.set_author(name="BotPhelios", icon_url="https://cdn.discordapp.com/attachments/1079139674116866129/1079140153286725733/219815_1.jpg")
    elif type(Infos) != str:
        # Data = Name=Infos['summonerName'] Rank=Infos['tier'] Division=Infos['rank'] LP=Infos['leaguePoints'] Wins=Infos['wins'] Losses=Infos['losses'] WINRATE=str(round(Infos['wins']/(Infos['wins']+Infos['losses'])*100,2))
        embed=discord.Embed(title="Opgg", url="https://BotPhelios.Rank", description="Here is the infos about "+Infos['summonerName'], color=0xff0000)
        embed.set_author(name="BotPhelios", icon_url="https://cdn.discordapp.com/attachments/1079139674116866129/1079140153286725733/219815_1.jpg")
        embed.set_thumbnail(url=API_RITO.Riot_Api.GetProfileIconUrlByNameAndRegion(Infos['summonerName'], API_RITO.Riot_Api.GetRealRegionName(region)))
        embed.add_field(name="Rank", value=Infos['tier'], inline=True)
        embed.add_field(name="Division", value=Infos['rank'], inline=True)
        embed.add_field(name="LPs", value=Infos['leaguePoints'], inline=False)
        embed.add_field(name="Wins", value=Infos['wins'], inline=True)
        embed.add_field(name="Losses", value=Infos['losses'], inline=True)
        embed.add_field(name="Winrate", value=str(round(Infos['wins']/(Infos['wins']+Infos['losses'])*100,2)), inline=True)
    return embed

def Aleksis(Aleksis007):
    Infos = API_RITO.Riot_Api.GetRankById(Aleksis007, "LAS", "SoloQ")
    embed=discord.Embed(title=Infos['summonerName'], url="https://www.youtube.com/@aleksis007", description="Here are all the infos about Alkesis007", color=0xff0000)
    embed.set_author(name="BotPhelios", icon_url="https://cdn.discordapp.com/attachments/1079139674116866129/1079140153286725733/219815_1.jpg")
    embed.set_thumbnail(url=API_RITO.Riot_Api.GetProfileIconUrlByNameAndRegion(Infos['summonerName'], API_RITO.Riot_Api.GetRealRegionName("LAS")))
    embed.add_field(name="Rank", value=Infos['tier'], inline=True)
    embed.add_field(name="Division", value=Infos['rank'], inline=True)
    embed.add_field(name="LPs", value=Infos['leaguePoints'], inline=False)
    embed.add_field(name="Wins", value=Infos['wins'], inline=True)
    embed.add_field(name="Losses", value=Infos['losses'], inline=True)
    embed.add_field(name="Winrate", value=str(round(Infos['wins']/(Infos['wins']+Infos['losses'])*100,2)), inline=True)
    embed.set_footer(text="https://www.youtube.com/@aleksis007")
    return embed

def Help():
    embed=discord.Embed(title="Commands Available", url="https://BotPhelios.Help", color=0xff0000)
    embed.set_author(name="BotPhelios", icon_url="https://cdn.discordapp.com/attachments/1079139674116866129/1079140153286725733/219815_1.jpg")
    embed.add_field(name="/𝙝𝙚𝙡𝙥", value="show every commands", inline=False)
    embed.add_field(name="/𝙮𝙩", value="get a youtube link to Aleksis007 channel", inline=False)
    embed.add_field(name="/𝙖𝙡𝙚𝙠𝙨𝙞𝙨", value="get every rank info about Aleksis007", inline=False)
    embed.add_field(name="/𝗿𝘂𝗻𝗲𝘀", value="get all the runes for Aphelios", inline=False)
    embed.add_field(name="/𝗶𝘁𝗲𝗺𝘀", value="get all the items for Aphelios", inline=False)
    embed.add_field(name="/𝙤𝙥𝙜𝙜", value="get the opgg data directly into discord", inline=False)
    embed.add_field(name="/𝙢𝙖𝙨𝙩𝙚𝙧𝙞𝙚𝙨", value="get masteries point about a champion", inline=False)
    embed.add_field(name="/𝙗𝙪𝙜𝙧𝙚𝙥𝙤𝙧𝙩", value="report a bug comming from BotPhelios", inline=True)
    embed.set_footer(text="Any question ? Ask @Nunch2#1387")
    return embed

def Masteries(name, region, champion):
    infos=API_RITO.Riot_Api.GetMasteryByChampionName(name, region, champion)
    if type(infos) == str:
        embed=discord.Embed(title="", url="https://BotPhelios.errorMasteries", description=API_RITO.Riot_Api.GetMasteryByChampionName(name, region, champion), color=0x0084ff)
        embed.set_author(name="BotPhelios", icon_url="https://cdn.discordapp.com/attachments/1079139674116866129/1079140153286725733/219815_1.jpg")
    elif type(infos) != str:
        # Data = Name=Infos['summonerName'] Rank=Infos['tier'] Division=Infos['rank'] LP=Infos['leaguePoints'] Wins=Infos['wins'] Losses=Infos['losses'] WINRATE=str(round(Infos['wins']/(Infos['wins']+Infos['losses'])*100,2))
        embed=discord.Embed(title="Masteries", url="https://BotPhelios.Masteries", description="Here is the mastery level of "+name+" on "+champion, color=0xff0000)
        embed.set_author(name="BotPhelios", icon_url="https://cdn.discordapp.com/attachments/1079139674116866129/1079140153286725733/219815_1.jpg")
        embed.set_thumbnail(url=API_RITO.Riot_Api.GetProfileIconUrlByNameAndRegion(name, API_RITO.Riot_Api.GetRealRegionName(region)))
        embed.add_field(name="Champion", value=champion, inline=True)
        embed.add_field(name="Level", value=infos['championLevel'], inline=True)
        embed.add_field(name="Points", value=infos['championPoints'], inline=True)
    return embed

def Runes():
    # staticLength = 3
    embedList = []
    a = BDD.bdd.PrintRunes()
    if type(a) != str:
        for i in a:
            embed=discord.Embed(title="ID: "+str(i[0]), url=i[2], description=i[1], color=0xeeff00)
            embed.set_author(name="BotPhelios", icon_url="https://cdn.discordapp.com/attachments/1079139674116866129/1079140153286725733/219815_1.jpg")
            embed.set_image(url=i[2])
            embedList.append(embed)
    else: 
        embed=discord.Embed(description="No runes available for now", color=0xff0000)
        embed.set_author(name="BotPhelios", icon_url="https://cdn.discordapp.com/attachments/1079139674116866129/1079140153286725733/219815_1.jpg")
        embedList.append(embed)
    return embedList

def Items():
    embedList = []
    a = BDD.bdd.PrintItems()
    if type(a) != str:
        for i in a:
            embed=discord.Embed(title="ID: "+str(i[0]), url=i[2], description=i[1], color=0x0400ff)
            embed.set_author(name="BotPhelios", icon_url="https://cdn.discordapp.com/attachments/1079139674116866129/1079140153286725733/219815_1.jpg")
            embed.set_image(url=i[2])
            embedList.append(embed)
    else: 
        embed=discord.Embed(description="No items available for now", color=0x0400ff)
        embed.set_author(name="BotPhelios", icon_url="https://cdn.discordapp.com/attachments/1079139674116866129/1079140153286725733/219815_1.jpg")
        embedList.append(embed)
    return embedList

def Coaching(name, icon, region, description, discordAleksis007, discordNunch2, discordName):
    riotId = API_RITO.Riot_Api.GetIDByNameAndRegion(name, region)
    if riotId != None:
        if BDD.bdd.GetCoachingDate(riotId) == False:
            infos = API_RITO.Riot_Api.GetRankById(riotId, region, "SoloQ")
            if type(infos) != str:
                rank = infos['tier']
                division = infos['rank']
                leaguePoints = str(infos['leaguePoints'])
            else:
                rank = "Unranked"
                division = "0"
                leaguePoints = "0"
            BDD.bdd.AddCoaching(discordName, icon, rank, division, leaguePoints, riotId, region, description)
            # messageToAleksis = MessageAleksis007(message, discordAleksis007)
            message = "Thank you for applying to a coaching, Aleksis007 has been notified and will contact you soon !\nYou can now upload your replay file here: https://drive.google.com/drive/folders/1trhN6Xp4XUMyFwsBX6ggKWs7ifNdqJK6?usp=share_link\n⚠️MAKE SURE TO CREATE A FOLDER NAMED AS YOUR DISCORD NAME⚠️"
        else:
            message = 1
    else:
        message = 2
    return message