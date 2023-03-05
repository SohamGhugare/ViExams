"""
    This file contains all the discord activity commands and listeners
"""

from discord.ext import commands
import discord
import requests
from enum import Enum
from views import CourseDropdownView, ChoiceButton


class Core(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot: commands.Bot = bot

    @commands.command()
    async def get(self, ctx: commands.Context):
        await ctx.send("Hey, I'm here to provide you with question papers!", view=CourseDropdownView(self.bot))

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.channel.id != 1081814592927309865:
            return 
        if message.author.id == self.bot.user.id:
            return
        await message.channel.send("Hi, How can I help you today..?", view=ChoiceButton(self.bot))


def setup(bot):
    bot.add_cog(Core(bot))