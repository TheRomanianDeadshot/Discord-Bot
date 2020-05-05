import os
import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

        print(
            f"{client.user} is online in the following guild:\n"
            f"{guild.name} (id: {guild.id})"
        )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == "idk":
        response = f"Hello, {message.author}"
        await message.channel.send(response)

    if message.content == "bruh":
        response1 = "moment"
        await message.channel.send(response1)

client.run(TOKEN)