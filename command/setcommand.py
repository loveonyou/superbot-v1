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
def setup(client):
    client.add_cog(setcommand(client))
class setcommand(commands.Cog):
    def __init__(self,client):
        self.client = client    
    @commands.command()
    async def setcommand(self,ctx, qui = None):    
        if isowner(idowner= ctx.author.id) == True :
            await ctx.message.delete()
            if qui == "wl":
                with open('db/command/command.json', 'r') as f:
                        prefixes = json.load(f)

                prefixes[str(ctx.guild.id)] = "wl"

                with open('db/command/command.json', 'w') as f: 
                        json.dump(prefixes, f, indent=4)
                await ctx.send("les **Whitelist** pouront utilsé tout les command")    
                return
            if qui == "owner":
                with open('db/command/command.json', 'r') as f:
                        prefixes = json.load(f)

                prefixes[str(ctx.guild.id)] = "owner"

                with open('db/command/command.json', 'w') as f: 
                        json.dump(prefixes, f, indent=4)
                await ctx.send("les **Owner** pouront utilsé tout les command")        
                return
            else : 
                await ctx.send("il manque un argument\n> syntax : setcommand <wl/owner>")