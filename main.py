import discord
from discord.ext import menus, commands


TOKEN="haha you think you got me didnt you trying to get me to publish my token to a live public repo hahaha no fuck off"
bot = commands.Bot(command_prefix='!')

@bot.command(name="bruh", help="moment")
async def menu_example(ctx):
    print("bruhing...")
    await ctx.channel.send("moment")

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

bot.run(TOKEN)


