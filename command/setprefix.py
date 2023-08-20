import discord 
from discord.ext import commands, tasks
import json
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
def getprefix(id):
        with open('./db/command/prefix.json', 'r') as f:
            prefixes = json.load(f)

            prefixr = prefixes[str(id.guild.id)] 
            return prefixr
def setup(client):
    client.add_cog(setprefix(client))
class setprefix(commands.Cog):
    def __init__(self,client):
        self.client = client    
    @commands.command()
    async def setprefix(self,ctx, prefix = None):   
        if checkowner(id = ctx.author.id) == True:
            await ctx.message.delete()
            if prefix != None :
                with open('./db/command/prefix.json', 'r') as f:
                    prefixes = json.load(f)

                    prefixes[str(ctx.guild.id)] = prefix

                with open('./db/command/prefix.json', 'w') as f: 
                    json.dump(prefixes, f, indent=4)
                await ctx.send(f"prefixe changer par  : ``{prefix}``")
            else: 
                await ctx.send("veuillez spécifier un prefix\n> ")