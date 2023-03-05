"""
    This file contains all the discord activity commands and listeners
"""

from discord.ext import commands
import discord

class Core(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot: commands.Bot = bot


def setup(bot):
    bot.add_cog(Core(bot))