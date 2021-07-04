"""Class file for Event."""

import discord
from discord.ext import commands
from discord.ext import tasks

from hacker_news import hacker_news_run


class Event(commands.Cog):
    """Event class."""

    def __init__(self, client):
        """Initialize."""
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        """Start news task."""
        self._news.start()

        """Confirm start, set status."""
        await self.client.change_presence(
            status=discord.Status.online,
            activity=discord.Game("with FBI crime statistics"),
        )
        print(f"{self.client.user} is ready")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(f"Command not recognized.")

    # Tasks
    @tasks.loop(hours=24)
    async def _news(self):
        hacker_news_run()


def setup(client):
    """Load cog."""
    client.add_cog(Event(client))
