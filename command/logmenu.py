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
    client.add_cog(logmenu(client))
from accet.accet import anti, get

    
class logmenu(commands.Cog):
    def __init__(self,client):
        self.client = client    
    @commands.command()    
    async def logmenu(self,ctx):    
        if get.owner( id = ctx.author.id) == True :
            try :
                logsmessageidfind = get.logmessage(id = ctx.guild.id)
                logsmessageid = (f"<#{logsmessageidfind}>")
            except : 
                logsmessageid = "none"      
            try :
                logsroleidfind = get.logrole(id = ctx.guild.id)
                logsroleid = (f"<#{logsroleidfind}>")          
            except :      
                    logsroleid = "none"
            try :
                logsserveuridfind = get.logrole(id = ctx.guild.id)
                logsserveurid = (f"<#{logsserveuridfind}>")          
            except :      
                    logsserveurid = "none"                
            
            logmessage = logsmessageid
            logrole = logsroleid
            logserveur = logsserveurid
            embed = discord.Embed(
                title = f"📁 ・ Logs de {ctx.guild.name} ",
                description = f"""
        💬 ・ **Logs Message**
        ``Messages edit, Messages Suprimer, Antilink,``
        > {logmessage}
        🎭 ・ **Logs Roles**
        ``Roles crée, Roles Suprimer, Roles ajouter/retire, Reles Modifier``
        > {logrole}
        👑 ・ **Logs Serveur** 
        ``Profiles du serveur Modifier(avatar, nom, bannier,ext), vanity changer``       
        > {logserveur}
        ❌ ・ **Close**
        ``pour close le menu``
                """
            )
            embed.set_author(
                    name= ctx.message.author.name,
                    icon_url = ctx.message.author.avatar_url
            )
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer( text = f" {cerdit} \u200b ")
            message = await ctx.send(embed= embed)
            await message.add_reaction("💬")
            await message.add_reaction("🎭")
            await message.add_reaction("👑")
            await message.add_reaction("❌")
            def check(reaction, user):
                            return user == ctx.author and str(reaction.emoji) in ["💬", "🎭","👑","❌"]
            def checka(message):
                        return message.author == ctx.author and message.channel == ctx.channel
            while True:
                        try:
                            reaction, user = await self.client.wait_for("reaction_add", check=check)

                            if str(reaction.emoji) == "💬":
                                    embedmessage =  discord.Embed(
                                            title = "💬 ・ **Logs Message**",
                                            description= f"Channel actuel {logmessage}\n"
                                    )
                                    embedmessage.set_author(
                                            name= ctx.message.author.name,
                                            icon_url = ctx.message.author.avatar_url
                                    )
                                    embedmessage.timestamp = datetime.datetime.utcnow()
                                    embedmessage.set_footer( text = f" {cerdit} \u200b ")                          
                                    embedchange =await ctx.send(embed = embedmessage)                  
                                    messagechange = await ctx.send("Par qu'elle channel veux tu le changer(id)")
                                    channelmessage = await self.client.wait_for('message', check=checka)
                                    with open('db/logs/message.json', 'r') as f:
                                        prefixes = json.load(f)

                                    prefixes[str(ctx.guild.id)] = channelmessage.content

                                    with open('db/logs/message.json', 'w') as f: 
                                        json.dump(prefixes, f, indent=4)
                                    await messagechange.delete()
                                    await embedchange.delete()
                                    await channelmessage.delete()
                                    await message.remove_reaction(reaction, user)
                            if str(reaction.emoji) == "🎭":
                                    embedrole =  discord.Embed(
                                            title = "🎭 ・ **Logs Role**",
                                            description= f"Channel actuel {logrole}\n"
                                    )
                                    embedrole.set_author(
                                            name= ctx.message.author.name,
                                            icon_url = ctx.message.author.avatar_url
                                    )
                                    embedrole.timestamp = datetime.datetime.utcnow()
                                    embedrole.set_footer( text = f" {cerdit} \u200b ")                          
                                    embedchange =await ctx.send(embed = embedrole)                  
                                    rolechange = await ctx.send("Par qu'elle channel veux tu le changer(id)")
                                    channelrole = await self.client.wait_for('message', check=checka)
                                    with open('db/logs/role.json', 'r') as f:
                                        prefixes = json.load(f)

                                    prefixes[str(ctx.guild.id)] = channelrole.content

                                    with open('db/logs/role.json', 'w') as f: 
                                        json.dump(prefixes, f, indent=4)
                                    await rolechange.delete()
                                    await embedchange.delete()
                                    await channelrole.delete()
                                    await message.remove_reaction(reaction, user)
                            if str(reaction.emoji) == "👑":
                                    embedserveur =  discord.Embed(
                                            title = "👑 ・ **Logs serveur**",
                                            description= f"Channel actuel {logserveur}\n"
                                    )
                                    embedserveur.set_author(
                                            name= ctx.message.author.name,
                                            icon_url = ctx.message.author.avatar_url
                                    )
                                    embedserveur.timestamp = datetime.datetime.utcnow()
                                    embedserveur.set_footer( text = f" {cerdit} \u200b ")                          
                                    embedserveur =await ctx.send(embed = embedserveur)                  
                                    serveurchange = await ctx.send("Par qu'elle channel veux tu le changer(id)")
                                    channelserveur = await self.client.wait_for('message', check=checka)
                                    with open('db/logs/serveur.json', 'r') as f:
                                        prefixes = json.load(f)

                                    prefixes[str(ctx.guild.id)] = channelserveur.content

                                    with open('db/logs/role.json', 'w') as f: 
                                        json.dump(prefixes, f, indent=4)
                                    await serveurchange.delete()
                                    await embedserveur.delete()
                                    await channelserveur.delete()
                                    await message.remove_reaction(reaction, user)
                            if str(reaction.emoji) == "❌":
                                    await message.edit(content  = "Logmenu close")
                                    time.sleep(5)
                                    await message.delete()

                        except:
                            
                            break