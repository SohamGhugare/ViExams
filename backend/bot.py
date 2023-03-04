import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv('backend/.env')

token = os.getenv('TOKEN')
owner_ids = [884026947699634197]

bot = commands.Bot(command_prefix=">", intents=discord.Intents.all(), owner_ids=owner_ids)

try:
    bot.load_extension(f"utils")
    print(f"Successfully loaded utils cog")
except Exception as e:
    print(e)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


bot.run(token)