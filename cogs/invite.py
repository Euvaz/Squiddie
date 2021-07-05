"""Class file for invite."""

import discord
from discord.ext import commands


class Invite(commands.Cog):
    """Invite class."""

    def __init__(self, client):
        """Initialize"""
        self.client = client

    # Invite command
    @commands.command(name="invite")
    async def _infract(self, ctx, *, arg):
        pass


def setup(client):
    """Load cog."""
    client.add_cog(Invite(client))
