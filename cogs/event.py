"""Class file for Event."""

import discord
from discord.ext import commands
from datetime import datetime as dt
from cogs.news import News


def get_time():
    time = dt.now().strftime('[%H:%M:%S]')
    return time


class Event(commands.Cog):
    """Event class."""

    def __init__(self, client):
        """Initialize."""
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        """Start tasks."""
        News.news.start(News(self))

        """Confirm start, set status."""
        await self.client.change_presence(
            status=discord.Status.online,
            activity=discord.Streaming(name="Le Fishe au chocolat",
                                       url='https://www.youtube.com/watch?v=3uQzdlVsLXY'),
        )
        print(f"{get_time()} {self.client.user} is ready")

    @commands.Cog.listener()
    async def on_command(self, ctx):
        print(f"{get_time()} Command \"{ctx.command}\" was executed")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(f"Command not recognized.")


def setup(client):
    """Load cog."""
    client.add_cog(Event(client))
