import discord
from discord.ext import commands
from libs import definitions
import json


class Todo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is running")

    @commands.hybrid_group(
        name="calendar", aliases=["cal"], invoke_without_command=True
    )
    async def _calendar(self, ctx: commands.Context):
        # TODO: Get the tasks
        data = definitions.jsonload("data/calendar(deployment).json")
        text = f"""
        **CALENDAR**
        -------------
    """
        for index in range(7):
            try:
                if data["Data"][str(definitions.getYearNow(daysdelta=index))][
                    str(int(definitions.getMonthNow(daysdelta=index)))
                ][str(int(ctx.author.id))][
                    str(int(definitions.getDateNow(daysdelta=index)))
                ][
                    "tasks"
                ]:
                    text += f"""**{definitions.getDayOfWeekNow(daysdelta=index)}**
            {(", ").join(data["Data"][str(definitions.getYearNow(daysdelta=index))][str(int(definitions.getMonthNow(daysdelta=index)))][str(int(ctx.author.id))][str(int(definitions.getDateNow(daysdelta=index)))]["tasks"])}
        """
            except:
                pass
            await ctx.send(text)
        await ctx.send(f"{ctx.author.mention}")

    @_calendar.command(hidden=True, name="view", aliases=["v"])
    async def _view(self, ctx: commands.Context):
        # TODO: Get the tasks
        data = definitions.jsonload("data/calendar(deployment).json")
        text = f"""
        **CALENDAR**
        -------------
    """
        for index in range(7):
            try:
                if data["Data"][str(definitions.getYearNow(daysdelta=index))][
                    str(int(definitions.getMonthNow(daysdelta=index)))
                ][str(int(ctx.author.id))][
                    str(int(definitions.getDateNow(daysdelta=index)))
                ][
                    "tasks"
                ]:
                    text += f"""**{definitions.getDayOfWeekNow(daysdelta=index)}**
            {(", ").join(data["Data"][str(definitions.getYearNow(daysdelta=index))][str(int(definitions.getMonthNow(daysdelta=index)))][str(int(ctx.author.id))][str(int(definitions.getDateNow(daysdelta=index)))]["tasks"])}
        """
            except:
                pass
        await ctx.send(text)

    @_calendar.command(name="add", aliases=["a"])
    async def _add(
        self, ctx: commands.Context, date: str, month: str, year: str, tasks: str
    ):
        with open("data/calendar(deployment).json", "r") as f:
            CurrentData = json.load(f)
            # CurrentData=CurrentData["Data"]
        if str(year) not in CurrentData["Data"]:
            CurrentData["Data"][year] = {}
        if month not in CurrentData["Data"][year]:
            CurrentData["Data"][year][month] = {}
        if str(ctx.author.id) not in CurrentData["Data"][year][month]:
            CurrentData["Data"][year][month][str(ctx.author.id)] = {}
        if date not in CurrentData["Data"][year][month][str(ctx.author.id)]:
            CurrentData["Data"][year][month][str(ctx.author.id)][date] = {}
        if bool(CurrentData["Data"][year][month][str(ctx.author.id)][date]) == False:
            CurrentData["Data"][year][month][str(ctx.author.id)][date]["tasks"] = []
        for x in tasks.split(","):
            CurrentData["Data"][year][month][str(ctx.author.id)][date]["tasks"].append(
                x
            )

        with open("data/calendar(deployment).json", "w") as f:
            json.dump(CurrentData, f, indent=2)
        await ctx.send(f"Added {tasks} to {date}/{month}/{year}")


async def setup(client):
    await client.add_cog(Todo(client))
