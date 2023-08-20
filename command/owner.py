import discord
from discord.ext import commands
import time
import datetime
import json
datebot = "lifetime"
oauth = "https://discord.com/api/oauth2/authorize?client_id=1034818686705479690&permissions=8&scope=bot"
cerdit = "Super Bot "
type  =  "Gestion v1"
from accet.accet import anti, get
def setup(client):
    client.add_cog(owner(client))
class owner(commands.Cog):
    def __init__(self,client):
        self.client = client  
    @commands.command()
    async def owner(self,ctx, fonction= None, user: discord.Member = None):
        await ctx.message.delete()
        if get.isowner(idowner = ctx.message.author.id) == True:
            if fonction == "add":
                with open('db/wl/owner.json', 'r') as f:
                    prefixes = json.load(f)
                
                prefixes['owner'].append(f"{user.id}")

                with open('db/wl/owner.json', 'w') as f:
                    json.dump(prefixes, f, indent=4)
                await ctx.send(f"{user.name} a été ajouter a la list des owner")
                return
            #if fonction == "list" :
            #    with open('db/wl/wl.json', 'r') as f:
            #        prefixes = json.load(f)
            #        id[""] = prefixes
            #    await ctx.send(id)
            if fonction == "remove":
                with open('db/wl/owner.json', 'r') as f:
                    file = json.load(f)

                file['owner'].remove(f"{user.id}")  
                with open('db/wl/owner.json', 'w') as f:
                    json.dump(file, f, indent=4)
                await ctx.send(f"{user.name} n'est plus owner")
                return
            else :
                embed = discord.Embed(
                title = "Argument invalide",
                description = "Synthax: **``owner <add/remove/list> <@user>``**",
                color = 0xFF0000
                )
                await ctx.send(embed= embed)
                return
        if not get.isowner(idowner = ctx.message.author.id) == True:
            await ctx.send("Tu n'est pas owner tu ne peux pas utilse cette command")