from discord.ui import View, Button, Select
from discord import SelectOption
import discord
from database import Database
from enum import Enum
import requests

class Url(Enum):
    FETCH_LINKS = "http://127.0.0.1:8000/api/papers"


class CourseDropdown(Select):
    def __init__(self, bot_: discord.Bot, time: int=None):
        self.time = time
        self.bot = bot_
        self.db = Database()
        options = [SelectOption(label=option.replace("-", " ").title(), value=option) for option in self.db.fetch_courses()]

        super().__init__(
            placeholder="Select a course...",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Fetching {self.values[0]} papers...")
        url = Url.FETCH_LINKS.value+"?course="+self.values[0]
        data = requests.get(url).json()
        await interaction.message.channel.send(data['response']['data']['image_urls'][0]['url'])



class CourseDropdownView(View):
    def __init__(self, bot_: discord.Bot, time: int=None):
        self.bot = bot_
        self.time = time
        super().__init__(CourseDropdown(self.bot, time=time))

class ChoiceButton(View):
    def __init__(self, bot_):
        super().__init__()
        self.value = None
        self.bot = bot_
    
    @discord.ui.button(label="Upload", style=discord.ButtonStyle.green)
    async def confirm_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        await interaction.message.channel.send("Please send your image here to upload")
        self.value = True
        self.stop()

    @discord.ui.button(label="Fetch", style=discord.ButtonStyle.green)
    async def cancel_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        await interaction.message.channel.send("Hey, I'm here to provide you with question papers!", view=CourseDropdownView(self.bot))
        self.value = True
        self.stop()