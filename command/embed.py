import discord
from discord.ext import commands
import datetime
import time
datebot = "lifetime"
oauth = "https://discord.com/api/oauth2/authorize?client_id=1034818686705479690&permissions=8&scope=bot"
cerdit = "Super Bot "
type  =  "Gestion v1"
def setup(client):
    client.add_cog(Commandembed(client))
from accet.accet import anti, get


class Commandembed(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def embed(self,ctx):
        if get.owner( id = ctx.author.id) == True :
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
                                    reaction, user = await self.client.wait_for("reaction_add", check=check)

                                    if str(reaction.emoji) == "🖊":
                                        titremessage = await ctx.send("Qu'elle est le titre de l'embed ?")
                                        titrewait = await self.client.wait_for('message', check=checka)
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
                                        descriptionwait = await self.client.wait_for('message', check = checka)
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
                                        imagewait = await self.client.wait_for('message', check =checka)
                                        imageembed = imagewait.content                              
                                        embed.set_image(url= imageembed)
                                        await embededit.edit(embed = embed) 
                                        await imagemessage.delete()
                                        await imagewait.delete()
                                        await message.remove_reaction(reaction, user)
                                    elif str(reaction.emoji) == "🪧":
                                        footermessage = await ctx.send("Que dois contenir le footer ? ")
                                        footerwait = await self.client.wait_for('message',check = checka)
                                        embed.set_footer( text= footerwait.content)
                                        await embededit.edit(embed = embed)
                                        await footermessage.delete()
                                        await footerwait.delete()
                                        await message.remove_reaction(reaction, user)
                                    elif str(reaction.emoji) == "🚹":
                                        autheurmessage = await ctx.send("Qu'elle est le nom de l'autheur")
                                        autheurwait = await self.client.wait_for('message',check = checka)
                                        autheurembed[0] = autheurwait.content
                                        await autheurmessage.delete()
                                        await autheurwait.delete()
                                        avatarmessage = await ctx.send("QU'elle est l'avatar de l'auteur")
                                        avatarwait = await self.client.wait_for('message',check = checka)
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
                                        sendwait = await self.client.wait_for('message', check= checka)
                                        channel = ctx.guild.get_channel(int(sendwait.content))
                                        if timeembed == True :
                                            embed.timestamp = datetime.datetime.utcnow()
                                            await channel.send(embed = embed)
                                            await sendmessage.delete()
                                            await sendwait.delete()
                                            await embedmenu.delete()
                                        else :    
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