import json
import discord
from datetime import datetime
#Everything below is not used because i used a database and not a json
#----------------------------------------------------------------------------------------------------------------

def GetRunesMessage():
    finalString = str()
    y = open('Discord/JSON/runes.json')
    data = json.load(y)
    for i in data['Runes message']:
        finalString += i
    y.close()
    return finalString
#----------------------------------------------------------------------------------------------------------------

def UpdateRunesMessage(newMessage):
    print(type("hey"))
    print(type(newMessage))
    dictionary = {
        "Rune message": newMessage
    }
    
    # Serializing json
    json_object = json.dumps(dictionary, indent=1)
    
    # Writing to sample.json
    with open("Discord/JSON/runes.json", "w") as outfile:
        outfile.write(json_object)
    return newMessage
#----------------------------------------------------------------------------------------------------------------

def GetItemsMessage():
    finalString = str()
    y = open('Discord/JSON/items.json')
    data = json.load(y)
    for i in data['Runes message']:
        finalString += i
    y.close()
    return finalString
#----------------------------------------------------------------------------------------------------------------

def UpdateItemsMessage(newMessage):
    print(type("hey"))
    print(type(newMessage))
    dictionary = {
        "Rune message": newMessage
    }
    
    # Serializing json
    json_object = json.dumps(dictionary, indent=1)
    
    # Writing to sample.json
    with open("Discord/JSON/ritems.json", "w") as outfile:
        outfile.write(json_object)
    return newMessage

def ConvertItemsStringToArray(string):
    newString = ''
    finalArray = []
    for i in string:
        if i != '|':
            newString += i
        elif i == '|':
            finalArray.append(newString)
            newString = ''
    return finalArray


def GetActualDate():
    now = datetime.now()
    actualDate = now.strftime("%d/%m/%Y %H:%M:%S")
    return actualDate