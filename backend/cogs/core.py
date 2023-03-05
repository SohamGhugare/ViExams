"""
    This file contains all the discord activity commands and listeners
"""

from discord.ext import commands
import discord
import requests
from enum import Enum
from views import CourseDropdownView


class Core(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot: commands.Bot = bot

    @commands.command()
    async def get(self, ctx: commands.Context):
        await ctx.send("Hey, I'm here to provide you with question papers!", view=CourseDropdownView(self.bot))


def setup(bot):
    bot.add_cog(Core(bot))