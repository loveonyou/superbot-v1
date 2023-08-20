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
  def antichannel(id):
    with open('./db/antiraid/channel.json', 'r') as f:
      prefixes = json.load(f)
    if prefixes[f"{id}"] == "on":
        return  True
    else:
        return False
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
    client.add_cog(on_guild_channel_delete(client))
class on_guild_channel_delete(commands.Cog):
    def __init__(self,client):
        self.client = client   
    @commands.Cog.listener()
    async def on_guild_channel_delete(self,channel):
        if get.antichannel(id = channel.guild.id) == True:
            channelp =  channel.position
            channelc = channel.category 
            with open('db/antiraid/channel.json', 'r') as f:
                    prefixes = json.load(f)

            prefixes[str(channel.guild.id)] = "off"

            with open('db/antiraid/channel.json', 'w') as f: 
                        json.dump(prefixes, f, indent=4)
            await channel.guild.create_text_channel(f"{channel.name}", category=channelc,position=channelp)
            with open('db/antiraid/channel.json', 'r') as f:
                prefixes = json.load(f)

            prefixes[str(channel.guild.id)] = "on"
            with open('db/antiraid/channel.json', 'w') as f: 
                            json.dump(prefixes, f, indent=4)            
            return
        else :
            channellog = channel.guild.get_channel(get.logserveur(id=channel.guild.id))
            channeln = channel.name
            channelcd = datetime.datetime.utcnow()
            embed2 = discord.Embed(
                title="Channel Suprimer",
                description=f"{channeln} a été crée le **``{channel.created_at.strftime('%Y-%m-%d')}``** \n suprimé le **``{channelcd.strftime('%Y-%m-%d')}``** ",
                color=0x0000FF)
            embed2.timestamp = datetime.datetime.utcnow()
            await channellog.send(embed=embed2)