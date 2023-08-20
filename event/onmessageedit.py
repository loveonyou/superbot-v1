import discord
from discord.ext import commands
import time
import datetime
import json
datebot = "lifetime"
oauth = "https://discord.com/api/oauth2/authorize?client_id=1034818686705479690&permissions=8&scope=bot"
cerdit = "Super Bot "
type  =  "Gestion v1"
def getantilink(id):
    with open('./db/antiraid/antilink.json', 'r') as f:
        prefixes = json.load(f)
    if prefixes[f"{id}"] == "on":
        return True
    if prefixes[f"{id}"] == "off":
        return False
def geteveryone(id):
    with open('./db/antiraid/antieveryone.json', 'r') as f:
        prefixes = json.load(f)
    if prefixes[f"{id}"] == "on":
        return True
    if prefixes[f"{id}"] == "off":
        return False
class get():
  def logmessage(id):
    with open('./db/logs/message.json', 'r') as f:
      prefixes = json.load(f)
      return int(prefixes[str(id)])

  def logrole(id):
    with open('./db/logs/role.json', 'r') as f:
      prefixes = json.load(f)
      return int(prefixes[str(id)])

  def logserveur(id):
    with open('./db/logs/serveur.json', 'r') as f:
      prefixes = json.load(f)
      return int(prefixes[str(id)])
def checkwl(id):
    with open('./db/wl/wl.json', 'r') as f:
      prefixes = json.load(f)
      lenwl = len(prefixes['wl'])
    wllen = -1
    for i in range(0,lenwl):
        wllen + 1
        if prefixes['wl'][wllen]  == str(id):
            return True

def checkowner(id):
    with open('./db/wl/owner.json', 'r') as f:
        prefixes = json.load(f)
        lenowner = len(prefixes['owner'])
    ownerlen = -1
    for i in range(0,lenowner):
        ownerlen + 1
        if prefixes['owner'][ownerlen]  == str(id):
            return True  
def getprefix(id):
        with open('./db/command/prefix.json', 'r') as f:
            prefixes = json.load(f)

            prefixr = prefixes[str(id.guild.id)] 
            return prefixr
def isowner(idowner):
    if idowner == 1024298168264953936:
        return True      
def setup(client):
    client.add_cog(on_message_edit(client))
class on_message_edit(commands.Cog):
    def __init__(self,client):
        self.client = client   
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if await self.client.process_commands(before):
            return
        else : 
            if getantilink(id = after.guild.id) == True:
                if "discord.gg" in after.content.lower():
                    if checkwl(id  = after.author.id) == True:
                            return
                    else:
                        if checkowner(id = after.author.id) == True:
                            return
                        else :
                            await after.delete() 
                            await after.channel.send(f"**Tu n'est pas autorisé a envoyer des invitations <@{before.author.id}> **")
                            embed = discord.Embed(
                            title = "Antilink Message",
                            description = f"**Content du message avant** : ``{before.content}``\n**Content du message apres** : ``{after.content}``"
                        )
                            embed.set_author(
                            name = after.author.name,
                            icon_url = after.author.avatar_url
                            )
                            embed.set_footer( text = f" {cerdit} \u200b ")          
                            channel = before.guild.get_channel(get.logmessage(id = before.guild.id)) 
                            await channel.send(embed = embed)  
                            return        
            if geteveryone(id = before.guild.id) == True:
                                if "@everyone" in after.content.lower():
                                    if checkwl(id  = after.author.id) == True:
                                        return
                                    else : 
                                        if checkowner(id = after.author.id) == True:
                                            return
                                        else :
                                            await after.delete() 
                                            await after.channel.send(f"**Tu n'est pas autorise a mentionnez everyone ici <@{before.author.id}>**")
                                            embed = discord.Embed(
                                            title = "Antieveryone Message",
                                            description = f"**Content du message avant** : ``{before.content}``\n**Content du message apres** : ``{after.content}``"
                                            )
                                            embed.set_author(
                                            name = before.author.name,
                                            icon_url = before.author.avatar_url
                                            )
                                            embed.timestamp = datetime.datetime.utcnow()
                                            embed.set_footer( text = f" {cerdit} \u200b ")          
                                            await channel.send(embed = embed)  
        
        embed = discord.Embed(
        title = "Message Edit",
        description = f"**Content du message avant** : ``{before.content}``\n**Content du message apres** : ``{after.content}``"
        )
        embed.set_author(
        name = before.author.name,
        icon_url = before.author.avatar_url
        )
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer( text = f" {cerdit} \u200b ") 
        channel = before.guild.get_channel(get.logmessage(id = before.guild.id))         
        await channel.send(embed = embed)                               