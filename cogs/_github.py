"""Class file for Github."""

import discord
from discord.ext import commands
from github import Github
import os


class _Github(commands.Cog):
    """Github class."""

    def __init__(self, client, git):
        """Initialize"""
        self.client = client
        self.git = git

    # Github command
    @commands.command(name="git", aliases=["github"])
    async def _github(self, ctx, *, arg):

        search = arg.split(' ')[0]
        count = 5

        try:
            count = int(arg.split(' ')[1])
            if count > 10:
                count = 10
            elif count <= 0:
                count = 5

        except IndexError:
            count = 5

        except ValueError:
            await ctx.send("Please enter a type (int) for the second field")

        result = self.git.search_repositories(search, 'stars', 'desc')

        repos = []
        urls = []
        for repo in result[:count]:
            repos.append(repo.name)
            urls.append(repo.clone_url)

        listings = []
        for repo, url in zip(repos, urls):
            listings.append("[{}]({})".format(repo, url))

        listings_joined = "\n".join(listings)

        embed = discord.Embed(
            title="Github: {}".format(search),
            color=0x853DE4,
            description="Listing results for \"{}\"".format(search)
        )
        embed.add_field(name="Top {} Search Results".format(count), value=listings_joined)

        await ctx.send(embed=embed)


# Initializing Github with token
github_token = os.environ.get("GIT_TOKEN")
g = Github(github_token)


def setup(client):
    """Load cog."""
    client.add_cog(_Github(client, g))
