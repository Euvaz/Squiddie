"""Class file for ETH."""

import discord
from discord.ext import commands
import requests


class ETH(commands.Cog):
    """ETH class."""

    def __init__(self, client):
        """Initialize."""
        self.client = client

    # ETH command
    @commands.command(name="eth")
    async def eth(self, ctx):
        """Display ETH exchange rate."""
        r = requests.get("https://www.coindesk.com/price/ethereum").text
        damu = (
            r.split('<div class="price-large">')[1]
            .split("</div>")[0]
            .replace('<span class="symbol">', "")
            .replace("</span>", "")
        )
        embed = discord.Embed(
            title="Ethereum",
            description=f"The Current ETH Rate Is {damu}",
            color=discord.Color.greyple(),
        )
        embed.set_thumbnail(
            url="https://cryptologos.cc/logos/ethereum-eth-logo.png?v=010"
        )
        await ctx.send(embed=embed)


def setup(client):
    """Load cog."""
    client.add_cog(ETH(client))
