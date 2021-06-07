"""Main bot code for Chimpanzino."""

from discord.ext import commands
import os
import dotenv


dotenv.load_dotenv()
discord_token = os.environ.get("DISCORD_TOKEN")


client = commands.Bot(command_prefix="!ch ", case_insensitive=True)
client.remove_command("help")


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
