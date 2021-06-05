"""Class file for XMR."""

import discord
from discord.ext import commands
import requests


class XMR(commands.Cog):
    """XMR class."""

    def __init__(self, client):
        """Initialize."""
        self.client = client

    # XMR command
    @commands.command(name="xmr")
    async def _xmr(self, ctx):
        """Display XMR exchange rate."""
        r = requests.get("https://www.coindesk.com/price/monero").text
        damu = (
            r.split('<div class="price-large">')[1]
                .split("</div>")[0]
                .replace('<span class="symbol">', "")
                .replace("</span>", "")
        )
        embed = discord.Embed(
            title="Monero",
            description=f"The Current XMR Rate Is {damu}",
            color=discord.Color.orange(),
        )
        embed.set_thumbnail(
            url="https://s2.coinmarketcap.com/static/img/coins/200x200/328.png"
        )
        await ctx.send(embed=embed)


def setup(client):
    """Load cog."""
    client.add_cog(XMR(client))
