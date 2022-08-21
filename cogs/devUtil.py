import discord
from discord.ext import commands
from discord import app_commands


class Developer_Utilities(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is running")

    @app_commands.command(name="character")
    @app_commands.describe(
        message="The string whose character you want to count",
        ephemeral="True if you don't want anyone else to see the message, defaults to False",
    )
    async def _char(
        self, interaction: discord.Interaction, message: str, ephemeral: bool = False
    ):
        """
        Counts the number of characters in a message.
        """
        await interaction.response.send_message(
            f"The message has {len(message)} characters.", ephemeral=ephemeral
        )


async def setup(client):
    await client.add_cog(Developer_Utilities(client))
