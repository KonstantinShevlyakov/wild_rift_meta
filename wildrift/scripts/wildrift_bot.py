#!usr/bin/env python3
import discord
from discord.ext import commands
import wildrift.scripts.get_meta as get_meta


CURRENT_META = open('wildrift/meta_files/s_tier.txt', 'r').read()
TOKEN = 'MTA2MzQ5MTkxODk1ODQ0NDU2NQ.GSHuey.rP2q8yv99wWUQekXbLXn-G3eehpa406XqWE9kc'

bot = commands.Bot(intents=discord.Intents.all(), command_prefix='!')


# @bot.command(pass_context=True)
# async def test(ctx, arg):
#     await ctx.send(arg)


@bot.command()
async def meta(ctx, *args):
    get_meta.main()
    await ctx.send(f'{CURRENT_META}')

bot.run(TOKEN)
