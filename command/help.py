import discord 
from discord.ext import commands, tasks
import json
from accet.accet import anti, get
def setup(client):
    client.add_cog(setprefix(client))
class setprefix(commands.Cog):
    def __init__(self,client):
        self.client = client    
    @commands.command()
    async def help(self,ctx):
        contents = [
        discord.Embed(title="Gestion commands",description=
    f"""
    ``Embed``
    > embed
    ``Embedimg``
    > embedimg
    ``setlog``
    > setlog <Webhook>
    ``setprefix``
    > setprefix <Prefix>
    ``Antiraid``
    > antiraid    
    """,colour=0xF00C0C),
        discord.Embed(title='Moderation commands',description=
    f"""
    ``Ban``
    > ban <User> <Reason>
    ``unban``
    > unban <User name> <Reason>
    ``kick``
    > kick <User> <Reason>
    ``Mute``
    > mute <User>
    ``Unmute``
    > unmute <User>
    ``Lock``
    > lock
    ``Unlock``
    > unlock
    ``Renew``
    > renew <Channel>
    ``addrole``
    > addrole <User> <Role>
    ``clear``
    > clear <Nombre>
    """,colour=0xF00C0C),
        discord.Embed(title='Public commands',description=
    f"""
    ``Snipe``
    > snipe
    """,colour=0xF00C0C),
        discord.Embed(title='Soon commands',description=
    f"""
    ``Setcolor``
    > setcolor <Color>
    ``Setwelcome``
    > setwelcome <Webhook>
    ``Setstyle``
    > setstyle <Embed/Message>
    ``Removerole``
    > removerole <User> <Role>
    ``Setsenction``
    > setsenction
    """,colour=0xF00C0C),
        discord.Embed(title=f'Bot\'s info | ID: {self.client.user.id}',description=
    f"""
    **Info**
    > **Serveur**: {len(self.client.guilds)}
    > **Developeur** : <@1024298168264953936>
    > **Support** : https://discord.gg/7AErzMPXD3
    > **Invite** :  https://discord.com/api/oauth2/authorize?client_id=1033664384838406144&permissions=8&scope=bot
    """,colour=0xF00C0C)
    ]
        pages = 5
        cur_page = 1
        message = await ctx.send(embed=contents[cur_page - 1])

        await message.add_reaction("◀️")
        await message.add_reaction("▶️")
        idmessage = message.id
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"] and reaction.message

        while True:
            try:
                reaction, user = await self.client.wait_for("reaction_add", check=check)

                if str(reaction.emoji) == "▶️" and cur_page != pages:
                    cur_page += 1
                    await message.edit(embed=contents[cur_page - 1])
                    await message.remove_reaction(reaction, user)

                elif str(reaction.emoji) == "◀️" and cur_page > 1:
                    cur_page -= 1
                    await message.edit(embed=contents[cur_page - 1])
                    await message.remove_reaction(reaction, user)

                else:
                    await message.remove_reaction(reaction, user)

            except:
                break
