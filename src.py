import discord
from discord.ext import commands, tasks
from discord.utils import get
from discord import Webhook, RequestsWebhookAdapter
from discord_slash import ButtonStyle, SlashCommand
from discord_slash.utils.manage_components import *
import os
import time
import json
import datetime
datebot = "lifetime"
oauth = "https://discord.com/api/oauth2/authorize?client_id=1034818686705479690&permissions=8&scope=bot"
cerdit = "Super Bot "
type  =  "Gestion v1"
intents = discord.Intents.all()
color = "FF0000"
client = commands.Bot(command_prefix="+", self_bot = False, help_command= None, intents=intents)
class get():
    def logmessage(id): 
        with open('db/logs/message.json', 'r') as f: 
            prefixes = json.load(f) 
            return int(prefixes[str(id)])    
    def logrole(id): 
        with open('db/logs/role.json', 'r') as f: 
            prefixes = json.load(f) 
            return int(prefixes[str(id)]) 
    def logserveur(id): 
        with open('db/logs/serveur.json', 'r') as f: 
            prefixes = json.load(f) 
            return int(prefixes[str(id)]) 
def checkwl(id):
    with open('db/wl/wl.json', 'r') as f:
      prefixes = json.load(f)
      
      if prefixes[str(id)] == str("wl"):
        return True
      if not prefixes[str(id)] == str("wl"):
        return False
def checkowner(id):
    with open('db/wl/owner.json', 'r') as f:
      prefixes = json.load(f)
      
      if prefixes[str(id)] == str("owner"):
        return True
      if not prefixes[str(id)] == str("owner"):
        return False        
def isowner(idowner):
    if idowner == 1002177532730290258:
        return True


@client.event
async def on_ready():
    print(f"Le bot est on\nInfo\n id = {client.user.id}\n name = {client.user.name}")
@client.command()
async def ping(ctx):
    await ctx.reply(content= f"**Pong*")
class menu:
    @client.command()
    async def botconfig(ctx):
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
            embed.set_thumbnail(url = client.user.avatar_url)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer( text = f" {cerdit} \u200b ")
            message =  await ctx.send(embed = embed)
            await message.add_reaction("1️⃣")
            await message.add_reaction("2️⃣")
            await message.add_reaction("3️⃣")
            await message.add_reaction("❌")
            def check(reaction, user):
                        return user == ctx.author and str(reaction.emoji) in ["1️⃣", "2️⃣","3️⃣","4️⃣","❌"]
            def checka(message):
                    return message.author == ctx.author and message.channel == ctx.channel
            while True:
                        try:
                            reaction, user = await client.wait_for("reaction_add", check=check)

                            if str(reaction.emoji) == "1️⃣":
                                tt =await ctx.send("Qu'elle est nom du bot")
                                name = await client.wait_for('message', check=checka)
                                await  client.user.edit(username  = name.content)
                                await name.delete()
                                await tt.delete()
                                a = await ctx.send("Mon nom a bien été mis a jour !") 
                                time.sleep(3)
                                await a.delete()
                                await message.remove_reaction(reaction, user)

                            elif str(reaction.emoji) == "2️⃣":
                                acti1 = await ctx.send("Qu'elle est la nouvelles activiter du bot(stream,joue,regarde)")  
                                acti = await client.wait_for('message', check=checka)
                                await acti1.delete() 
                                await acti.delete()
                                if acti.content == "stream":
                                    aac = await ctx.send("Que dois-je stream ")
                                    a = await client.wait_for('message', check=checka)
                                    await aac.delete()
                                    await a.delete()
                                    game = discord.Streaming(name=f"{a.content}",
                                        url='https://twitch.tv/abcdefg')
                                    await client.change_presence(status=discord.Status.online, activity=game)
                                    ac1 =await ctx.send(f"Activiter changer pour  :  stream **{a.content}**")
                                    time.sleep(3)
                                    await ac1.delete()
                                if acti.content == "joue":
                                    aab = await ctx.send("a quoi dois-je jouer  ")
                                    aabc = await client.wait_for('message', check=checka)
                                    await aab.delete()
                                    await aabc.delete()
                                    game = discord.Game(name=f"{aabc.content}")
                                    await client.change_presence(status=discord.Status.online, activity=game)
                                    ac2 = await ctx.send(f"Activiter  changer pour  :  joue a **{aabc.content}**")
                                    time.sleep(3)
                                    await ac2.delete()
                                await message.edit(embed=embed)
                                await message.remove_reaction(reaction, user)
                                if acti.content == "regarde":
                                    regarde1 = await ctx.send("Que dois-je regarder ?")
                                    regarde = await client.wait_for('message', check=checka)
                                    await regarde1.delete()
                                    await regarde.delete() 
                                    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= regarde.content))
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
                                            reaction, user = await client.wait_for("reaction_add", check=check)
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
    # @client.command()
    # async def logmenu(ctx):    
    #     try :
    #         logsmessageidfind = get.logmessage(id = ctx.guild.id)
    #         logsmessageid = (f"<#{logsmessageidfind}>")
    #     except : 
    #         logsmessageid = "none"      
    #     try :
    #         logsroleidfind = get.logrole(id = ctx.guild.id)
    #         logsroleid = (f"<#{logsroleidfind}>")          
    #     except :      
    #             logsroleid = "none"
    #     try :
    #         logsserveuridfind = get.logrole(id = ctx.guild.id)
    #         logsserveurid = (f"<#{logsserveuridfind}>")          
    #     except :      
    #             logsserveurid = "none"                
        
    #     logmessage = logsmessageid
    #     logrole = logsroleid
    #     logserveur = logsserveurid
    #     embed = discord.Embed(
    #         title = f"📁 ・ Logs de {ctx.guild.name} ",
    #         description = f"""
    # 💬 ・ **Logs Message**
    # ``Messages edit, Messages Suprimer, Antilink,``
    # > {logmessage}
    # 🎭 ・ **Logs Roles**
    # ``Roles crée, Roles Suprimer, Roles ajouter/retire, Reles Modifier``
    # > {logrole}
    # 👑 ・ **Logs Serveur** 
    # ``Profiles du serveur Modifier(avatar, nom, bannier,ext), vanity changer``       
    # > {logserveur}
    # ❌ ・ **Close**
    # ``pour close le menu``
    #         """
    #     )
    #     embed.set_author(
    #             name= ctx.message.author.name,
    #             icon_url = ctx.message.author.avatar_url
    #     )
    #     embed.timestamp = datetime.datetime.utcnow()
    #     embed.set_footer( text = f" {cerdit} \u200b ")
    #     message = await ctx.send(embed= embed)
    #     await message.add_reaction("💬")
    #     await message.add_reaction("🎭")
    #     await message.add_reaction("👑")
    #     await message.add_reaction("❌")
    #     def check(reaction, user):
    #                     return user == ctx.author and str(reaction.emoji) in ["💬", "🎭","👑","❌"]
    #     def checka(message):
    #                 return message.author == ctx.author and message.channel == ctx.channel
    #     while True:
    #                 try:
    #                     reaction, user = await client.wait_for("reaction_add", check=check)

    #                     if str(reaction.emoji) == "💬":
    #                             embedmessage =  discord.Embed(
    #                                     title = "💬 ・ **Logs Message**",
    #                                     description= f"Channel actuel {logmessage}\n"
    #                             )
    #                             embedmessage.set_author(
    #                                     name= ctx.message.author.name,
    #                                     icon_url = ctx.message.author.avatar_url
    #                             )
    #                             embedmessage.timestamp = datetime.datetime.utcnow()
    #                             embedmessage.set_footer( text = f" {cerdit} \u200b ")                          
    #                             embedchange =await ctx.send(embed = embedmessage)                  
    #                             messagechange = await ctx.send("Par qu'elle channel veux tu le changer(id)")
    #                             channelmessage = await client.wait_for('message', check=checka)
    #                             with open('db/logs/message.json', 'r') as f:
    #                                 prefixes = json.load(f)

    #                             prefixes[str(ctx.guild.id)] = channelmessage.content

    #                             with open('db/logs/message.json', 'w') as f: 
    #                                 json.dump(prefixes, f, indent=4)
    #                             await messagechange.delete()
    #                             await embedchange.delete()
    #                             await channelmessage.delete()
    #                             await message.remove_reaction(reaction, user)
    #                     if str(reaction.emoji) == "🎭":
    #                             embedrole =  discord.Embed(
    #                                     title = "🎭 ・ **Logs Role**",
    #                                     description= f"Channel actuel {logrole}\n"
    #                             )
    #                             embedrole.set_author(
    #                                     name= ctx.message.author.name,
    #                                     icon_url = ctx.message.author.avatar_url
    #                             )
    #                             embedrole.timestamp = datetime.datetime.utcnow()
    #                             embedrole.set_footer( text = f" {cerdit} \u200b ")                          
    #                             embedchange =await ctx.send(embed = embedrole)                  
    #                             rolechange = await ctx.send("Par qu'elle channel veux tu le changer(id)")
    #                             channelrole = await client.wait_for('message', check=checka)
    #                             with open('db/logs/role.json', 'r') as f:
    #                                 prefixes = json.load(f)

    #                             prefixes[str(ctx.guild.id)] = channelrole.content

    #                             with open('db/logs/role.json', 'w') as f: 
    #                                 json.dump(prefixes, f, indent=4)
    #                             await rolechange.delete()
    #                             await embedchange.delete()
    #                             await channelrole.delete()
    #                             await message.remove_reaction(reaction, user)
    #                     if str(reaction.emoji) == "👑":
    #                             embedserveur =  discord.Embed(
    #                                     title = "👑 ・ **Logs serveur**",
    #                                     description= f"Channel actuel {logserveur}\n"
    #                             )
    #                             embedserveur.set_author(
    #                                     name= ctx.message.author.name,
    #                                     icon_url = ctx.message.author.avatar_url
    #                             )
    #                             embedserveur.timestamp = datetime.datetime.utcnow()
    #                             embedserveur.set_footer( text = f" {cerdit} \u200b ")                          
    #                             embedserveur =await ctx.send(embed = embedserveur)                  
    #                             serveurchange = await ctx.send("Par qu'elle channel veux tu le changer(id)")
    #                             channelserveur = await client.wait_for('message', check=checka)
    #                             with open('db/logs/serveur.json', 'r') as f:
    #                                 prefixes = json.load(f)

    #                             prefixes[str(ctx.guild.id)] = channelserveur.content

    #                             with open('db/logs/role.json', 'w') as f: 
    #                                 json.dump(prefixes, f, indent=4)
    #                             await serveurchange.delete()
    #                             await embedserveur.delete()
    #                             await channelserveur.delete()
    #                             await message.remove_reaction(reaction, user)
    #                     if str(reaction.emoji) == "❌":
    #                             await message.edit(content  = "Logmenu close")
    #                             time.sleep(5)
    #                             await message.delete()

    #                 except:
                        
    #                     break  w²
    @client.command()
    async def embed(ctx):
        titreembed = "titre tempo&"
        descriptionembed = ""
        imageembed = ""
        footerembed =  ""
        autheurembed = ["",""]
        coleur = ""
        timeembed =  False
        embedmenu = discord.Embed(
            title = "Embed Builder",
            description = ""
        )
        embedmenu.add_field(
            name= "🖊 ・ Title",
            value= "``ajoute un titre a l'embed``"
            
        )
        embedmenu.add_field(
            name= "📃 ・ Description",
            value= "``ajoute une description a l'embed``"
            
        )    
        embedmenu.add_field(
            name= "🖼 ・ Image",
            value= "``ajoute un image a l'embed``"
            
        ) 
        embedmenu.add_field(
            name= "🪧 ・ Footer",
            value= "``ajoute un footer a l'embed``"
            
        )
        embedmenu.add_field(
            name= "🚹 ・ autheur",
            value= "``ajoute un autheur a l'embed``"
            
        )                           
        embedmenu.add_field(
            name= "🟢 ・ couleur",
            value= "``ajoute une couleur a l'embed``"
            
        )         
        embedmenu.add_field(
            name= "⏰ ・ timeembed",
            value= "``ajouter une timestamp``"
            
        )
        embedmenu.add_field(
            name= "💭 ・ Envoyer ",
            value= "``Permet d'envoyer l'embed``"
            
        )
        embedmenu.add_field(
            name= "❌ ・ Annuler ",
            value= "``Pour annuler la command embed``"
            
        )    
        embedmenu.timestamp = datetime.datetime.utcnow()
        embedmenu.set_footer( text = f" {cerdit} \u200b ")
        message = await ctx.send(embed= embedmenu)
        embed = discord.Embed(
            title = titreembed,
            description = descriptionembed
        )
        embededit = await ctx.send(embed= embed)
        await message.add_reaction("🖊")
        await message.add_reaction("📃")
        await message.add_reaction("🖼")   
        await message.add_reaction("🪧")   
        await message.add_reaction("🚹")   
        await message.add_reaction("🟢")   
        await message.add_reaction("⏰")  
        await message.add_reaction("💭")    
        await message.add_reaction("❌")                 
        def check(reaction, user):
                        return user == ctx.author and str(reaction.emoji) in ["🖊", "📃","🖼","🪧","🚹","🟢","⏰","💭","❌"]
        def checka(message):
                    return message.author == ctx.author and message.channel == ctx.channel    
        while True:
                            try:
                                reaction, user = await client.wait_for("reaction_add", check=check)

                                if str(reaction.emoji) == "🖊":
                                    titremessage = await ctx.send("Qu'elle est le titre de l'embed ?")
                                    titrewait = await client.wait_for('message', check=checka)
                                    titreembed = titrewait.content
                                    embed = discord.Embed(
                                        title = titreembed,
                                        description = descriptionembed
                                    )
                                    await embededit.edit(embed = embed) 
                                    await message.remove_reaction(reaction, user)
                                    await titremessage.delete()
                                    await titrewait.delete()
                                elif str(reaction.emoji) == "📃":
                                    descriptionmessage  = await ctx.send("Qu'elle est la description de l'embed")
                                    descriptionwait = await client.wait_for('message', check = checka)
                                    descriptionembed = descriptionwait.content
                                    embed = discord.Embed(
                                        title = titreembed,
                                        description = descriptionembed
                                    )
                                    await embededit.edit(embed = embed)                                 
                                    await descriptionmessage.delete()
                                    await descriptionwait.delete()
                                    await message.remove_reaction(reaction, user)
                                elif str(reaction.emoji) == "🖼":
                                    imagemessage = await ctx.send("Qu'elle est l'image de l'embed(url)")
                                    imagewait = await client.wait_for('message', check =checka)
                                    imageembed = imagewait.content                              
                                    embed.set_image(url= imageembed)
                                    await embededit.edit(embed = embed) 
                                    await imagemessage.delete()
                                    await imagewait.delete()
                                    await message.remove_reaction(reaction, user)
                                elif str(reaction.emoji) == "🪧":
                                    footermessage = await ctx.send("Que dois contenir le footer ? ")
                                    footerwait = await client.wait_for('message',check = checka)
                                    embed.set_footer( text= footerwait.content)
                                    await embededit.edit(embed = embed)
                                    await footermessage.delete()
                                    await footerwait.delete()
                                    await message.remove_reaction(reaction, user)
                                elif str(reaction.emoji) == "🚹":
                                    autheurmessage = await ctx.send("Qu'elle est le nom de l'autheur")
                                    autheurwait = await client.wait_for('message',check = checka)
                                    autheurembed[0] = autheurwait.content
                                    await autheurmessage.delete()
                                    await autheurwait.delete()
                                    avatarmessage = await ctx.send("QU'elle est l'avatar de l'auteur")
                                    avatarwait = await client.wait_for('message',check = checka)
                                    autheurembed[1] = avatarwait.content
                                    await avatarmessage.delete()
                                    await avatarwait.delete()
                                    embed.set_author(
                                        name = autheurembed[0],
                                        icon_url= autheurembed[1]
                                    )
                                    await embededit.edit(embed = embed)
                                    await message.remove_reaction(reaction, user)
                                elif str(reaction.emoji) == "🟢":
                                    #couleurmessage = await ctx.send("Qu'elle est la couleur de l'embed ? (Html color)")
                                    #couleurwait = await client.wait_for('message', check = checka)
                                    #embed = discord.Embed(
                                    #       title = titreembed,
                                    #       description = descriptionembed,
                                    #       color = discord.Color.couleurwait.content
                                    #)
                                    #await embededit.edit(embed = embed)                                                                 
                                    await message.remove_reaction(reaction, user)
                                elif str(reaction.emoji) == "⏰":
                                    if timeembed == True :
                                        t1 =await ctx.send("timestamp désactvier")
                                        time.sleep(3)
                                        await t1.delete()
                                        timeembed = False
                                    if timeembed == False:
                                            t2 =await ctx.send("timestamp activer")    
                                            time.sleep(3)
                                            await t2.delete()
                                            timeembed = True
                                    await message.remove_reaction(reaction, user)   
                                elif str(reaction.emoji) == "💭":
                                    sendmessage = await ctx.send("Qu'elle est le channel ou vous voulez envoyer l'embed(ID)")
                                    sendwait = await client.wait_for('message', check= checka)
                                    channel = ctx.guild.get_channel(int(sendwait.content))
                                    if timeembed == True :
                                        embed.timestamp = datetime.datetime.utcnow()
                                        await channel.send(embed = embed)
                                        await sendmessage.delete()
                                        await sendwait.delete()
                                        await embedmenu.delete()
                                        return
                                elif str(reaction.emoji) == "❌":
                                    await message.remove_reaction(reaction, user)                                                                       
                                else:
                                    await message.remove_reaction(reaction, user)

                            except:
                                break

class wlowner :
    @client.command()
    async def wl(ctx, fonction="none", u: discord.Member = None):
        if checkowner(id = ctx.author.id) == True :
            await ctx.message.delete()
            if fonction == "add":
                with open('db/wl/wl.json', 'r') as f:
                    prefixes = json.load(f)
                    
                    prefixes[str(u.id)] = str("wl")

                    with open('db/wl/wl.json', 'w') as f:
                        json.dump(prefixes, f, indent=4)
                    await ctx.send(f"{u.name} a été ajouter a la whitelist")
                    return
            #if fonction == "list" :
            #    with open('db/wl/wl.json', 'r') as f:
            #        prefixes = json.load(f)
            #        id[""] = prefixes
            #    await ctx.send(id)
            if fonction == "remove":
                with open('db/wl/wl.json', 'r') as f:
                    file = json.load(f)

                    file[str(u.id)] = "nowl"
                    with open('db/wl/wl.json', 'w') as f:
                        json.dump(file, f, indent=4)
                        await ctx.send(f"{u.name} n'est plus whitelist")
                        return
            else :
                embed = discord.Embed(
                title = "Argument invalide",
                description = "Synthax: **``wl <add/remove/list> <@user>``**",
                color = 0xFF0000
                )
                await ctx.send(embed= embed)
                return
        if checkowner(id = ctx.author.id) == False:
                await ctx.send("Tu n'est pas owner tu ne peux pas utilser cette command ")
    @client.command()
    async def owner(ctx, fonction="none", u: discord.Member = None):
        await ctx.message.delete()
        if isowner(idowner = ctx.message.author.id) == True:
            if fonction == "add":
                with open('db/wl/owner.json', 'r') as f:
                    prefixes = json.load(f)
                
                prefixes[str(u.id)] = str("owner")

                with open('db/wl/owner.json', 'w') as f:
                    json.dump(prefixes, f, indent=4)
                await ctx.send(f"{u.name} a été ajouter a la list des owner")
                return
            #if fonction == "list" :
            #    with open('db/wl/wl.json', 'r') as f:
            #        prefixes = json.load(f)
            #        id[""] = prefixes
            #    await ctx.send(id)
            if fonction == "remove":
                with open('db/wl/owner.json', 'r') as f:
                    file = json.load(f)

                file[str(u.id)] = "noowner"
                with open('db/wl/owner.json', 'w') as f:
                    json.dump(file, f, indent=4)
                await ctx.send(f"{u.name} n'est plus owner")
                return
            else :
                embed = discord.Embed(
                title = "Argument invalide",
                description = "Synthax: **``owner <add/remove/list> <@user>``**",
                color = 0xFF0000
                )
                await ctx.send(embed= embed)
                return
        if not isowner(idowner = ctx.message.author.id) == True:
            await ctx.send("Tu n'est pas owner tu ne peux pas utilse cette command")
class event : 
    @client.event
    async def on_guild_channel_create(channel):
        channellog = channel.guild.get_channel(get.logserveur(id=channel.guild.id))
        datecrea = datetime.date.today()
        channeln = channel.name
        channelcd = channel.created_at
        if type(channel) == discord.VoiceChannel :
            channeltype = "Channel vocal"
        if  not type(channel) == discord.VoiceChannel :
            channeltype = "Channel écrit"
        embed = discord.Embed(
            title="Channel Crée",
            description=
            f"<#{channel.id}>\n**Crée** :**``{datecrea}``**\n**Categorie** : {channel.category}\n**Type** : ``{channeltype}`` "
        )
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f" {cerdit} \u200b ")
        await channellog.send(embed=embed)


    @client.event
    async def on_guild_channel_delete(channel):
        channellog = channel.guild.get_channel(get.logserveur(id=channel.guild.id))
        datecrea = f"{channel.created_at.strftime('%Y-%m-%d')}"
        channeln = channel.name
        channelcd = channel.created_at
        if type(channel) == discord.VoiceChannel :
            channeltype = "Channel vocal"
        if  not type(channel) == discord.VoiceChannel :
            channeltype = "Channel écrit"
        embed = discord.Embed(
            title="Channel Suprimées",
            description=
            f"Nom : **``{channeln}``**\n**Crée** :**``{datecrea}``**\n**Suprimée** : **``{datetime.date.today()}``**\n**Categorie** : {channel.category}\n**Type** : ``{channeltype}``"
        )
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f" {cerdit} \u200b ")
        await channellog.send(embed=embed)

    @client.event
    async def on_guild_channel_update(before, after):
        channellog = before.guild.get_channel(get.logserveur(id=before.guild.id))
        embed = discord.Embed(
            title =  "Channel Upatade",
            description  =f"""
        <#{after.id}>    
        Nom avant : **``{before.name}``**
        Nom apres : **``{after.name}``**  
        Categorie avant : **``{before.category}``**
        Categorie apres : **``{after.category}``**"""
        )
        await channellog.send(embed = embed)
    # @client.event
    # async def on_message(message):
    #      channellog = message.guild.get_channel(get.logmessage(id=message.guild.id))
    #      if await client.process_commands(message):
    #              return  
    #      if "discord.gg" in message.content.lower():
    #          if checkwl(id  = message.author.id) == True:
    #              return
    #          if checkwl(id  = message.author.id) == False:
    #              if checkowner(id = message.author.id) == True:
    #                  return
    #              if checkowner(id = message.author.id) == False:
    #                  await message.delete() 
    #                  await message.channel.send(f"**Tu n'est pas autorisé a envoyer des invitations <@{message.author.id}> **")
    # #                 embed = discord.Embed(
    # #                 title = "Antilink Message",
    # #                 description = f"**Content du message** : ``{message.content}``"
    # #                 )
    # #                 embed.set_author(
    # #                 name = message.author.name,
    # #                 icon_url = message.author.avatar_url
    # #                 )
    # #                 embed.set_footer( text = f" {cerdit} \u200b ")          
    # #                 await channellog.send(embed = embed)
    # #     if "@everyone" in message.content.lower():
    # #         if checkwl(id  = message.author.id) == True:
    # #             return
    # #         if checkwl(id  = message.author.id) == False:
    #              if checkowner(id = message.author.id) == True:
    #                  return
    #              if checkowner(id = message.author.id) == False:
    #                  await message.delete() 
    #                  await message.channel.send(f"**Tu n'est pas autorise a mentionnez everyone ici <@{message.author.id}>**")
    #                  embed = discord.Embed(
    #                  title = "Antieveryone Message",
    #                  description = f"**Content du message** : ``{message.content}``"
    #                  )
    #                  embed.set_author(
    #                  name = message.author.name,
    #                  icon_url = message.author.avatar_url
    #                  )
    #                  embed.timestamp = datetime.datetime.utcnow()
    #                  embed.set_footer( text = f" {cerdit} \u200b ")          
    #                  await channellog.send(embed = embed)    
class command:
    @client.command()
    async def mybot(ctx):
        await ctx.message.delete()
        if checkowner(id = ctx.author.id) == True :
            ajd = datetime.date.today()
            ajd.strftime('%Y-%m-%d')
            if datebot == "lifetime":
                jours = "lifetime"
            if not datebot == "lifetime":
                args = datebot - ajd
                jours = f"{args.day} jours"
                embed = discord.Embed(
                title = client.user.name,
                description = f"**Temps Restant ** : {jours} \n> **type** : {type}",
                url = oauth
                )
                embed.set_author(
                name = ctx.author.name,
                icon_url= ctx.author.avatar_url
                )
                await ctx.send(embed= embed)
            else : 
                await ctx.send("vous n'avez pas la permision de utilser cette command") 
client.run("MTAzNDgxODY4NjcwNTQ3OTY5MA.Giv6ne.nf_ub5E1FBveQk-A456_n0RREIv_VezjHBMqwQ")
