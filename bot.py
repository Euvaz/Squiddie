import discord
from discord.ext import commands

client = commands.Bot(command_prefix='>')


@client.event
async def on_ready():
    print(f'{client.user} is ready')


@client.command()
async def nigger(ctx):
    await ctx.send('nigger')


client.run('NzM4MzI1NDgzOTg0Mzg4MTU3.XyKRMA.70RN0HbTynGy0e964CmAw3BhijU')

