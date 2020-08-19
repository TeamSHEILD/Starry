import random
import requests
import discord
from discord.ext import commands

class Google(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def google(self, ctx, *, args):
        if not ' ' in args:
            return await ctx.send(f'<http://lmgtfy.com/?q={args}&pp=1>')
        await ctx.send(f"<http://lmgtfy.com/?q={args.replace(' ', '+')}&pp=1>")


def setup(client):
    client.add_cog(Google(client))
