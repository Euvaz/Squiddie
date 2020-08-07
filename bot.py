import discord
import random
from discord.ext import commands


client = commands.Bot(command_prefix='>')


# Confirms start, and sets status
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game('with FBI crime statistics'))
    print(f'{client.user} is ready')


# Nick command
@client.command(name='nick')
@commands.has_permissions(change_nickname=True)
async def _nick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention}')

# TODO Work on Role command(s)

# Role.add command
@client.group(name='role.add')
@commands.has_permissions(manage_roles=True)
async def _roleadd(ctx):
    await ctx.send('add')

# Role.remove command
@client.command(name='role.remove')
@commands.has_permissions(manage_roles=True)
async def _roleremove(ctx):
    await ctx.send('remove')


# Kick command
@client.command(name='kick')
@commands.has_permissions(kick_members=True)
async def _kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} was Kicked')


# Ban command
@client.command(name='ban')
@commands.has_permissions(ban_members=True)
async def _ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} was Banned')


# Unban command
@client.command(name='unban')
@commands.has_permissions(ban_members=True)
async def _unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_deiscriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.self.user
        if (user.name, user.discriminator) == (member_name, member_deiscriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.mention} was Unbanned')
            return


# Mute command
# TODO Finish 'mute' command
# @client.command(name='mute')
# @commands.has_role('Staff')


# Unmute command
# TODO Finish 'unmute' command
# @client.command(name='unmute')
# @commands.has_any_role('Staff')
# async def unmute(ctx):
#     pass


# PP command
@commands.cooldown(1, 5, commands.BucketType.user)
@client.command(name='pp')
async def _pp(ctx):

    await ctx.send('8' + '=' * random.randint(1, 12) + 'D')


# 8Ball command
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


client.run('NzM4MzI1NDgzOTg0Mzg4MTU3.XyKRMA.oljJyLSmH-Qo8ZoN4cfhSzdGDuM')
