import discord
from discord.ext import commands
import time as t

client = commands.Bot(command_prefix='>')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('with FBI crime statistics'))
    print(f'{client.user} is ready')


@client.command()
async def kick(ctx):
    pass


@client.command()
async def ban(ctx):
    pass


@client.command()
async def mute(ctx):
    pass


client.run('NzM4MzI1NDgzOTg0Mzg4MTU3.XyKRMA.WN99uZQVN0cyYSq8RwnQz7oIuCI')
