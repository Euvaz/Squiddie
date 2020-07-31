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
@client.command(name='pp')
async def pp(ctx):
    length = random.choice(['=',
                            '==',
                            '===',
                            '====',
                            '=====',
                            '======',
                            '=======',
                            '========',
                            '=========',
                            '==========',
                            '===========',
                            '============'])

    await ctx.send('8' + length + 'D')


@commands.cooldown(1, 5, commands.BucketType.user)
@client.command(name='8ball')
async def _ball(ctx):
    await ctx.send(random.choice(['As I see it, yes.',
                                  'Ask again later.',
                                  'Better not tell you now.',
                                  'Cannot predict now.',
                                  'Concentrate and ask again.',
                                  'Don’t count on it.',
                                  'It is certain.',
                                  'It is decidedly so.',
                                  'Most likely.',
                                  'My reply is no.',
                                  'My sources say no.',
                                  'Outlook not so good.',
                                  'Outlook good.',
                                  'Reply hazy, try again.',
                                  'Signs point to yes.',
                                  'Very doubtful.',
                                  'Without a doubt.',
                                  'Yes.',
                                  'Yes – definitely.',
                                  'You may rely on it.']))

client.run('NzM4MzI1NDgzOTg0Mzg4MTU3.XyKRMA.WN99uZQVN0cyYSq8RwnQz7oIuCI')
