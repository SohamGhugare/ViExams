"""
    This file contains all the utility code
"""

from ocr import OCR
from PIL import Image
import discord
from discord.ext import commands
from typing import List

class OcrUtility:
    def parse_course(self, img_path=None, content=None):
        if img_path:
            img = Image.open(img_path)
            extract = OCR().ocr(img)
            courses = [
                "Engineering Chemistry",
                "Calculus",
                "Basic Electrical and Electronics Engineering",
                "Engineering Physics",
                "Engineering Mechanics"
            ]
            for course in courses:
                if course in extract:
                    return course
                
class DiscordUtility(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot
        self.debug_guild = None

    @commands.Cog.listener()
    async def on_ready(self):
        self.debug_guild = self.bot.get_guild(1081601039645544528)

    @property
    def _predefined_courses(self) -> List[discord.CategoryChannel]:
        channels = self.debug_guild.channels
        return [channel.name for channel in channels if channel.category_id == 1081601131781820466]
    
    async def upload_image(self, img_path):
        courses = self._predefined_courses
        img_course = OcrUtility().parse_course(img_path).lower().replace(" ", "-")
        if img_course not in courses:
            await self.debug_guild.create_text_channel(
                name=img_course,
                category=self.debug_guild.get_channel(1081601131781820466)
            )
        for channel in self.debug_guild.channels:
            if channel.name == img_course:
                msg = await channel.send(file=discord.File(img_path))
                img = msg.attachments[0]
                ch = self.debug_guild.get_channel(1081625462784151652)
                await ch.send(f"{img_course} - `{img.url}`")

    @commands.command()
    async def test_upload(self, ctx: commands.Context, img_path: str):
        
        await ctx.send("Testing...")
        img_path = "backend/tests/"+img_path+".jpg"
        await self.upload_image(img_path)


def setup(bot):
    bot.add_cog(DiscordUtility(bot))        

if __name__ == "__main__":
    print(OcrUtility().parse_course(img_path="backend/tests/calculus-jpg.jpg"))

