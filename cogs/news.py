"""Class file for News."""

from discord.ext import commands
from hacker_news import hacker_news_run


class News(commands.Cog):
    """News class."""

    def __init__(self, client):
        """Initialize."""
        self.client = client

    # News command
    @commands.command(name="news")
    async def _news(self, ctx):
        if ctx.author.id == 237415091320913921:
            hacker_news_run()
        else:
            await ctx.send("You lack the permissions to use this command")


def setup(client):
    """Load cog."""
    client.add_cog(News(client))
