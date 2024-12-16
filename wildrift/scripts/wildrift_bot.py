#!usr/bin/env python3
import discord
from discord.ext import commands
import wildrift.scripts.get_meta as get_meta



TOKEN = 'MTA2MzQ5MTkxODk1ODQ0NDU2NQ.GSHuey.rP2q8yv99wWUQekXbLXn-G3eehpa406XqWE9kc'

bot = commands.Bot(intents=discord.Intents.all(), command_prefix='!')


@bot.command()
async def meta(ctx, *args):
    get_meta.main()
    current_meta = open('wildrift/meta_files/s_tier.txt', 'r').read()
    await ctx.send(f'{current_meta}')


# @bot.command()
# async def build(ctx, *args):
#     get_meta.main()
#     current_meta = open('wildrift/meta_files/s_tier.txt', 'r').read()
#     await ctx.send(f'{current_meta}')


bot.run(TOKEN)
