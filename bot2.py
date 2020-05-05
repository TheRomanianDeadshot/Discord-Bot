import os
import random
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('GUILD')

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f"{bot.user} has connected to the guild:\n"
        f"{guild.name}(id: {guild.id})"
    )

@bot.command(name='idk')
async def idontknow(ctx):
    response = f'Hello,{ctx.message.author}'
    await ctx.send(response)

bot.run(TOKEN)