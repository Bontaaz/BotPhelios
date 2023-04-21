import sqlite3
from datetime import datetime
# import pandas as pd

conn = sqlite3.connect('BotPheliosBdd.db')
c = conn.cursor()


def CreateTable():
  c.execute('''
            CREATE TABLE IF NOT EXISTS runes
            ([runes_id] INTEGER PRIMARY KEY, [runes_description] TEXT, [runes_screenlink] TEXT)
            ''')
  c.execute('''
            CREATE TABLE IF NOT EXISTS items
            ([items_id] INTEGER PRIMARY KEY, [items_description] TEXT, [items_screenlink] TEXT)
            ''')
  c.execute('''
            CREATE TABLE IF NOT EXISTS bugsreport
            ([bugsreport_id] INTEGER PRIMARY KEY, [bugsreport_date] TEXT, [bugsreport_description] TEXT)
            ''')
  c.execute('''
          CREATE TABLE IF NOT EXISTS coaching
          ([coaching_id] INTEGER PRIMARY KEY, [coaching_discordName] TEXT, [coaching_discordIcon] TEXT, [coaching_date] TEXT, [coaching_actualRank] TEXT, [coaching_actualDivision] TEXT, [coaching_actualLp] TEXT, [coaching_riotId] TEXT, [coaching_region] TEXT, [coaching_description] TEXT)
          ''')
  conn.commit()


#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#Renvoi les runes
def PrintRunes():
  c.execute('''
          SELECT
          runes_id,
          runes_description,
          runes_screenlink
          FROM runes
          ''')
  rows = c.fetchall()
  if str(rows) == "[]":
    rows = ("no runes available right know")
    return rows
  # return RemoveShit(str(rows))
  return rows

#Ajoute les runes à la table
def AddRunes(RunesDesc, RunesLink):
  RunesDesc = "'" + RunesDesc + "'"
  RunesLink = "'" + RunesLink + "'"
  c.execute('''
            INSERT INTO runes (runes_description, runes_screenlink)
                    VALUES
                    (''' + RunesDesc + ''',''' + RunesLink + ''')
            ''')
  conn.commit()
  print("runes added")
  return "Runes added"

#Supprime les runes
def DelRunes(RunesId: int):
  RunesId = str(RunesId)
  c.execute('''
            DELETE FROM runes WHERE runes_id = ''' + RunesId + '''
            ''')
  conn.commit()
  return "Runes Deleted"


#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#Affiche les items
def PrintItems():
  c.execute('''
          SELECT
          items_id,
          items_description,
          items_screenlink
          FROM items
          ''')
  rows = c.fetchall()
  if str(rows) == "[]":
    rows = ("no items available right know")
    return rows
  # return RemoveShit(str(rows))
  return rows

#Ajoute les items à la table
def AddItems(ItemsDesc, ItemsLink):
  ItemsDesc = "'" + ItemsDesc + "'"
  ItemsLink = "'" + ItemsLink + "'"
  c.execute('''
            INSERT INTO items (items_description, items_screenlink)
                    VALUES
                    (''' + ItemsDesc + ''',''' + ItemsLink + ''')
            ''')
  conn.commit()
  return "Items added"

#Supprime un item de la table
def DelItems(ItemsId: int):
  ItemsId = str(ItemsId)
  c.execute('''
            DELETE FROM items WHERE items_id = ''' + ItemsId + '''
            ''')
  conn.commit()
  return "Items Deleted"
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#Ajoute un report de bug
def AddReport(BugDescription):
  now = datetime.now()
  dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
  dt_string = "'" + dt_string + "'"
  BugDescription = "'" + BugDescription + "'"
  c.execute('''
            INSERT INTO bugsreport (bugsreport_date, bugsreport_description)
                    VALUES
                    (''' + dt_string + ''',''' + BugDescription + ''')
            ''')
  conn.commit()
  return "Thanks for your report !"

#Renvoi les bugs de la table
def PrintBugs():
  c.execute('''
          SELECT
          bugsreport_id,
          bugsreport_date,
          bugsreport_description
          FROM bugsreport
          ''')
  rows = c.fetchall()
  if str(rows) == "[]":
    rows = ("no bugs yet VAMOS")
    return rows
  # return RemoveShit(str(rows))
  return rows

#Supprime un bug de la table en fonction de son ID
def DelBugs(bugsId: int):
  bugsId = str(bugsId)
  c.execute('''
            DELETE FROM bugsreport WHERE bugsreport_id = ''' + bugsId + '''
            ''')
  conn.commit()
  return "Bug deleted from list"
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#Ajoute un coahcing à la liste
#([coaching_id] INTEGER PRIMARY KEY, [coaching_date] TEXT, [coaching_actualRank] TEXT, [coaching_actualDivision] TEXT, [coaching_actualLp] TEXT, [coaching_riotId], TEXT[coaching_region])
def AddCoaching(discordName, discordIcon, actualRank, actualDivision, actualLp, riotId, region, description):
  now = datetime.now()
  dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
  discordName = "'" + discordName + "'"
  discordIcon = "'" + str(discordIcon) + "'"
  dt_string = "'" + dt_string + "'"
  actualRank = "'" + actualRank + "'"
  actualDivision = "'" + actualDivision + "'"
  actualLp = "'" + actualLp + "'"
  riotId = "'" + riotId + "'"
  region = "'" + region + "'"
  description = "'" + description + "'"
  c.execute('''
            INSERT INTO coaching (coaching_discordName, coaching_discordIcon, coaching_date, coaching_actualRank, coaching_actualDivision, coaching_actualLp, coaching_riotId, coaching_region, coaching_description)
                    VALUES
                    (''' + discordName + ''',''' + discordIcon + ''',''' + dt_string + ''',''' + actualRank + ''',''' + actualDivision + ''',''' + actualLp + ''',''' + riotId + ''',''' + region + ''',''' + description + ''')
            ''')
  conn.commit()

#Renvoi la un coaching en particulié
def AleksisPrintCoaching(discordName):
  discordName = "'" + discordName + "'"
  c.execute('''
          SELECT
          coaching_discordName,
          coaching_region,
          coaching_actualRank,
          coaching_actualDivision,
          coaching_description,
          coaching_discordIcon
          FROM coaching
          WHERE coaching_discordName = ''' + discordName + '''
          ''')
  rows = c.fetchall()
  if str(rows) == "[]":
    return "No coaching in the list"
  # return RemoveShit(str(rows))
  return rows

#Renvoi une liste de tous les coaching présent dans la bdd
def AleksisPrintAllCoaching():
  c.execute('''
          SELECT
          coaching_discordName,
          coaching_region,
          coaching_actualRank,
          coaching_actualDivision,
          coaching_description,
          coaching_discordIcon
          FROM coaching
          ''')
  rows = c.fetchall()
  if str(rows) == "[]":
    rows = ("No coaching in the list")
    return rows
  # return RemoveShit(str(rows))
  return rows


#Permet à la loop des 1 mois de poster les informations sur la personne qui a était coach
def OneMonthCoachingInfos():
  c.execute('''
          SELECT
          coaching_id,
          coaching_discordName,
          coaching_date,
          coaching_riotId,
          coaching_region,
          coaching_actualDivision,
          coaching_actualRank,
          coaching_description
          FROM coaching
          ''')
  rows = c.fetchall()
  if str(rows) == "[]":
    rows = ("no coaching in the list")
    return rows
  # return RemoveShit(str(rows))
  return rows


#Supprime un coaching de la bdd en fonction de son id (non utilisé)
def DelCoaching(coachingId: int):
  coachingId = str(coachingId)
  print('deleting coaching number '+coachingId)
  c.execute('''
            DELETE FROM coaching WHERE coaching_id = ''' + coachingId + '''
            ''')
  conn.commit()
  return "Coaching Deleted"


#Supprime un coaching en fonction du nom de la personne
def DelCoachingByName(coachedName: str):
  coachedName = "'"+coachedName+"'"
  print('deleting coaching number '+coachedName)
  c.execute('''
            DELETE FROM coaching WHERE coaching_discordName = ''' + coachedName + '''
            ''')
  conn.commit()
  return "Coaching Deleted"


#Renvoie la date de création de la demande de coaching
def GetCoachingDate(riotId):
  riotId = "'" + riotId + "'"
  c.execute('''
          SELECT coaching_date FROM coaching WHERE coaching_riotId = ''' + riotId + '''
          ''')
  rows = c.fetchall()
  if str(rows) == "[]":
    return False
  else:
    return True

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#Fonction permettant de réindenter certaines string (non utilisé)
def RemoveShit(Text: str):
  NewText = ""
  for i in Text:
    if i == '(' or i == ')' or i == "'" or i == '[' or i == ']' or i == " ":
      i = ""
    if i == ',': i = "\n"
    NewText += i
  return NewText
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#Permet de renommer une table (partiellement utilisé)
def RenameTable(OldName: str, NewName: str):
  c.execute('''
            ALTER TABLE ''' +OldName+''' RENAME '''+NewName+'''
            ''')
  conn.commit()


#Cette fonction se lance à chaque démarrage pour assurer un bon fonctionnement des tables
CreateTable()
# conn.commit()
# AddRunes("PTA Shitezfnzaepifnoziefnzeoifnizo","https://cdn.discordapp.com/attachments/1079139674116866129/1079350654209900554/image.png")
# AddRunes("CONQUEROR YAYA","https://cdn.discordapp.com/attachments/1079139674116866129/1079350748577529916/image.png")
# a = PrintRunes()
# for i in a:
#   print(i[1])

