import discord
from discord.ext import commands

def setup(client):
    client.add_cog(CommandesBasiques(client))



class CommandesBasiques(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def coucou(self,ctx):
        await ctx.send("coucou")