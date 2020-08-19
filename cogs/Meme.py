import random
import requests
import discord
from discord.ext import commands

class Meme(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def cat(self, ctx):
        url = 'https://some-random-api.ml/img/cat'
        result_url = requests.get(url)
        resultjson=result_url.json()
        embed=discord.Embed(title="Kitty Kat!", description="*meow*",
        colour=discord.Colour.green())
        embed.set_image(url=resultjson['link'])
        embed.set_footer(text="Starry has found a cat for you! Adopt it?")
        await ctx.send(embed=embed)

    @commands.command()
    async def dog(self, ctx):
        url = 'https://some-random-api.ml/img/dog'
        result_url = requests.get(url)
        resultjson = result_url.json()
        embed=discord.Embed(title="D O G", description="do you want a bone?",
        colour=discord.Colour.green())
        embed.set_image(url=resultjson['link'])
        embed.set_footer(text='Starry has found a doggy for you!')
        await ctx.send(embed=embed)
    
    @commands.command()
    async def bird(self, ctx):
        await ctx.trigger_typing()
        url = 'https://some-random-api.ml/img/birb'
        result_url = requests.get(url)
        resultjson = result_url.json()
        embed = discord.Embed(title='Birdy Wirdy', description="ca caw",
        colour=discord.Colour.green())
        embed.set_image(url=resultjson['link'])
        embed.set_footer(text='Starry is a bird watcher now')
        await ctx.send(embed=embed)

    @commands.command()
    async def meme(self, ctx):
        url = 'https://some-random-api.ml/meme'
        result_url = requests.get(url)
        resultjson = result_url.json()
        embed=discord.Embed(title=resultjson['caption'], description="meme",
        colour=discord.Colour.purple())
        embed.set_image(url=resultjson['image'])
        embed.set_footer(text=f"Category: {resultjson[ 'category']}")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Meme(client))