import discord 
from discord.ext import commands, tasks
import os
import datetime
import time
import asyncio
import cogs_2
import json
from discord import Permissions
intents = discord.Intents.all()
def get_prefix(client, message): 
    with open('db/command/prefix.json', 'r') as f: 
        prefixes = json.load(f) 
    return prefixes[str(message.guild.id)] 
client = commands.Bot(command_prefix=(get_prefix),help_command= None,intents=intents)

def checkwl(id):
    with open('./db/wl/wl.json', 'r') as f:
      prefixes = json.load(f)
      lenwl= len(prefixes['wl'])
    wllen = -1
    for i in range(0,lenwl- 1):
        wllen + 1
        if prefixes['wl'][wllen]  == str(id):
            return True

def load_command():
    commandnb = 0
    for filename in os.listdir('./command'):
        commandnb = commandnb+ 1
        if filename.endswith('.py'):
            client.load_extension(f'command.{filename[:-3]}')
            
            
    print(f"Tout les command on été load avec succes\nNombre Command {commandnb}")
def load_event():
    for filename in os.listdir('./event'):
        if filename.endswith('.py'):
            client.load_extension(f'event.{filename[:-3]}')
def unload_command():
    commandnb = 0
    for filename in os.listdir('./command'):
        commandnb = commandnb+ 1
        if filename.endswith('.py'):
            client.unload_extension(f'command.{filename[:-3]}')
def unload_event():
    for filename in os.listdir('./event'):
        if filename.endswith('.py'):
            client.unload_extension(f'event.{filename[:-3]}')
load_command()
@client.command()
async def reload(ctx):
    await ctx.send("Les command on été reload")
    unload_command()
    load_command()
    unload_event()
    load_event()
@client.event
async def on_ready():
    print(client.user.name)
    print(f'Currently at {len(client.guilds)} servers!')
    print('Servers connected to:')

          
client.run("")