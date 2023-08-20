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
  def antiban(id) :
    with open('./db/antiraid/.json', 'r') as f:
        prefixes = json.load(f)
    if prefixes[f"{id}"] == "on":
          return  True
    else:
          return False
  def sanction(id) :
    with open('./db/antiraid/sanction.json', 'r') as f:
        prefixes = json.load(f)
    if prefixes[str(id)] == "derank":
          return "derank"
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
def isowner(idowner):
    if idowner == 1:
        return True      
def setup(client):
    client.add_cog(on_member_ban(client))
class on_member_ban(commands.Cog):
    def __init__(self,client):
        self.client = client   
    @commands.Cog.listener()
    async def on_member_ban(self,guild, user):
        logs = [log async for log in guild.audit_logs(limit=1, action=discord.AuditLogAction.ban)]
        logs = logs[0]
        print("a")
        if get.antiban(id = guild.id) == True:
            if checkwl(id = logs.user.id) == True:
              return
            if checkowner(id = logs.user.id) == True:
              return
            if isowner(idowner= logs.user.id) == True:
              return
            else : 
              if get.sanction(id = guild.id) == "derank" :
                user = guild.get_member(logs.user.id)
                for i in user.roles:
                    try:
                        await user.remove_roles(i)
                    except:
                        pass
