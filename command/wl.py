import discord
from discord.ext import commands
import time
import datetime
import json
datebot = "lifetime"
oauth = "https://discord.com/api/oauth2/authorize?client_id=1034818686705479690&permissions=8&scope=bot"
cerdit = "Super Bot "
type  =  "Gestion v1"
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
def isowner(idowner):
    if idowner == 1028011304729968740:
        return True
def setup(client):
    client.add_cog(wl(client))
class wl(commands.Cog):
    def __init__(self,client):
        self.client = client  
    @commands.command()
    async def wl(self, ctx, fonction= None, u: discord.Member = None):
            if checkowner(id = ctx.author.id) == True :
                await ctx.message.delete()
                if fonction == "add":
                    with open('./db/wl/wl.json', 'r') as f:
                        prefixes = json.load(f)
                        
                        prefixes['wl'].append(f"{u.id}") 
                        with open('db/wl/wl.json', 'w') as f:
                            json.dump(prefixes, f, indent=4)
                        
                        await ctx.send(f"{u.name} a été ajouter a la whitelist")
                        return
                if fonction == "list" :
                    with open('./db/wl/wl.json', 'r') as f:
                        prefixes = json.load(f)
                        lenwl = len(prefixes['wl'])
                    embedlist = discord.Embed(
                        title = "Wl list",
                        description = ""
                    )   
                    wllen = -1
                    for i in range(0,lenwl):
                        wllen + 1   
                        wluser = prefixes['wl'][wllen]
                        embedlist.add_field(name =f"*id : {wluser}*",value = f"> <@{wluser}>", inline = False)

                    await ctx.send(embed = embedlist)
                    return
                            
                if fonction == "remove":
                    with open('db/wl/wl.json', 'r') as f:
                        file = json.load(f)
                        
                        file['wl'].remove(f"{u.id}")  
                        with open('db/wl/wl.json', 'w') as f:
                            json.dump(file, f, indent=4)
                        await ctx.send(f"{u.name} n'est plus whitelist")
                        return
                else :
                    embed = discord.Embed(
                    title = "Argument invalide",
                    description = "Synthax: **``wl <add/remove/list> <@user>``**",
                    color = 0xFF0000
                    )
                    await ctx.send(embed= embed)
                    return
            else :
                    await ctx.send("Tu n'est pas owner tu ne peux pas utilser cette command ")