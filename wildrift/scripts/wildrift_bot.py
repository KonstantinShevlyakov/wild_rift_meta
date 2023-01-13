#!usr/bin/env python3
import discord
from discord.ext import commands
import asyncio
import os

TOKEN =

bot = commands.Bot(intents=discord.Intents.all(), command_prefix='$')

@bot.command (pass_context=True)
async def test(ctx, arg):
    await ctx.send(arg)
    
    
bot.run(TOKEN)