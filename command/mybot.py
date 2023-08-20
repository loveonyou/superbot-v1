import discord
from discord.ext import commands
import time
import datetime
import json
import calendar
datebot = datetime.date(2022,12,22)
oauth = "https://discord.com/api/oauth2/authorize?client_id=1034818686705479690&permissions=8&scope=bot"
cerdit = "Super Bot "
type  =  "Gestion v1"
from accet.accet import anti, get
def setup(client):
    client.add_cog(botconfig(client))



class botconfig(commands.Cog):
    def __init__(self, client):
        self.client = client    
    @commands.command()
    async def mybot(self,ctx):
        await ctx.message.delete()
        if get.owner(id = ctx.author.id) == True :
            ajd = datetime.date.today()
            ajd.strftime('%Y-%m-%d')
            if datebot == "lifetime":
                jours = "lifetime"
            if not datebot == "lifetime":
                args = ajd - datebot
            
            embed = discord.Embed(
            title = self.client.user.name,
            description = f"**Temps Restant ** : {args.days} jours \n> **type** : {type}",
            url = oauth
            )
            embed.set_author(
            name = ctx.author.name,
            icon_url= ctx.author.avatar_url
            )
            await ctx.send(embed= embed)
        else : 
                await ctx.send("vous n'avez pas la permision de utilser cette command")