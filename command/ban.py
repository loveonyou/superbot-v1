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
    client.add_cog(ban(client))
class ban(commands.Cog):
    def __init__(self,client):
        self.client = client  
    @commands.command()
    async def ban(self,ctx ,user : discord.Member  = None, reason = None):
        if get.owner(id = ctx.author.id) == True:
            if ctx.author.guild_permissions.ban_members == True:
                try :
                    await user.ban(reason =reason)
                except:
                    await ctx.send(f"je n'ai aps reussi a ban {user.name}")
                    return
                if reason == None:
                        reason = "raison non spécifier." 
                await ctx.message.delete()
                try: 
                    await user.send(f"tu a été bannis du \n**server : {ctx.guild.name}**\n**raison :** {reason}")
                except :
                    pass
                await ctx.send(f"{user.name} a été ban du server {ctx.guild.name} avec **success**")
                return
            else:
                await ctx.send("**tu na pas les permisisons  requise pour ban! **")
            