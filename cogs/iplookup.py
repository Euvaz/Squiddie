"""Class file for IPLookup."""

import discord
from discord.ext import commands
from requests import get


class IPLookup(commands.Cog):
    """IPLookup class."""

    def __init__(self, client):
        """Initialize."""
        self.client = client

    # IPLookup command
    @commands.command(name="iplookup")
    async def iplookup(self, ctx, arg):
        """Display general IP information."""
        r = get(f'http://ipwhois.app/json/{arg}').json()

        embed = discord.Embed(
            title=f"IP lookup results for {r['ip']}",
            description=f"ISP: {r['isp']}\nCountry: {r['country']}\nRegion: {r['region']}\nCity: {r['city']}\nTimezone: {r['timezone']}\nGMT-Offset: {r['timezone_gmt']}",
            color=discord.Color.red(),
            )
        await ctx.send(embed=embed)


def setup(client):
    """Load cog."""
    client.add_cog(IPLookup(client))
