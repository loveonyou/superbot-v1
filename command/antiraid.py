import discord
from discord.ext import commands
import time
import datetime
import json
import accet.accet 
from accet.accet import anti, get
datebot = "lifetime"
oauth = "https://discord.com/api/oauth2/authorize?client_id=1034818686705479690&permissions=8&scope=bot"
cerdit = "Super Bot "
type  =  "Gestion v1"

def setup(client):
    client.add_cog(Eventchannelcreate(client))
class Eventchannelcreate(commands.Cog):
    def __init__(self,client):
        self.client = client  
    @commands.command()
    async def antiraid(self,ctx):
      if get.owner(id = ctx.author.id) == True:
            await ctx.message.delete()
            try :
              anti_link = (f"**{anti.link(id = ctx.guild.id)}**")
            except :
              anti_link = "**none**"
            try :
              anti_everyone = (f"**{anti.everyone(id = ctx.guild.id)}**")
            except :
              anti_everyone = "**none**"
            try :
              anti_channel = (f"**{anti.channel(id = ctx.guild.id)}**")
            except :
              anti_channel = "**none**"
            try :
              anti_role = (f"**{anti.role(id = ctx.guild.id)}**")
            except :
              anti_role = "**none**"
            try :
              anti_webhook = (f"**{anti.webhook(id = ctx.guild.id)}**")
            except :
              anti_webhook = "**none**"
            try :
              anti_ban = (f"**{anti.ban(id = ctx.guild.id)}**")
            except :
              anti_ban = "**none**"
            try :
              anti_spam = (f"**{anti.spam(id = ctx.guild.id)}**")
            except :
              anti_spam = "**none**"
            embed = discord.Embed(
                title = "Antiraid",
                description  = "",
                color = discord.Color.from_rgb(255,0,0)
            )
            embed.add_field(
                name= "1️⃣ ・links ",
                value= f"L'anti channel permet de suprimer les  invitations discord\n🌐 : {anti_link}",
                inline= False
            )
            embed.add_field(
                name="2️⃣ ・ everyone",
                value= f"L'anti everyone permet de suprimer les message qui contient everyone\n🌐 :{anti_everyone} ",
                inline= False
            )
            embed.add_field(
              name = "3️⃣・channel",
              value = f"L'anti channel empeche la creation de channel **pour tout le monde**\n🌐 :{anti_channel}",
              inline= False
            )
            embed.add_field(
              name = "4️⃣・Roles",
              value= f"L'anti rank empeche <ajout/creation/supression> de roles\n🌐 :{anti_role}",
              inline= False

            )
            embed.add_field(
              name=  "5️⃣・Webhook",
              value =f"L'anti webhool empeche la creation de webhook\n🌐 :{anti_webhook}",
              inline= False 
            )
            embed.add_field(
              name = "6️⃣・Ban",
              value = f"L'anti ban deban les gens qui on été banni\n🌐 :{anti_ban}",
              inline=False
            )
            embed.add_field(
              name = "7️⃣・Antispam",
              value= f"l'antispam empeche les personne de spam de message sur votre serveur\n🌐 :{anti_spam}",
              inline= False
            )
            embed.set_author(
                    name= ctx.message.author.name,
                    icon_url = ctx.message.author.avatar_url
            )        
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer( text = f" {cerdit} \u200b ")
            #**personne qui ne sont pas autorisé de le faire**
            message = await ctx.send(embed = embed) 
            await message.add_reaction("1️⃣")
            await message.add_reaction("2️⃣")
            await message.add_reaction("3️⃣")
            await message.add_reaction("4️⃣")
            await message.add_reaction("5️⃣")
            await message.add_reaction("6️⃣")
            await message.add_reaction("7️⃣")
            await message.add_reaction("❌")
            idmessage = message.id
            def check(reaction, user):
                            return user == ctx.author and str(reaction.emoji) in ["1️⃣", "2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","❌"] and reaction.message.id == idmessage
            def checka(message):
                        return message.author == ctx.author and message.channel == ctx.channel 
            def checklink(reaction, user):
                            return user == ctx.author and str(reaction.emoji) in ["✅", "❎","✖️"] 
            while True:
                        try:
                            reaction, user= await self.client.wait_for("reaction_add", check=check)        
                            if str(reaction.emoji) == "1️⃣": 
                              await message.remove_reaction(reaction, user)
                              embedlinks = discord.Embed(
                                title = "Anti links",
                                description = f"✅ : **pour activer l'antilink**\n❎ : **pour desactiver l'antilink**\n 🌐 : {anti_link}",
                                color = discord.Color.from_rgb(255,0,0)
                              )   
                              embedlinks.set_footer(text="pour close se message reagis avec ✖️")
                              messagelinks = await ctx.send(embed = embedlinks)
                              await messagelinks.add_reaction("✅")
                              await messagelinks.add_reaction("❎")
                              await messagelinks.add_reaction("✖️")
                              while True:
                                  try:
                                    reaction, user = await self.client.wait_for("reaction_add", check=checklink)  
                                    if str(reaction.emoji) == "✅":
                                      with open('db/antiraid/antilink.json', 'r') as f:
                                        prefixes = json.load(f)

                                      prefixes[str(ctx.guild.id)] = "on"

                                      with open('db/antiraid/antilink.json', 'w') as f: 
                                        json.dump(prefixes, f, indent=4)
                                      messagelinkon =await ctx.send("**antilink activé par succés**")
                                      time.sleep(2)
                                      await messagelinkon.delete()
                                      await messagelinks.delete()
                                      break
                                    if str(reaction.emoji) == "❎":
                                      with open('db/antiraid/antilink.json', 'r') as f:
                                        prefixes = json.load(f)

                                      prefixes[str(ctx.guild.id)] = "off"

                                      with open('db/antiraid/antilink.json', 'w') as f: 
                                        json.dump(prefixes, f, indent=4)
                                      messagelinkoff =await ctx.send("**antilink desactivé par succés**")
                                      time.sleep(2)
                                      await messagelinkoff.delete()
                                      await messagelinks.delete()
                                      break
                                    if str(reaction.emoji) == "✖️":
                                      await messagelinks.delete()
                                      break
                                  except:
                                    break  
                            if str(reaction.emoji) == "2️⃣":
                              await message.remove_reaction(reaction, user)
                              embedeveryone = discord.Embed(
                                title = "Anti @everyone",
                                description =f"✅ : **pour activer l'antieveryone**\n❎ : **pour desactiver l'antieveryone**\n 🌐 : {anti_channel}",
                                color = discord.Color.from_rgb(255,0,0)
                              )   
                              embedeveryone.set_footer(text="pour close se message reagis avec ✖️")
                              message_everyone = await ctx.send(embed = embedeveryone)
                              await message_everyone.add_reaction("✅")
                              await message_everyone.add_reaction("❎")
                              await message_everyone.add_reaction("✖️")
                              while True:
                                  try:
                                    reaction, user = await self.client.wait_for("reaction_add", check=checklink)  
                                    if str(reaction.emoji) == "✅":
                                      with open('db/antiraid/antieveryone.json', 'r') as f:
                                        prefixes = json.load(f)

                                      prefixes[str(ctx.guild.id)] = "on"

                                      with open('db/antiraid/antieveryone.json', 'w') as f: 
                                        json.dump(prefixes, f, indent=4)
                                      message_everyone_on =await ctx.send("**anti everyone activé par succés**")
                                      time.sleep(2)
                                      await message_everyone_on.delete()
                                      await message_everyone.delete()
                                      break
                                    if str(reaction.emoji) == "❎":
                                      with open('db/antiraid/antieveryone.json', 'r') as f:
                                        prefixes = json.load(f)

                                      prefixes[str(ctx.guild.id)] = "off"

                                      with open('db/antiraid/antieveryone.json', 'w') as f: 
                                        json.dump(prefixes, f, indent=4)
                                      message_everyone_off =await ctx.send("**anti everyone desactivé par succés**")
                                      time.sleep(2)
                                      await message_everyone_off.delete()
                                      await message_everyone.delete()
                                      break
                                    if str(reaction.emoji) == "✖️":
                                      await message_everyone.delete()
                                      break
                                  except:
                                    break                          
                            if str(reaction.emoji) == "3️⃣":
                              await message.remove_reaction(reaction, user)
                              embedchannel = discord.Embed(
                                title = "Anti Channel",
                                description =f"✅ : **pour activer l'antichannel**\n❎ : **pour desactiver l'antichannel**\n 🌐 : {anti_channel}",
                                color = discord.Color.from_rgb(255,0,0)
                              )   
                              embedchannel.set_footer(text="pour close se message reagis avec ✖️")
                              message_channel = await ctx.send(embed = embedchannel)
                              await message_channel.add_reaction("✅")
                              await message_channel.add_reaction("❎")
                              await message_channel.add_reaction("✖️")
                              while True:
                                  try:
                                    reaction, user = await self.client.wait_for("reaction_add", check=checklink)  
                                    if str(reaction.emoji) == "✅":
                                      with open('db/antiraid/channel.json', 'r') as f:
                                        prefixes = json.load(f)

                                      prefixes[str(ctx.guild.id)] = "on"

                                      with open('db/antiraid/channel.json', 'w') as f: 
                                        json.dump(prefixes, f, indent=4)
                                      message_channel_on =await ctx.send("**anti channel activé par succés**")
                                      time.sleep(2)
                                      await message_channel_on.delete()
                                      await message_channel.delete()
                                      break
                                    if str(reaction.emoji) == "❎":
                                      with open('db/antiraid/channel.json', 'r') as f:
                                        prefixes = json.load(f)

                                      prefixes[str(ctx.guild.id)] = "off"

                                      with open('db/antiraid/channel.json', 'w') as f: 
                                        json.dump(prefixes, f, indent=4)
                                      message_channel_off =await ctx.send("**anti channel desactivé par succés**")
                                      time.sleep(2)
                                      await message_channel_off.delete()
                                      await anti_channel.delete()
                                      break
                                    if str(reaction.emoji) == "✖️":
                                      await message_channel.delete()
                                      break
                                  except:
                                    break                                                        
                            if str(reaction.emoji) == "❌":
                              await message.remove_reaction(reaction, user)
                              antiraidmes = await ctx.send("**antiraid close**")
                              await message.delete()
                              time.sleep(4)
                              await antiraidmes.delete()
                              return
                        except:
                            break  
      else : 
          return                        