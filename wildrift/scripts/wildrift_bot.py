#!usr/bin/env python3
import discord
from discord.ext import commands
import asyncio

TOKEN = #'MTA2MzQ5MTkxODk1ODQ0NDU2NQ.GGO5iK.JGKWAuI0rlKn9YGtwZnbaJHJ4eFA3sPPjrtABo'

bot = commands.Bot(intents=discord.Intents.all(), command_prefix='$')

@bot.command (pass_context=True)
async def test(ctx, arg):
    await ctx.send(arg)
    
    
bot.run(TOKEN)