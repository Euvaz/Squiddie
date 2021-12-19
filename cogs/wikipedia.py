"""Class file for Wikipedia."""

import discord
from discord.ext import commands
import random
import wikipedia


class Wikipedia(commands.Cog):
    """Wikipedia class."""

    def __init__(self, client):
        """Initialize."""
        self.client = client

    # Wikipedia command
    @commands.command(name="wiki", aliases=["wikipedia"])
    async def wikipedia(self, ctx, *, arg):
        search = arg

        try:
            page_content = wikipedia.page(search)
            page_text = wikipedia.summary(search, sentences=5)

            try:
                thumbnail = page_content.images[
                    random.randint(0, len(page_content.images))
                ]

            except wikipedia.WikipediaException:
                thumbnail = "https://www.wikipedia.org/static/images/project-logos/enwiki.png"

            embed = discord.Embed(
                title=search,
                color=0x853DE4,
                description=page_text
                            + "\n\n[Read further]({})".format(page_content.url),
            )
            embed.set_thumbnail(url=thumbnail)
            await ctx.send(embed=embed)

        except wikipedia.DisambiguationError:

            NotSpecificRequestErrorMessage = "Sorry, your search request wasn't specific enough. Please see the related search items provided"
            embed = discord.Embed(
                title="Bad request:",
                color=0x853DE4,
                description=NotSpecificRequestErrorMessage,
            )

            search_results = wikipedia.search(search, results=10, suggestion=False)
            search_results_joined = "\n".join(search_results)

            embed.add_field(name="Related Searches:", value=search_results_joined)
            embed.set_thumbnail(
                url="https://www.wikipedia.org/static/images/project-logos/enwiki.png"
            )
            await ctx.send(embed=embed)

        except wikipedia.PageError:

            NoResultErrorMessage = "Sorry, no matching Wikipedia articles could be found with that title. Please see the related search items provided"
            embed = discord.Embed(
                title="Not found:",
                color=0x853DE4,
                description=NoResultErrorMessage,
            )

            search_results = wikipedia.search(search, results=10, suggestion=False)
            search_results_joined = "\n".join(search_results)

            embed.add_field(name="Related Searches:", value=search_results_joined)
            embed.set_thumbnail(
                url="https://www.wikipedia.org/static/images/project-logos/enwiki.png"
            )
            await ctx.send(embed=embed)

        except Exception as error:

            RandomErrorMessage = "Sorry, a random error occurred"
            embed = discord.Embed(
                title="Error", color=0x992D22, description=RandomErrorMessage
            )
            embed.set_thumbnail(
                url="https://www.wikipedia.org/static/images/project-logos/enwiki.png"
            )
            await ctx.send(embed=embed)


def setup(client):
    """Load cog."""
    client.add_cog(Wikipedia(client))
