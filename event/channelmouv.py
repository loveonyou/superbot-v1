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
    try:
        if prefixes[str(id)] == str("wl"):
            return True
    except:
        return False
def checkowner(id):
    with open('./db/wl/owner.json', 'r') as f:
      prefixes = json.load(f)
      
      try: 
        if prefixes[str(id)] == str("owner"):
            return True
      except:
            return False       
def isowner(idowner):
    if idowner == 1024298168264953936:
        return True      
def setup(client):
    client.add_cog(on_guild_channel_update(client))
class on_guild_channel_update(commands.Cog):
    def __init__(self,client):
        self.client = client   
    @commands.Cog.listener()
    async def on_guild_channel_update(self,before, after):
        channellog = before.guild.get_channel(get.logserveur(id=before.guild.id))
        embed = discord.Embed(
            title =  "Channel Upatade",
            description  =f"""
        <#{after.id}>    
        Nom avant : **``{before.name}``**
        Nom apres : **``{after.name}``**  
        Categorie avant : **``{before.category}``**
        Categorie apres : **``{after.category}``**"""
        )
        await channellog.send(embed = embed)