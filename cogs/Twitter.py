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

class Twitter(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.session = aiohttp.ClientSession()
    
    def __embed_json(self, data, key='message'):
        em = discord.Embed(color=0x1B0FDD)
        em.set_image(url=data[key]) 
        return em 
    
    @commands.command()
    @commands.cooldown(1,10, commands.BucketType.user)
    async def tweet(self, ctx, username : str, *, text : str):
        await ctx.trigger_typing()
        async with self.session.get('https://nekobot.xyz/api/imagegen?type=tweet'
                                    '&username=%s'
                                    '&text=%s' % (username, text,)) as r:
            res = await r.json()
        await ctx.send(embed=self.__embed_json(res))

  
    

def setup(client):
    client.add_cog(Twitter(client))