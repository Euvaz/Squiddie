"""Class file for XMR."""

import discord
from discord.ext import commands
import http.client
import json


class XMR(commands.Cog):
    """XMR class."""

    def __init__(self, client):
        """Initialize."""
        self.client = client

    # XMR command
    @commands.command(name="xmr")
    async def xmr(self, ctx):
        """Display XMR exchange rate."""
        conn = http.client.HTTPSConnection("api.coincap.io")
        payload = ''
        headers = {}
        conn.request("GET", "/v2/assets/monero", payload, headers)
        res = conn.getresponse()
        data = res.read().decode("utf-8")
        price = json.loads(data)['data']['priceUsd']

        embed = discord.Embed(
            title="Monero",
            description=f"The Current XMR Rate Is: ${price}",
            color=discord.Color.orange(),
        )
        embed.set_thumbnail(
            url="https://s2.coinmarketcap.com/static/img/coins/200x200/328.png"
        )
        await ctx.send(embed=embed)


def setup(client):
    """Load cog."""
    client.add_cog(XMR(client))
