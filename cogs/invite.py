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
    async def invite(self, ctx, *, arg):
        inviteChannelID = 822606443722309642
        inviteURL = await ctx.guild.get_channel(inviteChannelID).create_invite()
        await ctx.send(f'Here is the invite link!: {inviteURL}')


def setup(client):
    """Load cog."""
    client.add_cog(Invite(client))
