import discord
import random
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

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


@commands.cooldown(1, 5, commands.BucketType.user)
@client.command()
async def pp(ctx):
    i = random.randint(1, 10)

    def pp_length(x):
        length = {
                1: '=',
                2: '==',
                3: '===',
                4: '====',
                5: '=====',
                6: '======',
                7: '=======',
                8: '========',
                9: '=========',
                10: '==========',
                11: '===========',
                12: '============'
        }
        return length.get(x, "Invalid Length")

    await ctx.send('8' + pp_length(i) + 'D')

client.run('NzM4MzI1NDgzOTg0Mzg4MTU3.XyKRMA.WN99uZQVN0cyYSq8RwnQz7oIuCI')
