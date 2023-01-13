import discord
from discord.ext import commands

TOKEN = 'MTA2MzQ5MTkxODk1ODQ0NDU2NQ.GGO5iK.JGKWAuI0rlKn9YGtwZnbaJHJ4eFA3sPPjrtABo'

bot = commands.Bot(command_prefix='$')

@bot.command (pass_context=True)
async def test(ctx, arg):
    await ctx.send(arg)
    
    
bot.run(TOKEN)