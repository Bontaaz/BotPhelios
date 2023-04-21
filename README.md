# BotPhelios - ProjetDEV - Groupe6B

BotPhelios est un bot Discord programmé en Python et permettant de recevoir des informations depuis l'API de Riot Games sur les joueurs et les personnages du jeu vidéo League of Legends.

## Pour commencer
Ce bot est uniquement présent sur un serveur en particulier, néanmoins il est possible de le rendre accessible partout.

Pour cela:
  * Rendez-vous dans le fichier COMMANDS.py présent dans le dossier Discord.
  * Modifiez la ligne ci-dessous avec: 
```python
intents=discord.Intent.default()
```

![image](https://user-images.githubusercontent.com/98102389/233601065-babbe2b5-e26a-413e-93d1-f43b4423ac91.png)
  * Supprimez ensuite le GuildId dans chaque commande.

## Lancer le bot
Pour lancer le bot, il vous suffit de cloner le lien ce repository grâce à la commande: 'git clone https://github.com/Bontaaz/BotPhelios.git'
Installez ensuite les packages nécessaires.
Lancez ensuite le main en utilisant : `python3 main.py`

## Inviter le bot sur un serveur discord
Pour inviter le bot, assurez-vous d'être administrateur du serveur. Cliquez ensuite sur le lien suivant.
https://discord.com/api/oauth2/authorize?client_id=1078402825891102831&permissions=8&scope=bot

## Exemple de commandes complexes
`/opgg name:WallAphelios region:EUW queue:SoloQ`
Permet d'afficher les informations de classement du joueur 'WallAphelios'

`/coaching name:WallAphelios region:EUW description:j'aimerais me faire coach car je suis nul`
Permet de réserver une session de coaching avec le coach affilié

`/showcoaching name:WallAphelios`
Permet de voir les informations sur la personne souhaitant se faire coach (normalement accessible uniquement du coach ou des admins)

## Comment voir si le bot est up ou non ?
D'abord regarder si le bot à un petit logo vert à coté de sa photo
![image](https://user-images.githubusercontent.com/98102389/233603491-db131a9e-0761-4910-8542-3f8f1cb0a741.png)

Vous pouvez aussi le confirmer sur
https://botphelios-dev.nunch2.repl.co

