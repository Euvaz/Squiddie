"""Class file for misc."""

import discord
from discord.ext import commands


class Misc(commands.Cog):
    """Misc class."""

    def __init__(self, client):
        """Initialize."""
        self.client = client

    ## Misc commands
    # Chicken command
    @commands.command(name="chicken")
    async def chicken(self, ctx):
        """Think fast chucklenuts."""
        await ctx.send("https://tenor.com/view/chicken-gif-19565842")


def setup(client):
    """Load cog."""
    client.add_cog(Misc(client))
