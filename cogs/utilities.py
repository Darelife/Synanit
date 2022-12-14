import discord
from discord.ext import commands
from discord import app_commands
import os
from libs import secrets
import datetime

folderlocation = secrets.folderLocation
image_list = os.listdir(f"{folderlocation}/data/images/study")
imgList = []
for i in image_list:
    i = i[:-4]
    imgList.append(i)
imgStr = (", ".join(imgList))
class Utilities(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is running")

    @commands.command(name="movie", aliases=["movies", "m"])
    async def _movie(self, ctx, *, movieName):
        movieName = movieName.replace(" ", "+")
        await ctx.send(f"https://www.google.com/search?q={movieName}+movie")
        await ctx.send(
            "Lmao this isn't what the bot is supposed to do. The developer has written the code, but he needs to clean the code, and make it look good. So he just made a google search for the movie name and he sent it to you. He has apologized for the inconvenience."
        )

    @app_commands.command(
        name="movie",
        description="Searches for a movie on Google. (gonna be perfect in the future when i have time)"
    )
    @app_commands.describe(
        movie_name="The name of the movie you want to search for",
        ephemeral="True if you don't want anyone else to see the message, defaults to False",
    )
    async def _movie(self, interaction: discord.Interaction, movie_name: str, ephemeral: bool = False):
        # await discord.InteractionResponse.defer()
        movie_name = movie_name.replace(" ", "+")
        await interaction.response.send_message(
            f"""https://www.google.com/search?q={movie_name}+movie
Lmao this isn't what the bot is supposed to do. The developer has written the code, but he needs to clean the code, and make it look good. So he just made a google search for the movie name and he sent it to you. He has apologized for the inconvenience.""",
            ephemeral=ephemeral
        )

    @commands.command(name="invite", aliases=["invitebot"])
    async def _invite(self, ctx):
        await ctx.send(
            "https://discord.com/oauth2/authorize?client_id=980733466968748122&permissions=148221774912&scope=bot%20applications.commands"
        )

    @app_commands.command(name="invite", description="Invite the bot to your server")
    @app_commands.describe(
        ephemeral="True if you don't want anyone else to see the message. Defaults to False"
    )
    async def _invite(self, interaction: discord.Interaction, ephemeral: bool):
        await interaction.response.send_message(
            f"{ephemeral} https://discord.com/oauth2/authorize?client_id=980733466968748122&permissions=148221774912&scope=bot%20applications.commands",
            ephemeral=ephemeral
        )

    @app_commands.command(name="yo", description="Says Yo")
    @app_commands.describe(name="Your name")
    async def _yo(self, interaction: discord.Interaction, *, name: str):
        # await interaction.response.defer()
        await interaction.response.send_message(f"Yo {name}", ephemeral=True)

    @app_commands.command(name = "study_event", description="Create a study event")
    @app_commands.describe(
        name="The name of the study event",
        description="The description of the study event",
        channel_id="The id of the study event's channel",
        image=imgStr
    )
    async def _study_event(self, interaction: discord.Interaction, name: str, description:str, channel_id:str = "952844838280249365", image:str = "realistic_image_of_a_boy_studying"):
        with open(f"{folderlocation}/data/images/study/{image}.png", "rb") as image_file:
            #data\images\study\1Morningstudy.png
            img = image_file.read()
        await interaction.response.defer()
        channel_id = int(channel_id)
        guild = interaction.guild
        channel = guild.get_channel(channel_id)
        start_time:datetime.datetime = datetime.datetime.now().astimezone()
        a = await guild.create_scheduled_event(name=name, description=description, channel=channel, start_time = start_time+datetime.timedelta(minutes=5), image=img)
        id = a.id
        await interaction.edit_original_response(content = f"{name} event has been created\nhttps://discord.com/events/{guild.id}/{id}") 

async def setup(client):
    await client.add_cog(Utilities(client))
