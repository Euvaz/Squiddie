"""Class file for BTC."""

import discord
from discord.ext import commands
import requests


class BTC(commands.Cog):
    """BTC class."""

    def __init__(self, client):
        """Initialize."""
        self.client = client

    # BTC command
    @commands.command(name="btc")
    async def btc(self, ctx):
        """Display BTC exchange rate."""
        r = requests.get("https://www.coindesk.com/price/bitcoin").text
        damu = (
            r.split('<div class="price-large">')[1]
            .split("</div>")[0]
            .replace('<span class="symbol">', "")
            .replace("</span>", "")
        )
        embed = discord.Embed(
            title="Bitcoin",
            description=f"The Current BTC Rate Is {damu}",
            color=discord.Color.gold(),
        )
        embed.set_thumbnail(
            url="https://static.currency.com/img/media/bitcoin.dd8a16.png"
        )
        await ctx.send(embed=embed)


def setup(client):
    """Load cog."""
    client.add_cog(BTC(client))
