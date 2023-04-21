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
from discord import Embed
from discord.ext import commands, tasks
from discord import app_commands
from dotenv import load_dotenv
import API_RITO.Riot_Api
import interactions
#POINT IMPORTANT: Les fonction ci-dessous sont appelé par les commandes dans COMMANDS.py, pour plus de détails merci de regarder les commentaires présent là bas
#Embed est un modèle d'encryptage de message reservé au bot, il permet de styliser des messages et ainsi les rendre uniques

# bot = COMMANDS.abot()
# tree = app_commands.CommandTree(bot)
# GuildId = COMMANDS.GuildId

#----------------------------------------------------------------------------------------------------------------
#                                               [ERROR HANDLER BELOW]
#----------------------------------------------------------------------------------------------------------------
# @tree.error
# async def on_app_command_error(interaction, error):
#     if isinstance(error, app_commands.MissingPermissions):
#         await interaction.response.send_message(error, ephemeral = True)
#     if isinstance(error, app_commands.MissingRole):
#         await interaction.response.send_message("You need to be a youtube member to use this command", ephemeral = True)
#     else: raise error
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
def ShowAdminCommand():
    embed=discord.Embed(title="Commands Available", url="https://BotPhelis.AdminCommands", color=0xff0000)
    embed.set_author(name="BotPhelios", icon_url="https://cdn.discordapp.com/attachments/1079139674116866129/1079140153286725733/219815_1.jpg")
    embed.add_field(name="/𝙝𝙚𝙡𝙥", value="show every commands", inline=False)
    embed.add_field(name="/𝙖𝙡𝙚𝙠𝙨𝙞𝙨", value="get every rank info about Aleksis007", inline=False)
    embed.add_field(name="/𝗿𝘂𝗻𝗲𝘀", value="get all the runes for Aphelios", inline=False)
    embed.add_field(name="/𝗶𝘁𝗲𝗺𝘀", value="get all the items for Aphelios", inline=False)
    embed.add_field(name="/𝙤𝙥𝙜𝙜", value="get the opgg data directly into discord", inline=False)
    embed.add_field(name="/𝙢𝙖𝙨𝙩𝙚𝙧𝙞𝙚𝙨", value="get masteries point about a champion", inline=False)
    embed.add_field(name="/𝙗𝙪𝙜𝙧𝙚𝙥𝙤𝙧𝙩", value="report a bug comming from BotPhelios", inline=False)
    embed.add_field(name="",value='-----------------\n👇【A】【D】【M】【I】【N】👇\n-----------------', inline=False)
    embed.add_field(name="/addrunes", value="add runes to the list", inline=False)
    embed.add_field(name="/delrunes", value="delet runes from the list", inline=False)
    embed.add_field(name="/additems", value="add items to the list", inline=False)
    embed.add_field(name="/delitems", value="delet items from the list", inline=False)
    embed.add_field(name="/showbuglist", value="get the list of all the bugs reported", inline=False)
    embed.add_field(name="/delbugs", value="delet bug from the list", inline=False)
    embed.add_field(name="/showcoaching", value="Get coaching information by giving a discord name", inline=False)
    embed.add_field(name="/allcoaching", value="Get ALL coaching information", inline=False)
    embed.add_field(name="/delcoaching", value="Delet a coaching from the list by giving a discord name", inline=False)
    embed.set_footer(text="Any question ? Ask @Nunch2#1387")
    return embed
#------------------------------------------------------------------------------------------------------------------------------------
def ShowCoaching(name):
    row = BDD.bdd.AleksisPrintCoaching(name)
    if type(row) != str:
        for infos in row:
            embed=discord.Embed(title="", url="https://BotPhelios.Coaching", color=0x00ff33)
            embed.set_author(name="BotPhelios", icon_url="https://cdn.discordapp.com/attachments/1079139674116866129/1079140153286725733/219815_1.jpg")
            embed.set_thumbnail(url=infos[5])
            embed.add_field(name="Name", value=infos[0], inline=False)
            embed.add_field(name="Rank", value=infos[2], inline=True)
            embed.add_field(name="Division", value=infos[3], inline=True)
            embed.add_field(name="Region", value=infos[1], inline=True)
            embed.add_field(name="Description", value=infos[4], inline=False)
        return embed
    else:
        return "Sorry no coaching asked by " + name
#------------------------------------------------------------------------------------------------------------------------------------
def AllCoaching():
    embedList = []
    row = BDD.bdd.AleksisPrintAllCoaching()
    if type(row) != str:
        for infos in row:
            embed=discord.Embed(title="", color=0x00ff33)
            embed.set_author(name="BotPhelios", icon_url="https://cdn.discordapp.com/attachments/1079139674116866129/1079140153286725733/219815_1.jpg")
            embed.set_thumbnail(url=infos[5])
            embed.add_field(name="Name", value=infos[0], inline=False)
            embed.add_field(name="Rank", value=infos[2], inline=True)
            embed.add_field(name="Division", value=infos[3], inline=True)
            embed.add_field(name="Region", value=infos[1], inline=True)
            embed.add_field(name="Description", value=infos[4], inline=False)
            embedList.append(embed)
        return embedList
    else:
        return "Sorry no coaching asked"
#----------------------------------------------------------------------------------------------------------------
def ShowBugList():
    # staticLength = 3
    embedList = []
    a = BDD.bdd.PrintBugs()
    if type(a) != str:
        for i in a:
            embed=discord.Embed(title="Bug Report", color=0xff0000)
            embed.set_author(name="BotPhelios", icon_url="https://cdn.discordapp.com/attachments/1079139674116866129/1079140153286725733/219815_1.jpg")
            embed.add_field(name="ID:", value=str(i[0]), inline=False)
            embed.add_field(name="Date:", value=i[1], inline=False)
            embed.add_field(name="Description", value=i[2], inline=False)
            embedList.append(embed)
    else: 
        embedList = "No bug yet vamos"
    return embedList
#----------------------------------------------------------------------------------------------------------------