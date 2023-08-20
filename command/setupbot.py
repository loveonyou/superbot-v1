import discord
from discord.ext import commands
import time
import datetime
import json
datebot = "lifetime"
oauth = "https://discord.com/api/oauth2/authorize?client_id=1034818686705479690&permissions=8&scope=bot"
cerdit = "Super Bot "
type  =  "Gestion v1"
def setup(client):
    client.add_cog(autosetup(client))
class autosetup(commands.Cog):
    def __init__(self,client):
        self.client = client  
    @commands.command()
    async def setupbot(self, ctx):
        with open('db/antiraid/antilink.json', 'r') as f:
            anti_link = json.load(f)

            anti_link[str(ctx.guild.id)] = "off"

        with open('db/antiraid/antilink.json', 'w') as f: 
            json.dump(anti_link, f, indent=4)
        # with open('db/antiraid/antieveryone.json', 'r') as a:
        #     anti_everyone = json.load(a)

        #     anti_everyone[str(ctx.guild.id)] = "off"

        # with open('db/antiraid/antieveryone.json', 'w') as a: 
        #     json.dump(anti_everyone, a, indent=4)
        with open('db/antiraid/channel.json', 'r') as f:
            anti_channel = json.load(f)

            anti_channel[str(ctx.guild.id)] = "off"

        with open('db/antiraid/channel.json', 'w') as f: 
            json.dump(anti_channel, f, indent=4)
        with open('db/logs/message.json', 'r') as f:
            logs_message = json.load(f)

            logs_message[str(ctx.guild.id)] = "none"

        with open('db/logs/message.json', 'w') as f: 
            json.dump(logs_message, f, indent=4)
        with open('db/logs/role.json', 'r') as f:
            logs_role = json.load(f)

            logs_role[str(ctx.guild.id)] = "none"

        with open('db/logs/role.json', 'w') as f: 
            json.dump(logs_role, f, indent=4)
        with open('db/logs/serveur.json', 'r') as f:
            logs_serveur = json.load(f)

            logs_serveur[str(ctx.guild.id)] = "none"

        with open('db/logs/role.json', 'w') as f: 
            json.dump(logs_serveur, f, indent=4)
        await ctx.send("**Bot setup**")                            

    