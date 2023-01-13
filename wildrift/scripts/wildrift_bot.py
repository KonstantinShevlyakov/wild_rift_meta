#!usr/bin/env python3
import discord
from discord.ext import commands
import asyncio
import os
from wildrift.scripts.get_meta import get_splus_tier

TOKEN =

bot = commands.Bot(intents=discord.Intents.all(), command_prefix='$')

@bot.command (pass_context=True)
async def test(ctx, arg):
    await ctx.send(arg)
    

@bot.command(pass_context=True)
async def meta(ctx):
    await ctx.send(get_splus_tier())
 
bot.run(TOKEN)