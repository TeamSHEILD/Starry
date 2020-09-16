import discord
from discord.ext import commands
import random
import json
import random
import aiohttp
import nekos
import asyncio
import uwuify
import sqlite3 as s
import requests

class Calculator(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.session = aiohttp.ClientSession()
    
    @commands.command()
    async def addnum(self, ctx, left: int, right: int):
        embed = discord.Embed(title = left + right)
        message = await ctx.send(embed = embed)
        await message.add_reaction('➕')

    @commands.command()
    async def subnum(self, ctx, left: int, right: int):
        embed = discord.Embed(title = left - right)
        message = await ctx.send(embed = embed)
        await message.add_reaction('➖')        

    @commands.command()
    async def multnum(self, ctx, left: int, right: int):
        embed = discord.Embed(title = left*right)
        message = await ctx.send(embed = embed)
        await message.add_reaction('✖') 

    @commands.command()
    async def divnum(self, ctx, left: int, right: int):
        embed = discord.Embed(title = left/right)
        message = await ctx.send(embed = embed)
        await message.add_reaction('➗')     

def setup(client):
    client.add_cog(Calculator(client))