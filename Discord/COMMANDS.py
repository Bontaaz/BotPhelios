import os
import discord
import random
import asyncio
import typing
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import Discord.Otherfunction
import BDD.bdd
import Discord.Admincommand as ADMIN
import Discord.Usercommand as USER
from discord import Embed
from discord.ext import commands, tasks
from discord import app_commands
from dotenv import load_dotenv
import API_RITO.Riot_Api
import interactions
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = interactions.Client(TOKEN)


#Les différentes lignes ci-dessous permettent de tester le bot dans plusieurs serveurs et conditions différentes
#Aleksis
Aleksis007 = '6bocMayFv0MB1UlCRmAYbybEybkkD_-z6pN07btgxMLrVo8'
#Aleksis Discord:
# GuildId = 1079425518916603996
# CoachingChannel = 1079770051546189894
# LoopChannel = 1098573991599427705
#BotTesting
GuildId = 1033732474452328510
CoachingChannel = 1098573663856492676
LoopChannel = 1098573991599427705
#BotTesting PUBLIC
# GuildId = 1098895018267262976
# CoachingChannel = 1098898323785662464
# LoopChannel = 1098898064657350758
#----------------------------------------------------------------------------------------------------------------

# bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
#Lancement et connection du bot à l'api Discord
class abot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
    async def on_ready(self):
        OneMonthCoaching.start()
        await tree.sync(guild=discord.Object(id=GuildId))
        self.synced = True
        print("Bot is online")
#----------------------------------------------------------------------------------------------------------------
#Cette classe permet de donner un style à un bouton de supression
class DeletButton(discord.ui.View):
    @discord.ui.button(label="Done !",
                       style=discord.ButtonStyle.red)
    async def hello(self, interaction: discord.Interaction, button: discord.ui.Button):
        await  interaction.message.delete()
bot = abot()
tree = app_commands.CommandTree(bot)

#----------------------------------------------------------------------------------------------------------------
#                                               [ERROR HANDLER]
#----------------------------------------------------------------------------------------------------------------
@tree.error
async def on_app_command_error(interaction, error):
    if isinstance(error, app_commands.MissingPermissions):
        await interaction.response.send_message(error, ephemeral = True)
    if isinstance(error, app_commands.MissingRole):
        await interaction.response.send_message("You need to be a youtube member to use this command", ephemeral = True)
    else: raise error
#----------------------------------------------------------------------------------------------------------------
#                                               [LOOP]
#----------------------------------------------------------------------------------------------------------------
#Loop chaque mois pour donner une update et supprimer les anciens coaching de la BDD
@tasks.loop(hours=1.0)
async def OneMonthCoaching():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    channel = bot.get_channel(LoopChannel)
    coachingInfos = BDD.bdd.OneMonthCoachingInfos()
    if type(coachingInfos) != str:
        for row in coachingInfos:
            if datetime.strptime(str(row[2]), '%d/%m/%Y %H:%M:%S')  + relativedelta(months=1) <= datetime.strptime(dt_string, '%d/%m/%Y %H:%M:%S'):
                if type(coachingInfos) != str:
                    Infos = API_RITO.Riot_Api.GetRankById(row[3], row[4], "SoloQ")
                    if type(Infos) == str:
                        embed=discord.Embed(title="", url="https://BotPhelios.errorRank", description=Infos, color=0x0084ff)
                        embed.set_author(name="BotPhelios", icon_url="https://cdn.discordapp.com/attachments/1079139674116866129/1079140153286725733/219815_1.jpg")
                    elif type(Infos) != str:
                        # Data = Name=Infos['summonerName'] Rank=Infos['tier'] Division=Infos['rank'] LP=Infos['leaguePoints'] Wins=Infos['wins'] Losses=Infos['losses'] WINRATE=str(round(Infos['wins']/(Infos['wins']+Infos['losses'])*100,2))
                        embed=discord.Embed(title="Opgg", url="https://BotPhelios.Rank", description="One month ago " + row[1] + " was " + row[6] + " " + row[5] + ".\n Now:", color=0xff0000)
                        embed.set_author(name="BotPhelios", icon_url="https://cdn.discordapp.com/attachments/1079139674116866129/1079140153286725733/219815_1.jpg")
                        embed.set_thumbnail(url=API_RITO.Riot_Api.GetProfileIconUrlByNameAndRegion(Infos['summonerName'], API_RITO.Riot_Api.GetRealRegionName(row[4])))
                        embed.add_field(name="Rank", value=Infos['tier'], inline=True)
                        embed.add_field(name="Division", value=Infos['rank'], inline=True)
                        embed.add_field(name="LPs", value=Infos['leaguePoints'], inline=False)
                        embed.add_field(name="Wins", value=Infos['wins'], inline=True)
                        embed.add_field(name="Losses", value=Infos['losses'], inline=True)
                        embed.add_field(name="Winrate", value=str(round(Infos['wins']/(Infos['wins']+Infos['losses'])*100,2)), inline=True)
                        await channel.send(embed=embed, ephemeral = True)
                    else: print("something went wrong")
                BDD.bdd.DelCoaching(row[0])
#----------------------------------------------------------------------------------------------------------------
#                                               [CLASSIC]
#----------------------------------------------------------------------------------------------------------------
#Permet de recevoir ses informations de rank via l'api Riot
@tree.command(name="opgg", description="get basic rank infos", guild=discord.Object(id=GuildId))
@app_commands.describe(name="The summoner name", region="The server region", queue="Queue type")
async def self(interation: discord.Interaction,name:str , region: typing.Literal["EUW","EUNE","NA","BR","JP","KR","LA","LAS","OC","TR","RU"], queue: typing.Literal["SoloQ","FelxQ"]):
    await interation.response.send_message(embed=USER.Opgg(name, region, queue))
#----------------------------------------------------------------------------------------------------------------
#Donne les informations de rank du coach
@tree.command(name="aleksis", description="All Aleksis007 infos", guild=discord.Object(id=GuildId))
async def self(interation: discord.Interaction):
    await interation.response.send_message(embed=USER.Aleksis(Aleksis007), ephemeral = True)
#----------------------------------------------------------------------------------------------------------------
#Donne la liste des commandes
@tree.command(name="help", description="show every commands available", guild=discord.Object(id=GuildId))
async def self(interation: discord.Interaction):
    await interation.response.send_message(embed=USER.Help(), ephemeral = True)
#----------------------------------------------------------------------------------------------------------------
#Donne les informations youtube du coach
@tree.command(name="yt", description="Link to Aleksis007 youtube channel", guild=discord.Object(id=GuildId))
async def self(interation: discord.Interaction):
    await interation.response.send_message("Aleksis007 youtube channel: \nhttps://www.youtube.com/@aleksis007", ephemeral = True)
#----------------------------------------------------------------------------------------------------------------
#Permet de connaitre les statistique d'un joueur sur un personnage uniquement
@tree.command(name="masteries", description="Get masteries point of a user on a precise champion", guild=discord.Object(id=GuildId))
@app_commands.describe(name="The summoner name", region="The server region", champion="The champion you are looking for")
async def self(interaction: discord.Interaction, name: str, region: typing.Literal["EUW","EUNE","NA","BR","JP","KR","LA","LAS","OC","TR","RU"], champion: str):
    await interaction.response.send_message(embed=USER.Masteries(name, region, champion))
#----------------------------------------------------------------------------------------------------------------
#Permet de connaitres les runes les plus optimales
@tree.command(name="runes", description="Informations about what runes to take in different matchup", guild=discord.Object(id=GuildId))
async def self(interation: discord.Interaction):
    await interation.response.send_message(embeds=USER.Runes(), ephemeral = True)
#----------------------------------------------------------------------------------------------------------------
#Permet de connaitres les objets les plus optimaux
@tree.command(name="items", description="Informations about what items to take in different matchup", guild=discord.Object(id=GuildId))
async def self(interation: discord.Interaction):
    await interation.response.send_message(embeds=USER.Items(), ephemeral = True)
#----------------------------------------------------------------------------------------------------------------
#Permet de reserver une scéance de coaching à raison de une fois par mois
@tree.command(name="coaching", description="Apply for a coaching session with Aleksis007", guild=discord.Object(id=GuildId))
# @app_commands.checks.has_role(1079800586221916173)
@app_commands.describe(name="tell me your in game name", region="Your server region", description="Give more context to the replay, or anything you want to say to Aleksis ?")
async def self(interation: discord.Interaction, name: str, region: typing.Literal["EUW","EUNE","NA","BR","JP","KR","LA","LAS","OC","TR","RU"], description: str):
    discordAleksis007 = await bot.fetch_user(535097144500158464)
    discordNunch2 = await bot.fetch_user(218775238027116545)
    discordName = str(interation.user.name)
    discordIcon = interation.user.avatar
    message = USER.Coaching(name, discordIcon, region, description, discordAleksis007, discordNunch2, discordName)
    if message == 1: message = "Sorry but you can only apply for one coaching every months"
    elif message == 2: message = "Make sure you have entered the right informations"
    else:
        if discordIcon == None:
            discordIcon = "https://cdn.discordapp.com/attachments/1079809895450300446/1083061610408575107/images.png"
        dmMessage = discordName + " just applied for a coaching ! Use '/showcoaching name:" + discordName + "' to get all the informations, when the coaching session is done, click on the 'Done !' button to delet this message"
        await MessageNunch2(dmMessage, discordNunch2)
        # MessageAleksis007(dmMessage, discordAleksis007)
    await interation.response.send_message(message,ephemeral=True)
#----------------------------------------------------------------------------------------------------------------
#                                               [ADMIN]
#----------------------------------------------------------------------------------------------------------------
#Montre les commands admin comme le /help
@tree.command(name="admincommands", description="list of commands", guild=discord.Object(id=GuildId))
@app_commands.checks.has_permissions(administrator=True)
async def self(interation: discord.Interaction):
    await interation.response.send_message(embed=ADMIN.ShowAdminCommand(), ephemeral=True)
#----------------------------------------------------------------------------------------------------------------
#Affiche les donnés d'un coaching en particulier
@tree.command(name="showcoaching", description="you can show coaching data by a given discord name", guild=discord.Object(id=GuildId))
@app_commands.describe(name="Discord name given in DM")
@app_commands.checks.has_permissions(administrator=True)
async def self(interation:discord.Interaction,name: str):
    infos = ADMIN.ShowCoaching(name)
    if type(infos) is str:
        await interation.response.send_message(infos, ephemeral=True)
    else:
        await interation.response.send_message(embed=ADMIN.ShowCoaching(name), ephemeral=True)
#----------------------------------------------------------------------------------------------------------------
#Affiche les données de tous les coaching
@tree.command(name="allcoaching", description="you can show ALL coaching data by a given discord name", guild=discord.Object(id=GuildId))
@app_commands.checks.has_permissions(administrator=True)
async def self(interation: discord.Interaction):
    infos = ADMIN.AllCoaching()
    if type(infos) is str:
        await interation.response.send_message("Sorry no coaching asked", ephemeral=True)
    else:
        await interation.response.send_message(embeds=infos, ephemeral=True)
#----------------------------------------------------------------------------------------------------------------
#Supprime un coaching de la bdd
@tree.command(name="delcoaching", description="you can delet a coaching by a given discord name", guild=discord.Object(id=GuildId))
@app_commands.describe(name="Discord name given in DM")
@app_commands.checks.has_permissions(administrator=True)
async def self(interaction: discord.Interaction, name: str):
    await interaction.response.send_message(BDD.bdd.DelCoachingByName(name), ephemeral = True)
#------------------------------------------------------------------------------------------------------------------------------------
#Ajoute des runes
@tree.command(name="addrunes", description="admin can add RUNES (MAKE SUR THE IMAGE LINK IS CORRECT)", guild=discord.Object(id=GuildId))
@app_commands.describe(message="A little description on why to take this runes", link="Image link (better to use discord link)")
@app_commands.checks.has_permissions(administrator=True)
async def self(interaction: discord.Interaction, message: str, link: str):
     await interaction.response.send_message(BDD.bdd.AddRunes(message, link), ephemeral=True)
#----------------------------------------------------------------------------------------------------------------
#Supprime des runes
@tree.command(name="delrunes", description="admin can delet RUNES", guild=discord.Object(id=GuildId))
@app_commands.describe(id="Give the id you want to delet")
@app_commands.checks.has_permissions(administrator=True)
async def self(interaction: discord.Interaction, id: int):
     await interaction.response.send_message(BDD.bdd.DelRunes(id), ephemeral=True)
#----------------------------------------------------------------------------------------------------------------
#Ajoute des items
@tree.command(name="additems", description="admin can add ITEMS (MAKE SUR THE IMAGE LINK IS CORRECT)", guild=discord.Object(id=GuildId))
@app_commands.describe(message="A little description on why to take this items", link="Image link (better to use discord link)")
@app_commands.checks.has_permissions(administrator=True)
async def self(interaction: discord.Interaction, message: str, link: str):
     await interaction.response.send_message(BDD.bdd.AddItems(message, link), ephemeral=True)
#----------------------------------------------------------------------------------------------------------------
#Supprime des items
@tree.command(name="delitems", description="admin can delet ITEMS", guild=discord.Object(id=GuildId))
@app_commands.describe(id="Give the id you want to delet")
@app_commands.checks.has_permissions(administrator=True)
async def self(interaction: discord.Interaction, id: int):
     await interaction.response.send_message(BDD.bdd.DelItems(id), ephemeral=True)
#----------------------------------------------------------------------------------------------------------------
#Permet de report un bug au dev
@tree.command(name="bugreport", description="Report a bug comming ⚠️ FROM BotPhelios ⚠️, for discord issues or other, pls contact @Nunch2#1387", guild=discord.Object(id=GuildId))
async def self(interaction: discord.Interaction, explanation: str):
    embed=discord.Embed(title="", url="https://BotPhelios.nunch2.repl.co", description=BDD.bdd.AddReport(explanation), color=0x0084ff)
    embed.set_author(name="BotPhelios", icon_url="https://cdn.discordapp.com/attachments/1079139674116866129/1079140153286725733/219815_1.jpg")
    await interaction.response.send_message(embed=embed, ephemeral=True)
#----------------------------------------------------------------------------------------------------------------
#Le dev peut afficher tous les bugs
@tree.command(name="showbuglist", description="Informations about what runes to take in different matchup", guild=discord.Object(id=GuildId))
@app_commands.checks.has_permissions(administrator=True)
async def self(interation: discord.Interaction):
    infos = ADMIN.ShowBugList()
    if type(infos) is str:await interation.response.send_message(infos, ephemeral=True)
    else:await interation.response.send_message(embeds=infos, ephemeral=True)
#----------------------------------------------------------------------------------------------------------------
#Supprime un bug une fois corrigé
@tree.command(name="delbugs", description="admin can delet BUGS in the bug list", guild=discord.Object(id=GuildId))
@app_commands.checks.has_permissions(administrator=True)
async def self(interaction: discord.Interaction, id: int):
    await interaction.response.send_message(BDD.bdd.DelBugs(id), ephemeral=True)
#----------------------------------------------------------------------------------------------------------------

# @tree.command(name="wewillsee", description="Apply for a coaching session with Aleksis007", guild=discord.Object(id=GuildId))
# # @app_commands.checks.has_role(1079800586221916173)
# async def self(interation: discord.Interaction):
#     discordNunch2 = await bot.fetch_user(218775238027116545)
#     view = DeletButton()
#     messageToNunch2 = await discordNunch2.send(" just applied for a coaching ! Use '/showcoaching name:" + "' to get all the informations", view=view)


#----------------------------------------------------------------------------------------------------------------
#                                               [ON MESSAGE EVENT]
#----------------------------------------------------------------------------------------------------------------
#Supprime les messages envoyé dans un channel discord en particulié
@bot.event
async def on_message(message):
    if  message.channel.id == CoachingChannel:
        if message.author.id == bot.user.id:
            return
        else:
            await message.delete()

#Permet d'envoyer un message privé à un dev
async def MessageNunch2(message, discordNunch2):
    await discordNunch2.send(message, view=DeletButton())
# async def MessageAleksis007(message, discordAleksis007):
#     await discordAleksis007.send(message, view=COMMANDS.DeletButton())


# @tree.command(name="embed", description="Get masteries point of a user on a precise champion", guild=discord.Object(id=GuildId))
# async def self(interaction: discord.Interaction, name: str, region: typing.Literal["EUW","EUNE","NA","BR","JP","KR","LA","LAS","OC","TR","RU"], champion: str):
#         a = []
#     # if description=GetMasteryByChampionName(name ,region, champion) == list:
#     #else :
#         #description="make sure enter right mes couilles"
#     #modifier url pour send plusieur embed
#         embed=discord.Embed(title="", url="https://BotPhelios.nunch2.repl.co", description="you know what i know", color=0x0084ff)
#         embed.set_author(name="BotPhelios", icon_url="https://cdn.discordapp.com/attachments/1079139674116866129/1079140153286725733/219815_1.jpg")
#         embed.set_image(url="https://cdn.discordapp.com/attachments/1079139674116866129/1079140153286725733/219815_1.jpg")
#         embed2=discord.Embed(title="", url="https://BotPhelios.nunch2.repl.com", description="second oneazfiugaizufaiuzfgiazfaziufgagfiazgfiuazfggaizfiaviaegviauga", color=0x0088ff)
#         embed2.set_author(name="BotPhelios", icon_url="https://cdn.discordapp.com/attachments/1079139674116866129/1079140153286725733/219815_1.jpg")
#         embed2.set_image(url="https://cdn.discordapp.com/attachments/1079139674116866129/1079140153286725733/219815_1.jpg")
#         embed3=discord.Embed(title="", url="https://BotPhelios.nunch2.repl.com", description="second oneazfiugaizufaiuzfgiazfaziufgagfiazgfiuazfggaizfiaviaegviauga", color=0x0088ff)
#         embed3.set_author(name="BotPhelios", icon_url="https://cdn.discordapp.com/attachments/1079139674116866129/1079140153286725733/219815_1.jpg")
#         embed3.set_image(url="azdazdazdazdazd")
#         await interaction.response.send_message(embed=embed3)
#----------------------------------------------------------------------------------------------------------------
#                                               [LAUNCH FUNCTION]
#----------------------------------------------------------------------------------------------------------------
#Fonction de lancement du bot
def Launch():
    bot.run(TOKEN)