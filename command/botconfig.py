import discord
from discord.ext import commands
import time
import datetime
import json
from accet.accet import anti, get
datebot = "lifetime"
oauth = "https://discord.com/api/oauth2/authorize?client_id=1034818686705479690&permissions=8&scope=bot"
cerdit = "Super Bot "
type  =  "Gestion v1"
def setup(client):
    client.add_cog(botconfig(client))
class botconfig(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def botconfig(self,ctx):
        if get.owner( id = ctx.author.id ) == True :    
            await ctx.message.delete()  
            embed= discord.Embed(
                title ="Botconfig",
                description = f"""
        :one: = **botsetname** 
        ``Permet de changer le nom de ton bot``
        :two: = **bot Activity**
        ``Permet de change le l'Activité du bot ``
        :three: =  **Theme**
        ``Permet de change le theme du bot (couleur)``
        """
            ) 
            embed.set_author(
                name= ctx.message.author.name,
                icon_url = ctx.message.author.avatar_url
            )
            embed.set_thumbnail(url = self.client.user.avatar_url)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer( text = f" {cerdit} \u200b ")
            message =  await ctx.send(embed = embed)
            await message.add_reaction("1️⃣")
            await message.add_reaction("2️⃣")
            await message.add_reaction("3️⃣")
            await message.add_reaction("❌")
            def check(reaction, user):
                        return user == str(reaction.emoji) in ["1️⃣", "2️⃣","3️⃣","4️⃣","❌"]
            def checka(message):
                    return message.author == ctx.author and message.channel == ctx.channel
            while True:
                        try:
                            reaction, user = await self.client.wait_for("reaction_add", check=check)

                            if str(reaction.emoji) == "1️⃣":
                                tt =await ctx.send("Qu'elle est nom du bot")
                                name = await self.client.wait_for('message', check=checka)
                                try :
                                    await  self.client.user.edit(username  = name.content)
                                    await name.delete()
                                    await tt.delete()
                                    a = await ctx.send("Mon nom a bien été mis a jour !") 
                                    time.sleep(3)
                                    await a.delete()
                                except:
                                    error = await ctx.send("Je ne peux plus changer de nom veuillez ressayer dans 20 minutes")
                                    time.sleep(3)
                                    await error.delete()
                                await message.remove_reaction(reaction, user)

                            elif str(reaction.emoji) == "2️⃣":
                                acti1 = await ctx.send("Qu'elle est la nouvelles activiter du bot(stream,joue,regarde)")  
                                acti = await self.client.wait_for('message', check=checka)
                                await acti1.delete() 
                                await acti.delete()
                                if acti.content == "stream":
                                    aac = await ctx.send("Que dois-je stream ")
                                    a = await self.client.wait_for('message', check=checka)
                                    await aac.delete()
                                    await a.delete()
                                    game = discord.Streaming(name=f"{a.content}",
                                        url='https://twitch.tv/abcdefg')
                                    await self.client.change_presence(status=discord.Status.online, activity=game)
                                    ac1 =await ctx.send(f"Activiter changer pour  :  stream **{a.content}**")
                                    time.sleep(3)
                                    await ac1.delete()
                                if acti.content == "joue":
                                    aab = await ctx.send("a quoi dois-je jouer  ")
                                    aabc = await self.client.wait_for('message', check=checka)
                                    await aab.delete()
                                    await aabc.delete()
                                    game = discord.Game(name=f"{aabc.content}")
                                    await self.client.change_presence(status=discord.Status.online, activity=game)
                                    ac2 = await ctx.send(f"Activiter  changer pour  :  joue a **{aabc.content}**")
                                    time.sleep(3)
                                    await ac2.delete()
                                await message.edit(embed=embed)
                                await message.remove_reaction(reaction, user)
                                if acti.content == "regarde":
                                    regarde1 = await ctx.send("Que dois-je regarder ?")
                                    regarde = await self.client.wait_for('message', check=checka)
                                    await regarde1.delete()
                                    await regarde.delete() 
                                    await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= regarde.content))
                                    ac3 = await ctx.send(f"Activiter changer pour  : Regarde **{regarde.content}** ")
                                    time.sleep(3)
                                    await ac3.delete()
                            elif str(reaction.emoji) == "3️⃣":
                                    embedcoleur = discord.Embed(
                                        title = "Theme Du bot",
                                        description ="🟢 : ``Vert``\n🔴: ``Rouge``\n🔵 : ``Bleu``"
                                    )
                                    embedcoleur.set_author(
                                        name= ctx.message.author.name,
                                        icon_url = ctx.message.author.avatar_url
                                    )
                                    embedcoleur.timestamp = datetime.datetime.utcnow()
                                    embedcoleur.set_footer( text = f" {cerdit} \u200b ")
                                    messagecouleur =  await ctx.send(embed = embedcoleur)
                                    await messagecouleur.add_reaction("🟢")
                                    await messagecouleur.add_reaction("🔴")
                                    await messagecouleur.add_reaction("🔵")
                                    def check(reaction, user):
                                        return user == ctx.author and str(reaction.emoji) in ["🔵", "🔴","🟢","❌"]
                                    while True:
                                        try:
                                            reaction, user = await self.client.wait_for("reaction_add", check=check)
                                            if str(reaction.emoji) == "🟢":
                                                    with open('prefixes.json', 'r') as f:
                                                        colorvert = json.load(f)

                                                        #colorvert[str(ctx.guild.id)] = prefix

                                                        #with open('prefixes.json', 'w') as f: 
                                                        #    json.dump(prefixes, f, indent=4)
                                        except:
                                            break
                            elif str(reaction.emoji) == "❌":
                                await message.edit(content = "Ton bot config  va être close")
                                time.sleep(5)
                                await message.delete()
                                return
                            else:
                                await message.remove_reaction(reaction, user)

                        except:
                            break    