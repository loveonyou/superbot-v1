import discord 
from discord.ext import commands, tasks
def setup(client):
    client.add_cog(Ping(client))
class Ping(commands.Cog):
    def __init__(self,client):
        self.client = client    
    @commands.command()
    async def api(self,ctx):    
        

       
       await ctx.send(f"**Super bot Api**\n<:serveur:1050861133545881610> ・ **Statut** : Online\n<:green:1050861218384064572> ・ **Ping** :  {round(self.client.latency *1000)}\n<a:loead:1050861379235622962> ・ discord.gg/protect")
