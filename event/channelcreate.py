import discord
from discord.ext import commands
import time
import datetime
import json
from accet.accet import get, anti
datebot = "lifetime"
oauth = "https://discord.com/api/oauth2/authorize?client_id=1034818686705479690&permissions=8&scope=bot"
cerdit = "Super Bot "
type  =  "Gestion v1"
def setup(client):
    client.add_cog(Eventchannelcreate(client))
class Eventchannelcreate(commands.Cog):
    def __init__(self,client):
        self.client = client   
    @commands.Cog.listener()
    async def on_guild_channel_create(self,channel):
        logs = [log async for log in channel.guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_create)]
        logs = logs[0]
        embedv = discord.Embed(
          Title = "Channel Créer",
          description = f"""
          **Channel Créer par ** <@{logs.user.id}>
          > Channel : <#{channel.id}>
          > date :**``{datetime.datetime.utcnow().date()}``**""",
          color = logs.user.color
        )
        embedv.set_author(icon_url= logs.user.avatar_url, name = logs.user.name)
        await channel.send(embed= embedv)
        if anti.channel(id = channel.guild.id) == True:
          #if get.isowner(id = logs.user.id) == True:
          #  print("a") 

          if get.owner(id = logs.user.id ) == True:
            print("a")
          if get.wl(id = logs.user.id) == True:
            print("a")
          else :
              if get.sanction(id = channel.guild.id) == "derank" :
                user = channel.guild.get_member(logs.user.id)
                for i in user.roles:
                    try:
                        await user.remove_roles(i)
                    except:
                        pass
