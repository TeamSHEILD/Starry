import random
import discord
import urllib
import secrets
import asyncio
import aiohttp
import re
from io import BytesIO
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def f(self, ctx, *, member : discord.Member):
        hearts = ['❤', '💛', '💚', '💙', '💜']
        embed = discord.Embed(title = f"**{ctx.author.name}** has paid their respect for {member.name}{random.choice(hearts)}", color=random.randint(0, 16777215))
        await ctx.send(embed = embed)



    @commands.command()
    async def hotmeter(self, ctx, *, user: discord.Member = None):
        """ Returns a random percent for how hot is a discord user """
        user = user or ctx.author

        random.seed(user.id)
        r = random.randint(1, 100)
        hot = r / 1.17

        emoji = "💔"
        if hot > 25:
            emoji = "❤"
        if hot > 50:
            emoji = "💖"
        if hot > 75:
            emoji = "💞"

        embed = discord.Embed(title = f"**{user.name}** is **{hot:.2f}%** hot {emoji}", color=random.randint(0, 16777215))
        await ctx.send(embed = embed)

    @commands.command()
    async def slots(self, ctx):
        emojis = "🍩🍪🧁🍰🎂🍫🍭"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)

        slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"

        if (a == b == c):
            embed = discord.Embed(title = f"{slotmachine} All of it is matching, so you win! 🎉", color=random.randint(0, 16777215))
            await ctx.send(embed = embed)
        elif (a == b) or (a == c) or (b == c):
            embed = discord.Embed(title = f"{slotmachine} 2 in a row, good enough, you win! 🎉", color=random.randint(0, 16777215))
            await ctx.send(embed = embed)
        else:
            embed = discord.Embed(title = f"{slotmachine} No match, you lost 😢. Press F for respects", color=random.randint(0, 16777215))
            await ctx.send(embed = embed)


def setup(client):
    client.add_cog(Fun(client))
