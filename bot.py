"""Main bot code for Squiddie."""

from discord.ext import commands
import logging
import os
import dotenv


# Configure Logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename='discord.log',
    encoding='utf-8',
    mode='w')
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


# Load .env variables
dotenv.load_dotenv()
discord_token = os.environ.get("DISCORD_TOKEN")


# Initialize bot
PREFIX = "!sq "
client = commands.Bot(command_prefix=PREFIX, case_insensitive=True)
#client.remove_command("help")


# Load cogs
@client.command()
async def load(ctx, extension):
    """Load cogs."""
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    """Unload cogs."""
    client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


if __name__ == "__main__":

    if discord_token:
        client.run(discord_token)
    else:
        print("Please set your discord token in .env file")
