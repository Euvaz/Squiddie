"""Class file for IPLookup."""

import discord
from discord.ext import commands
import requests


class IPLookup(commands.Cog):
    """IPLookup class."""

    def __init__(self, client):
        """Initialize."""
        self.client = client

    # IPLookup command
    @commands.command(name="iplookup")
    async def iplookup(self, ctx, arg):
        ip = arg
        r = requests.get("https://check-host.net/ip-info?host=" + ip).text
        isp = (
            r.split("<td>ISP</td>")[1]
            .split("<td")[1]
            .split("</td>")[0]
            .replace("\n", "")
        )
        country = (
            r.split("<td>Country</td>")[1]
            .split("<strong")[1]
            .split("</strong>")[0]
            .replace("\n", "")
        )
        region = (
            r.split("<td>Region</td>")[1]
            .split("<td")[1]
            .split("</td>")[0]
            .replace("\n", "")
        )
        city = (
            r.split("<td>City</td>")[1]
            .split("<td")[1]
            .split("</td>")[0]
            .replace("\n", "")
        )
        timezone = (
            r.split("<td>Time zone</td>")[1]
            .split("<td")[1]
            .split("</td>")[0]
            .replace("\n", "")
        )
        localtime = (
            r.split("<td>Local time</td>")[1]
            .split("<td")[1]
            .split("</td>")[0]
            .replace("\n", "")
        )
        embed = discord.Embed(
            title="**:white_check_mark: IP lookup results for {}**".format(ip),
            description="{}\n ".format(isp)
            + "{}\n ".format(country)
            + "{}\n ".format(region)
            + "{}\n ".format(city)
            + "{}\n ".format(timezone)
            + "{}\n".format(localtime),
            color=discord.Color.red(),
        )
        await ctx.send(embed=embed)


def setup(client):
    """Load cog."""
    client.add_cog(IPLookup(client))
