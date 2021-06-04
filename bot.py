import discord
import random
import requests
import wikipedia
from discord.ext import commands
from hacker_news import hacker_news_run
import os
import dotenv


dotenv.load_dotenv()
discord_token = os.environ.get("DISCORD_TOKEN")


client = commands.Bot(command_prefix=">", case_insensitive=True)
client.remove_command("help")

# Confirms start, and sets status
@client.event
async def on_ready():
    await client.change_presence(
        status=discord.Status.online,
        activity=discord.Game("with FBI crime statistics"),
    )
    print(f"{client.user} is ready")


# XMR command
@client.command(name="xmr")
async def _XMR(ctx):
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
    await ctx.channel.send(embed=embed)


# BTC command
@client.command(name="btc")
async def _BTC(ctx):
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
    await ctx.channel.send(embed=embed)


# ETH command
@client.command(name="eth")
async def _ETH(ctx):
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
    await ctx.channel.send(embed=embed)


# IPLookup command
@client.command(name="iplookup")
async def _iplookup(ctx, arg):
    IP = arg
    r = requests.get("https://check-host.net/ip-info?host=" + IP).text
    ISP = (
        r.split("<td>ISP</td>")[1]
        .split("<td")[1]
        .split("</td>")[0]
        .replace("\n", "")
    )
    COUNTRY = (
        r.split("<td>Country</td>")[1]
        .split("<strong")[1]
        .split("</strong>")[0]
        .replace("\n", "")
    )
    REGION = (
        r.split("<td>Region</td>")[1]
        .split("<td")[1]
        .split("</td>")[0]
        .replace("\n", "")
    )
    CITY = (
        r.split("<td>City</td>")[1]
        .split("<td")[1]
        .split("</td>")[0]
        .replace("\n", "")
    )
    TIMEZONE = (
        r.split("<td>Time zone</td>")[1]
        .split("<td")[1]
        .split("</td>")[0]
        .replace("\n", "")
    )
    LOCALTIME = (
        r.split("<td>Local time</td>")[1]
        .split("<td")[1]
        .split("</td>")[0]
        .replace("\n", "")
    )
    embed = discord.Embed(
        title=f"**:white_check_mark: IP lookup results for {IP}**",
        description=f"{ISP}\n {COUNTRY}\n {REGION}\n {CITY}\n {TIMEZONE}\n {LOCALTIME}\n",
        color=discord.Color.red(),
    )
    await ctx.channel.send(embed=embed)


# Wikipedia command
@client.command(name="wikipedia", aliases=["wiki"])
async def _wikipedia(ctx, *, arg):
    search = arg

    try:
        page_content = wikipedia.page(search)
        page_text = wikipedia.summary(search, sentences=5)

        try:
            thumbnail = page_content.images[
                random.randint(0, len(page_content.images))
            ]

        except:
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

        print(error)
        RandomErrorMessage = "Sorry, a random error occured"
        embed = discord.Embed(
            title="Error", color=0x992D22, description=RandomErrorMessage
        )
        embed.set_thumbnail(
            url="https://www.wikipedia.org/static/images/project-logos/enwiki.png"
        )
        await ctx.send(embed=embed)


# News command
@client.command(name="news")
async def _news(ctx):
    if ctx.author.id == 237415091320913921:
        hacker_news_run()
    else:
        await ctx.send("You lack the permissions to use this command")


if __name__ == "__main__":

    if discord_token:
        client.run(discord_token)
    else:
        print("Please set your discord token in .env file")
