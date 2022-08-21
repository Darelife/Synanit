from libs import definitions
import traceback
from copy import copy
import typing

import discord
from discord.ext import commands

import secrets

dummyVariable = "test"


class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is running")

    # this command won't work cuz the intent isn't enabled, so u'll have to use it in a DM
    @commands.command(hidden=True, name="eval", aliases=["evaluate"])
    async def _eval(self, ctx, *, code: str):
        """
        Evaluates code.
        """
        global dummyVariable

        # ? DO NOT EDIT THIS LINE

        if ctx.author.id == secrets.darelife or ctx.author.id == secrets.noir:
            funcName = "evalFunction"
            code = definitions.getCode(code)
            code = "\n".join(f"    {i}" for i in code.splitlines())
            body = f"async def {funcName}():\n{code}"
            env = {
                "bot": ctx.bot,
                "discord": discord,
                "commands": commands,
                "ctx": ctx,
                "client": self.client,
                "__import__": __import__,
                "dummyVariable": dummyVariable,
            }
            globals().update(env)
            # If you replace globals() with env, and try to change the value of dummyVariable, it will not work.
            # Because, the value of dummyVariable (global) is not in the env.
            # Env only contains the value of dummyVariable (local)
            try:
                exec(body, globals())
            except:
                await ctx.send(f"```py\n{traceback.format_exc()}\n```")
            result = await eval(f"{funcName}()", globals())
            # try:
            #   await ctx.send(result)
            # except:
            #   await ctx.send(f"```py\n{traceback.format_exc()}\n```")

    # this command won't work cuz the intent isn't enabled, so u'll have to use it in a DM
    @commands.command(hidden=True, name="sudo", aliases=["su"])
    async def _sudo(self, ctx, user: discord.Member, *, command):
        """
        Takes Control
        """
        if ctx.author.id == secrets.darelife or ctx.author.id == secrets.noir:
            msg = copy(ctx.message)
            msg.author = user
            msg.content = ctx.prefix + command

            await self.client.process_commands(msg)

    # this command won't work cuz the intent isn't enabled, so u'll have to use it in a DM
    @commands.command(name="sync", hidden=True)
    @commands.is_owner()
    async def _sync(
        self,
        ctx: commands.Context,
        guilds: commands.Greedy[discord.Object],
        spec: typing.Optional[typing.Literal["~", "*"]] = None,
    ) -> None:
        """Syncs the bot with the guilds.
        ,sync -> global sync
        ,sync ~ -> sync current guild
        ,sync * -> copies all global app commands to current guild and syncs
        ,sync id_1 id_2 -> syncs guilds with id 1 and 2"""
        if not guilds:
            if spec == "~":
                fmt = await self.client.tree.sync(guild=ctx.guild)

            elif spec == "*":
                self.client.tree.copy_global_to(guild=ctx.guild)
                fmt = await self.client.tree.sync(guild=ctx.guild)

            else:
                fmt = await self.client.tree.sync()

            await ctx.send(
                f"Synced {len(fmt)} commands {'globally' if spec is None else 'to the current guild.'}"
            )
            return

        fmt = 0
        for guild in guilds:
            try:
                await self.client.tree.sync(guild=guild)
            except discord.errors.HTTPException:
                pass
            else:
                fmt += 1

        await ctx.send(f"Synced the tree to {fmt}/{len(guilds)} guilds.")

    # TO load a cog
    # this command won't work cuz the intent isn't enabled, so u'll have to use it in a DM
    @commands.command(hidden=True)
    async def load(self, ctx, extension):
        if ctx.author.id == secrets.darelife or ctx.author.id == secrets.noir:
            await self.client.load_extension(f"cogs.{extension}")

    # TO unload a cog
    # this command won't work cuz the intent isn't enabled, so u'll have to use it in a DM
    @commands.command(hidden=True)
    async def unload(self, ctx, extension):
        if ctx.author.id == secrets.darelife or ctx.author.id == secrets.noir:
            await self.client.unload_extension(f"cogs.{extension}")


async def setup(client):
    await client.add_cog(Admin(client))
