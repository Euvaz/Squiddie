"""Class file for infract."""

import discord
from discord.ext import commands


class Infract(commands.Cog):
    """Infract class."""

    def __init__(self, client):
        """Initialize."""
        self.client = client

    # Infract command
    @commands.command(name="infract")
    async def infract(self, ctx, *, arg):
        pass


def setup(client):
    """Load cog."""
    client.add_cog(Infract(client))
