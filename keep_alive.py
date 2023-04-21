from flask import Flask
from threading import Thread
#Ici nous permettons au bot de créer une page web qui est ensuite ping par un robot toutes les 5 minutes permettant de garder le bot en vie



app = Flask('')


@app.route('/')
def home():
  return "Discord.py Bot is online"


def run():
  app.run(host='0.0.0.0', port=8080)


def keep_alive():
  t = Thread(target=run)
  t.start()