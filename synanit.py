# import json
# import os
# import asyncio

# from aiohttp import ClientSession
import logging
# from typing import Optional
# import os

# from discord.app_commands import CommandTree
# from discord import Interaction
# from discord import app_commands
from discord.ext.commands import Bot
import discord
# from discord.ext import commands

from libs import secrets


class Synanit(Bot):
    def __init__(self):
        super().__init__(command_prefix=",", intents=discord.Intents.default())
        # self.initial_extensions = ["cogs.admin", "cogs.devUtil", "cogs.todo", "cogs.utilities"]
        self.initial_extensions = ["cogs.admin", "cogs.devUtil", "cogs.utilities"]

    async def setup_hook(self):
        for ext in self.initial_extensions:
            await self.load_extension(ext)
    
    async def on_ready(self):
        print("Ready!")

client = Synanit()

client.run(
    secrets.TOKEN,
    log_level=logging.DEBUG
    # log_handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
)