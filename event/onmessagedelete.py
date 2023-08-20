import discord
from discord.ext import commands
import time
import datetime
import json
datebot = "lifetime"
oauth = "https://discord.com/api/oauth2/authorize?client_id=1034818686705479690&permissions=8&scope=bot"
cerdit = "Super Bot "
type  =  "Gestion v1"
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
    client.add_cog(on_message_delete(client))
class on_message_delete(commands.Cog):
    def __init__(self,client):
        self.client = client   
    @commands.Cog.listener()
    async def on_message_delete(self,message):        
        if await self.client.process_commands(message = message):
            pass
        else :
            channel = message.guild.get_channel(get.logmessage(id = message.guild.id))
            embed2 = discord.Embed(
                title="Message surpimer",
                description=
                f"Le message de <@{message.author.id}> a été supprimé \n> **Content** : {message.content}")
            embed2.timestamp = datetime.datetime.utcnow()
            embed2.set_author(icon_url= message.author.avatar_url,name= message.author.name)
            embed2.set_footer(icon_url=  self.client.user.avatar_url, text = f" {cerdit} \u200b")
            await channel.send(embed=embed2)