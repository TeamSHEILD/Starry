import random
import requests
import discord
import asyncio
from discord.ext import commands

class Giveaway(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def fivesecgive(self, ctx, amount: int=1, *, prize:str):
      users = []
      embed = discord.Embed(title = '🎉 GIVEAWAY! 🎉',color = 0xff6f70)
      embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/737006339619815535.gif?v=1')
      embed.set_footer(text = f'Hosted by {ctx.author.name}')
      embed.add_field(name = '🎉 Come and Join!', value = f'Prize : {prize}\nRunning Time : 5 seconds!\nWinners : {amount} of you (lucky) people')
      await ctx.send(embed = embed)

      await asyncio.sleep(5)

      embed = discord.Embed(title = '🎉 The GIVEAWAY! has ended🎉',color = 0xff6f70)
      embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/737006339619815535.gif?v=1')
      embed.set_footer(text = f'Thank you {ctx.author.name}!!')
      embed.add_field(name = '🎉 A Reminder of the prize!', value = f'Prize : {prize}', inline = False)
      embed.add_field(name = 'So what happens now?', value='The results are DM\'ed to Serenity, and the randomizer picks who wins!', inline = False)
      await ctx.send(embed = embed)

      await ctx.author.create_dm()
      await ctx.author.dm_channel.send(f'Hey {ctx.author.mention}, the giveaway has ended! Go announce a winner in the giveaway channel!!')

    @commands.command()
    async def fivemingive(self, ctx, amount: int=1, *, prize:str):
      users = []
      embed = discord.Embed(title = '🎉 GIVEAWAY! 🎉',color = 0xff6f70)
      embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/737006339619815535.gif?v=1')
      embed.set_footer(text = f'Hosted by {ctx.author.name}')
      embed.add_field(name = '🎉 Come and Join!', value = f'Prize : {prize}\nRunning Time : 5 minutes!\nWinners : {amount} of you (lucky) people')
      await ctx.send(embed = embed)

      await asyncio.sleep(300)

      embed = discord.Embed(title = '🎉 The GIVEAWAY! has ended🎉',color = 0xff6f70)
      embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/737006339619815535.gif?v=1')
      embed.set_footer(text = f'Thank you {ctx.author.name}!!')
      embed.add_field(name = '🎉 A Reminder of the prize!', value = f'Prize : {prize}', inline = False)
      embed.add_field(name = 'So what happens now?', value='The results are DM\'ed to Serenity, and the randomizer picks who wins!', inline = False)
      await ctx.send(embed = embed)

      await ctx.author.create_dm()
      await ctx.author.dm_channel.send(f'Hey {ctx.author.mention}, the giveaway has ended! Go announce a winner in the giveaway channel!!')

    @commands.command()
    async def tenmingive(self, ctx, amount: int=1, *, prize:str):
      users = []
      embed = discord.Embed(title = '🎉 GIVEAWAY! 🎉',color = 0xff6f70)
      embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/737006339619815535.gif?v=1')
      embed.set_footer(text = f'Hosted by {ctx.author.name}')
      embed.add_field(name = '🎉 Come and Join!', value = f'Prize : {prize}\nRunning Time : 10 minutes!\nWinners : {amount} of you (lucky) people')
      await ctx.send(embed = embed)

      await asyncio.sleep(600)

      embed = discord.Embed(title = '🎉 The GIVEAWAY! has ended🎉',color = 0xff6f70)
      embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/737006339619815535.gif?v=1')
      embed.set_footer(text = f'Thank you {ctx.author.name}!!')
      embed.add_field(name = '🎉 A Reminder of the prize!', value = f'Prize : {prize}', inline = False)
      embed.add_field(name = 'So what happens now?', value='The results are DM\'ed to Serenity, and the randomizer picks who wins!', inline = False)
      await ctx.send(embed = embed)

      await ctx.author.create_dm()
      await ctx.author.dm_channel.send(f'Hey {ctx.author.mention}, the giveaway has ended! Go announce a winner in the giveaway channel!!')

    @commands.command()
    async def thirtymingive(self, ctx, amount: int=1, *, prize:str):
      users = []
      embed = discord.Embed(title = '🎉 GIVEAWAY! 🎉',color = 0xff6f70)
      embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/737006339619815535.gif?v=1')
      embed.set_footer(text = f'Hosted by {ctx.author.name}')
      embed.add_field(name = '🎉 Come and Join!', value = f'Prize : {prize}\nRunning Time : 30 minutes!\nWinners : {amount} of you (lucky) people')
      await ctx.send(embed = embed)

      await asyncio.sleep(1800)

      embed = discord.Embed(title = '🎉 The GIVEAWAY! has ended🎉',color = 0xff6f70)
      embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/737006339619815535.gif?v=1')
      embed.set_footer(text = f'Thank you {ctx.author.name}!!')
      embed.add_field(name = '🎉 A Reminder of the prize!', value = f'Prize : {prize}', inline = False)
      embed.add_field(name = 'So what happens now?', value='The results are DM\'ed to Serenity, and the randomizer picks who wins!', inline = False)
      await ctx.send(embed = embed)

      await ctx.author.create_dm()
      await ctx.author.dm_channel.send(f'Hey {ctx.author.mention}, the giveaway has ended! Go announce a winner in the giveaway channel!!')

    @commands.command()
    async def onehrgive(self, ctx, amount: int=1, *, prize:str):
      users = []
      embed = discord.Embed(title = '🎉 GIVEAWAY! 🎉',color = 0xff6f70)
      embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/737006339619815535.gif?v=1')
      embed.set_footer(text = f'Hosted by {ctx.author.name}')
      embed.add_field(name = '🎉 Come and Join!', value = f'Prize : {prize}\nRunning Time : 1 hour!\nWinners : {amount} of you (lucky) people')
      await ctx.send(embed = embed)

      await asyncio.sleep(3600)

      embed = discord.Embed(title = '🎉 The GIVEAWAY! has ended🎉',color = 0xff6f70)
      embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/737006339619815535.gif?v=1')
      embed.set_footer(text = f'Thank you {ctx.author.name}!!')
      embed.add_field(name = '🎉 A Reminder of the prize!', value = f'Prize : {prize}', inline = False)
      embed.add_field(name = 'So what happens now?', value='The results are DM\'ed to Serenity, and the randomizer picks who wins!', inline = False)
      await ctx.send(embed = embed)

      await ctx.author.create_dm()
      await ctx.author.dm_channel.send(f'Hey {ctx.author.mention}, the giveaway has ended! Go announce a winner in the giveaway channel!!')

    @commands.command()
    async def twohrgive(self, ctx, amount: int=1, *, prize:str):
      users = []
      embed = discord.Embed(title = '🎉 GIVEAWAY! 🎉',color = 0xff6f70)
      embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/737006339619815535.gif?v=1')
      embed.set_footer(text = f'Hosted by {ctx.author.name}')
      embed.add_field(name = '🎉 Come and Join!', value = f'Prize : {prize}\nRunning Time : 2 hours!\nWinners : {amount} of you (lucky) people')
      await ctx.send(embed = embed)

      await asyncio.sleep(7200)

      embed = discord.Embed(title = '🎉 The GIVEAWAY! has ended🎉',color = 0xff6f70)
      embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/737006339619815535.gif?v=1')
      embed.set_footer(text = f'Thank you {ctx.author.name}!!')
      embed.add_field(name = '🎉 A Reminder of the prize!', value = f'Prize : {prize}', inline = False)
      embed.add_field(name = 'So what happens now?', value='The results are DM\'ed to Serenity, and the randomizer picks who wins!', inline = False)
      await ctx.send(embed = embed)

      await ctx.author.create_dm()
      await ctx.author.dm_channel.send(f'Hey {ctx.author.mention}, the giveaway has ended! Go announce a winner in the giveaway channel!!')

    @commands.command()
    async def threehrgive(self, ctx, amount: int=1, *, prize:str):
      users = []
      embed = discord.Embed(title = '🎉 GIVEAWAY! 🎉',color = 0xff6f70)
      embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/737006339619815535.gif?v=1')
      embed.set_footer(text = f'Hosted by {ctx.author.name}')
      embed.add_field(name = '🎉 Come and Join!', value = f'Prize : {prize}\nRunning Time : 3 hours!\nWinners : {amount} of you (lucky) people')
      await ctx.send(embed = embed)

      await asyncio.sleep(10800)

      embed = discord.Embed(title = '🎉 The GIVEAWAY! has ended🎉',color = 0xff6f70)
      embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/737006339619815535.gif?v=1')
      embed.set_footer(text = f'Thank you {ctx.author.name}!!')
      embed.add_field(name = '🎉 A Reminder of the prize!', value = f'Prize : {prize}', inline = False)
      embed.add_field(name = 'So what happens now?', value='The results are DM\'ed to Serenity, and the randomizer picks who wins!', inline = False)
      await ctx.send(embed = embed)

      await ctx.author.create_dm()
      await ctx.author.dm_channel.send(f'Hey {ctx.author.mention}, the giveaway has ended! Go announce a winner in the giveaway channel!!')

    @commands.command()
    async def sixhrgive(self, ctx, amount: int=1, *, prize:str):
      users = []
      embed = discord.Embed(title = '🎉 GIVEAWAY! 🎉',color = 0xff6f70)
      embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/737006339619815535.gif?v=1')
      embed.set_footer(text = f'Hosted by {ctx.author.name}')
      embed.add_field(name = '🎉 Come and Join!', value = f'Prize : {prize}\nRunning Time : 6 hours!\nWinners : {amount} of you (lucky) people')
      await ctx.send(embed = embed)

      await asyncio.sleep(21600)

      embed = discord.Embed(title = '🎉 The GIVEAWAY! has ended🎉',color = 0xff6f70)
      embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/737006339619815535.gif?v=1')
      embed.set_footer(text = f'Thank you {ctx.author.name}!!')
      embed.add_field(name = '🎉 A Reminder of the prize!', value = f'Prize : {prize}', inline = False)
      embed.add_field(name = 'So what happens now?', value='The results are DM\'ed to Serenity, and the randomizer picks who wins!', inline = False)
      await ctx.send(embed = embed)

      await ctx.author.create_dm()
      await ctx.author.dm_channel.send(f'Hey {ctx.author.mention}, the giveaway has ended! Go announce a winner in the giveaway channel!!')

    @commands.command()
    async def twelvehrgive(self, ctx, amount: int=1, *, prize:str):
      users = []
      embed = discord.Embed(title = '🎉 GIVEAWAY! 🎉',color = 0xff6f70)
      embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/737006339619815535.gif?v=1')
      embed.set_footer(text = f'Hosted by {ctx.author.name}')
      embed.add_field(name = '🎉 Come and Join!', value = f'Prize : {prize}\nRunning Time : 12 hours!\nWinners : {amount} of you (lucky) people')
      await ctx.send(embed = embed)

      await asyncio.sleep(43200)

      embed = discord.Embed(title = '🎉 The GIVEAWAY! has ended🎉',color = 0xff6f70)
      embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/737006339619815535.gif?v=1')
      embed.set_footer(text = f'Thank you {ctx.author.name}!!')
      embed.add_field(name = '🎉 A Reminder of the prize!', value = f'Prize : {prize}', inline = False)
      embed.add_field(name = 'So what happens now?', value='The results are DM\'ed to Serenity, and the randomizer picks who wins!', inline = False)
      await ctx.send(embed = embed)

      await ctx.author.create_dm()
      await ctx.author.dm_channel.send(f'Hey {ctx.author.mention}, the giveaway has ended! Go announce a winner in the giveaway channel!!')

    @commands.command()
    async def onedaygive(self, ctx, amount: int=1, *, prize:str):
      users = []
      embed = discord.Embed(title = '🎉 GIVEAWAY! 🎉',color = 0xff6f70)
      embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/737006339619815535.gif?v=1')
      embed.set_footer(text = f'Hosted by {ctx.author.name}')
      embed.add_field(name = '🎉 Come and Join!', value = f'Prize : {prize}\nRunning Time : 1 day!\nWinners : {amount} of you (lucky) people')
      await ctx.send(embed = embed)

      await asyncio.sleep(43200)

      embed = discord.Embed(title = '🎉 The GIVEAWAY! has ended🎉',color = 0xff6f70)
      embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/737006339619815535.gif?v=1')
      embed.set_footer(text = f'Thank you {ctx.author.name}!!')
      embed.add_field(name = '🎉 A Reminder of the prize!', value = f'Prize : {prize}', inline = False)
      embed.add_field(name = 'So what happens now?', value='The results are DM\'ed to Serenity, and the randomizer picks who wins!', inline = False)
      await ctx.send(embed = embed)

      await ctx.author.create_dm()
      await ctx.author.dm_channel.send(f'Hey {ctx.author.mention}, the giveaway has ended! Go announce a winner in the giveaway channel!!')

    @commands.command()
    async def twodaygive(self, ctx, amount: int=1, *, prize:str):
      users = []
      embed = discord.Embed(title = '🎉 GIVEAWAY! 🎉',color = 0xff6f70)
      embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/737006339619815535.gif?v=1')
      embed.set_footer(text = f'Hosted by {ctx.author.name}')
      embed.add_field(name = '🎉 Come and Join!', value = f'Prize : {prize}\nRunning Time : 2 days!\nWinners : {amount} of you (lucky) people')
      await ctx.send(embed = embed)

      await asyncio.sleep(86400)

      embed = discord.Embed(title = '🎉 The GIVEAWAY! has ended🎉',color = 0xff6f70)
      embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/737006339619815535.gif?v=1')
      embed.set_footer(text = f'Thank you {ctx.author.name}!!')
      embed.add_field(name = '🎉 A Reminder of the prize!', value = f'Prize : {prize}', inline = False)
      embed.add_field(name = 'So what happens now?', value='The results are DM\'ed to Serenity, and the randomizer picks who wins!', inline = False)
      await ctx.send(embed = embed)

      await ctx.author.create_dm()
      await ctx.author.dm_channel.send(f'Hey {ctx.author.mention}, the giveaway has ended! Go announce a winner in the giveaway channel!!')

    @commands.command()
    async def threedaygive(self, ctx, amount: int=1, *, prize:str):
      users = []
      embed = discord.Embed(title = '🎉 GIVEAWAY! 🎉',color = 0xff6f70)
      embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/737006339619815535.gif?v=1')
      embed.set_footer(text = f'Hosted by {ctx.author.name}')
      embed.add_field(name = '🎉 Come and Join!', value = f'Prize : {prize}\nRunning Time : 3 days!\nWinners : {amount} of you (lucky) people')
      await ctx.send(embed = embed)

      await asyncio.sleep(259200)

      embed = discord.Embed(title = '🎉 The GIVEAWAY! has ended🎉',color = 0xff6f70)
      embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/737006339619815535.gif?v=1')
      embed.set_footer(text = f'Thank you {ctx.author.name}!!')
      embed.add_field(name = '🎉 A Reminder of the prize!', value = f'Prize : {prize}', inline = False)
      embed.add_field(name = 'So what happens now?', value='The results are DM\'ed to Serenity, and the randomizer picks who wins!', inline = False)
      await ctx.send(embed = embed)

      await ctx.author.create_dm()
      await ctx.author.dm_channel.send(f'Hey {ctx.author.mention}, the giveaway has ended! Go announce a winner in the giveaway channel!!')

    @commands.command()
    async def oneweekgive(self, ctx, amount: int=1, *, prize:str):
      users = []
      embed = discord.Embed(title = '🎉 GIVEAWAY! 🎉',color = 0xff6f70)
      embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/737006339619815535.gif?v=1')
      embed.set_footer(text = f'Hosted by {ctx.author.name}')
      embed.add_field(name = '🎉 Come and Join!', value = f'Prize : {prize}\nRunning Time : 1 week!\nWinners : {amount} of you (lucky) people')
      await ctx.send(embed = embed)

      await asyncio.sleep(604800)

      embed = discord.Embed(title = '🎉 The GIVEAWAY! has ended🎉',color = 0xff6f70)
      embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/737006339619815535.gif?v=1')
      embed.set_footer(text = f'Thank you {ctx.author.name}!!')
      embed.add_field(name = '🎉 A Reminder of the prize!', value = f'Prize : {prize}', inline = False)
      embed.add_field(name = 'So what happens now?', value='The results are DM\'ed to Serenity, and the randomizer picks who wins!', inline = False)
      await ctx.send(embed = embed)

      await ctx.author.create_dm()
      await ctx.author.dm_channel.send(f'Hey {ctx.author.mention}, the giveaway has ended! Go announce a winner in the giveaway channel!!')

def setup(client):
    client.add_cog(Giveaway(client))