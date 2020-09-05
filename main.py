#Admin Perms:
#https://discord.com/api/oauth2/authorize?client_id=742030317451214888&permissions=8&scope=bot

#Non-Admin Perms:
#https://discord.com/api/oauth2/authorize?client_id=742030317451214888&permissions=2080767094&scope=bot

import discord
from discord.ext import commands, tasks
import os
import lavalink
import B
import asyncio
import discord.utils
import random
import youtube_dl
import datetime
import time
import piclinks
import json
import aiohttp
import sqlite3
import pymongo
import discord_webhook
from difflib import SequenceMatcher
from discord import Webhook, AsyncWebhookAdapter
import tweepy
import youtube_dl
import itertools
import functools
import math
from async_timeout import timeout
from pymongo import MongoClient
from datetime import *
import math
from pytz import timezone
from async_timeout import timeout
today = datetime.today()
day = today.strftime('%m/%d/%Y %H:%M:%S')
coin = ["Heads", "Tails", "Heads", "Tails", "Heads", "Tails", "Heads", "Tails","HA! The coin fell off the table! No one wins! (or loses....)"]
flip = coin[random.randint(0, 8)]
key = os.getenv('key')
wkey = os.getenv('wkey')
client = discord.Client()
client = commands.Bot(command_prefix=commands.when_mentioned_or("star+"))
client.remove_command("help")
discordprefix = "star+"
time_location = "America/New_York"

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_ready():
	print('Logged in as:')
	print("Username:", client.user.name + " #9492")
	print("Client ID:", client.user.id)
	print("Bot Creator: Shadi#7894")
	print(today)
	print('-----------------------------')
	await client.change_presence(status=discord.Status.online,activity=discord.Activity(type=discord.ActivityType.streaming, name=" star+help | DM"))

@client.command()
async def simpltime(ctx):
  embed = discord.Embed(title=day, color=0x10deb0)
  message = await ctx.send(embed=embed)
  await message.add_reaction('⌚')


@client.command()
@commands.has_permissions(administrator=True)
async def changenickname(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    embed = discord.Embed(title = "Nickname Successfully Changed!", color=random.randint(0, 16777215))
    embed.add_field(name = "Original Name", value = f"{member.name}")
    embed.add_field(name = "New Nickname", value = f"{member.mention}")
    message = await ctx.send(embed=embed)
    await message.add_reaction('📝')
    
@client.command()
async def parrot(ctx, *, mssg=None):
  if mssg == None:
    embed = discord.Embed(title="🦜 Parrot Starry", color=random.randint(0, 16777215))
    embed.add_field(name="Slight Problem...", value='hmm whattya want me to copy?')
    await ctx.send(embed=embed)
  else:
    embed = discord.Embed(title="🦜 Parrot Starry", color=random.randint(0, 16777215))
    embed.add_field(name="now gimme cracker pls 🍘", value=f'{mssg}')
    message = await ctx.send(embed=embed)
    await message.add_reaction('🍘')
    await message.add_reaction('🦜')

@client.command()
async def serverpop(ctx):
  embed = discord.Embed(title='🏭 Server Population', color=random.randint(0, 16777215))
  embed.add_field(name='How many members are in this server? (bots included)',value=f'There are {ctx.guild.member_count} members (including bots) in this server')
  message = await ctx.send(embed=embed)
  await message.add_reaction('🏭')

@client.command()
async def feedback(ctx, *, mssg=None):
  if mssg == None:
    embed = discord.Embed(title="Send feedback", color=random.randint(0, 16777215))
    embed.add_field(name="Slight Problem...", value='hmm whattya want to feedback on?')
    await ctx.send(embed=embed)
  else:
    message = await ctx.send(f'{ctx.author}, your feedback on me has been sent!')
    await message.add_reaction('👏')
    await ctx.send("If you would like to contact the owner directly, he is open! <@717822288375971900>")
    channel = client.get_channel(738792718964359340)
    embed = discord.Embed(title="We have feedback!", color=random.randint(0, 16777215))
    embed.add_field(name=f'''{ctx.author} from {ctx.guild.name} says...''',value=f'{mssg}')
    await channel.send(embed=embed)

@client.command()
async def ping(ctx):
  embed = discord.Embed(title="📡 Ping Latency", color=random.randint(0, 16777215))
  embed.add_field(name="📡",value=f'This is my ping -> ({round(client.latency * 10000)})ms')
  message = await ctx.send(embed=embed)
  await message.add_reaction('📡')

@client.command()
async def reverse(ctx, *, mssg=None):
  if mssg == None:
    embed = discord.Embed(title="🔄 Reverse that!", color=random.randint(0, 16777215))
    embed.add_field(name="hmmm", value='gimme something to reverse!')
    await ctx.send(embed=embed)
  else:
    embed = discord.Embed(title="🔄 Reverse that!", color=random.randint(0, 16777215))
    embed.add_field(name="Pop poP", value=f'{mssg}' [::-1])
    message = await ctx.send(embed=embed)
    await message.add_reaction('🔄')


@client.command()
async def human(ctx, *, mssg=None, amount=1):
	if mssg == None:
		embed = discord.Embed(title="🙍‍♂️ Human Bot", color=random.randint(0, 16777215))
		embed.add_field(name="hey wait a minute!", value="I can't ghost your message if you don't give me one!")
		await ctx.send(embed=embed)
	else:
		await ctx.channel.purge(limit=amount)
		await ctx.send(f'{mssg}')

@client.command()
async def uptime(ctx):
  await ctx.send(f'Under work')

@client.command()
async def about(ctx):
	embed = discord.Embed(title="All about Starry!!", color=random.randint(0, 16777215))
	embed.add_field(name="I am Serenity's favored creation 😋",value="**Bot Name:** Starry\n**Creator:** Shadi#7894\n**Programming Language:** Python 3.8\n**Date Created:** June 7th, 2020 | 14:30:00 PM\n **Purpose:** it's a fun bot, so it doesn't use moderation, and is still in the making, but hopefully  𝑺𝒕𝒂𝒓𝒓𝒚 adds a passive, customized feel to any server that it is in!\nIt can do very basic stuff, but if you want more features, DM 'Shadi#7894', I'm always open to some nice feedback!")
	await ctx.send(embed=embed)

  
@client.event
async def on_command_error(ctx, error):
  embed = discord.Embed(title="❗ Error ❗", color=0xA90000)
  embed.add_field(name="Uh oh...", value=f'{error}')
  message = await ctx.send(embed=embed)
  await message.add_reaction('❗')

@client.command()
async def time(ctx):
  embed = discord.Embed(title="⌚ Time in Coordinated Universal Time", color=random.randint(0, 16777215))
  embed.add_field(name="Time (UTC):", value=today)
  message = await ctx.send(embed=embed)
  await message.add_reaction('⌚')


@client.command()
async def grade(ctx):
  gr = random.randint(1, 100)
  if gr < 50:
    embed = discord.Embed(title="📝 You take a test and...", color=0xFF4242)
    embed.set_footer(text=f"Bruh {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.add_field(name="YOU FAILED!!", value=gr)
    message = await ctx.send(embed=embed)
    await message.add_reaction('🔴')
  elif gr < 70 and gr > 51:
    embed = discord.Embed(title="📝 You take a test and...", color=0xFF7542)
    embed.set_footer(text=f"Oh jeez {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.add_field(name="Lol your baaaaddd 🤣", value=gr)
    message = await ctx.send(embed=embed)
    await message.add_reaction('🟠')
  elif gr < 90 and gr > 71:
    embed = discord.Embed(title="📝 You take a test and...", color=0xFFBD42)
    embed.set_footer(text=f"... {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.add_field(name="you did quite average", value=gr)
    message = await ctx.send(embed=embed)
    await message.add_reaction('🟡')
  elif gr < 99 and gr > 91:
    embed = discord.Embed(title="📝 You take a test and...", color=0x82FF42)
    embed.set_footer(text=f"Sweet {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.add_field(name="ayyeee you did sweet!", value=gr)
    message = await ctx.send(embed=embed)
    await message.add_reaction('🟢')
  elif gr == 100:
    embed = discord.Embed(title="📝 You take a test and...", color=0x9B42FF)
    embed.set_footer(text=f"WOW {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.add_field(name="YOU GOT A HUNDRED!!! 🥳", value=gr)
    message = await ctx.send(embed=embed)
    await message.add_reaction('🟣')

@client.command()
async def flip(ctx):
	flip = coin[random.randint(0, 8)]
	await ctx.send("I hope you betted beforehand! 😋")
	await asyncio.sleep(2)
	await ctx.send("Flipping...")
	await asyncio.sleep(3)
	await ctx.send("Okay, the flip is in! The Dollar says:")
	await asyncio.sleep(1)
	await ctx.send(flip)

@client.command()
@commands.has_permissions(manage_channels=True)
async def chanmute(ctx, user: discord.Member):
    if not user:
        return await ctx.send("Who do you want to mute from only this channel?")
    await ctx.channel.set_permissions(user, send_messages=False)
    await ctx.send(f'{user} has been muted in this channel alone.')

@client.command()
@commands.has_permissions(manage_channels=True)
async def unchanmute(ctx, user: discord.Member):
    if not user:
      return await ctx.send("Who do you want to unmute?")
    await ctx.channel.set_permissions(user, send_messages=True)
    await ctx.send(f'{user} has been unmuted in this channel.')

@client.command()
async def corny(ctx):
	co = ['What is the best day to go to the beach? Sunday, of course!',
	      'What bow can\'t be tied? A rainbow!',
	      'How does a dog stop a video? By hitting the paws button!',
	      'What did one toilet say to the other? You look flushed.',
	      'A cement mixer and a prison bus crashed on the highway. Police advise citizens to look out for a group of hardened criminals',
	      'It\'s always windy in a sports area. All those fans',
	      'What is worse than raining cats and dogs? Hailing taxis!',
	      'I used to be addicted to not showering. Luckily, I\'ve been clean for five years.',
	      'How does a farmer mend his overalls? With cabbage patches.',
	      'What did the big flower say to the little flower? Hi bud!',
	      'How many tickles does it take to get an octopus to laugh? Ten tickles.',
	      'I couldn\'t figure out why the baseball kept getting bigger. Then it hit me.',
	      'Why does Humpty Dumpty love autumn? Because he always has a great fall.',
	      'Where do hamburgers take their sweethearts on Valentine\'s Day to dance? The Meat Ball!',
	      'What time does a duck wake up? The quack of down.',
	      'Some people eat snails. They must not like fast food.',
	      'What happens to a frog\'s car when it breaks down?\nIt gets toad away.',
	      'What did the duck say when it bought lipstick?\n"Put it on my bill."',
	      ' What do you call two monkeys that share an Amazon account?\nPrime mates.',
	      'Whew, this is Shadi#7894 here, the creator of this bot. You just got saved from seeing a bunch of cringy jokes I stole from some "clean" websites 🤣🤣'
	]
	co1 = random.choice(co)
	embed = discord.Embed(title="🌽 Corny Jokes", color=random.randint(0, 16777215))
	embed.add_field(name="Ahhhh so corny!", value=co1)
	message = await ctx.send(embed=embed)

@client.command()
async def facts(ctx):
	fa = [
	    'Did you know that when ants die, they let off a unique stench only other ants can smell, and they will be attracted to the dead ant, and carry him away?',
	    'Did you know that Concorde, that supersonic plane, can burn as much fuel as the average car burns in a month, just by taxi\'ing towards the runway?'
	]

	fa1 = random.choice(fa)
	embed = discord.Embed(title="📔Random Facts", color=random.randint(0, 16777215))
	embed.add_field(name="Here's a random fact 😋", value=fa1)
	message = await ctx.send(embed=embed)



@commands.cooldown(1, 3600, commands.BucketType.user)
@client.command()
async def sushi(ctx):
	sushi = random.randint(100, 300)
	embed = discord.Embed(title="Work for that sushi! 😋", color=0xCF2A40)
	embed.add_field(name="**🍣 Sushi you earned 🍣**", value=sushi)
	message = await ctx.send(embed=embed)

@client.command()
async def swapcase(ctx, *, mssg=None):
	if mssg == None:
		await ctx.send(f'{ctx.author.mention} re-run the command and also type in something that you would like to swapcase')
	else:
		await ctx.send(f'{mssg.swapcase()}')

@client.command()
async def lower(ctx, *, mssg=None):
	if mssg == None:
		await ctx.send(f'{ctx.author.mention} re-run the command and also type in something that you would like to all lowercase')
	else:
		await ctx.send(f'{mssg.lower()}')

@client.command()
async def upper(ctx, *, mssg=None):
	if mssg == None:
		await ctx.send(f'{ctx.author.mention} re-run the command and also type in something that you would like to uppercase')
	else:
		await ctx.send(f'{mssg.upper()}')


@client.command()
@commands.has_permissions(administrator=True)
async def saymembers(ctx):
	for members in ctx.guild.members:
		await ctx.send(members)




@client.command()
async def serverinfo(ctx):
    roles = [role for role in ctx.guild.roles]
    channels = [channel for channel in ctx.guild.channels]
    embed = discord.Embed(title="Guild Info", color=random.randint(0, 16777215))
    embed.add_field(name='Server Name:',value=f'{ctx.guild.name}')
    embed.add_field(name='Server ID:',value=f'{ctx.guild.id}')
    embed.add_field(name='Server region:',value=f'{ctx.guild.region}')
    embed.add_field(name='Server Creation Date:',value=f'{ctx.guild.created_at}')
    embed.add_field(name='Server Owner:',value=f'{ctx.guild.owner}')
    embed.add_field(name='Member Count:',value=f'{ctx.guild.member_count}')
    embed.add_field(name='Amount of Channels:',value=f"{len(channels)}")
    embed.add_field(name='Amount of Roles:',value=f"{len(roles)}")
    message = await ctx.send(embed=embed)
    await message.add_reaction('📉')

@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, user: discord.Member, *, reason):
	await ctx.channel.purge(limit=amount)
	await user.kick(reason=reason)
	await ctx.send(f'{user} kicked for {reason}')

@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, user: discord.Member, *, reason):
	await user.kick(reason=reason)
	await ctx.send(f'{user} banned for {reason}')

@client.command()
async def identity(ctx, member: discord.Member):
  user = ctx.author
  playinggame = user.activity
  roles = [role for role in member.roles]
  pfp = member.avatar_url
  embed = discord.Embed(title=f'This is {member.name}',colour=member.color,timestamp=ctx.message.created_at)
  embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
  embed.set_thumbnail(url=(pfp))
  embed.add_field(name='Name:', value=f'{member.name}')
  embed.add_field(name='Discriminator:', value=f'{member.discriminator}')
  embed.add_field(name='Mention:', value=f'{member.mention}')
  embed.add_field(name='User ID:', value=f'{member.id}')
  embed.add_field(name='User Status:', value=f'{member.status}')
  embed.add_field(name="Game Status:", value=playinggame)
  embed.add_field(name=f"Roles ({len(roles)})",value=" ".join([role.mention for role in roles]),inline=False)
  await ctx.send(embed=embed)


@client.command()
async def allinfo(ctx, member: discord.Member):
  playinggame = member.activity
  roles = [role for role in member.roles]
  pfp = member.avatar_url
  embed = discord.Embed(title=f'This is {member.name}',colour=member.color,timestamp=ctx.message.created_at)
  embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
  embed.set_thumbnail(url=(pfp))
  embed.add_field(name='Name:', value=f'{member.name}', inline=False)
  embed.add_field(name='Discriminator:', value=f'{member.discriminator}', inline=False)
  embed.add_field(name='Mention:', value=f'{member.mention}', inline=False)
  embed.add_field(name='User ID:', value=f'{member.id}', inline=False)
  embed.add_field(name='User Status:', value=f'{member.status}', inline=False)
  embed.add_field(name="Game Status:", value=playinggame),
  embed.add_field(name=f"Roles ({len(roles)})",value=" ".join([role.mention for role in roles]),inline=False)
  embed.add_field(name="Account Creation Date:",value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
  embed.add_field(name="Join Date:",value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
  embed.add_field(name="Bot?", value=member.bot, inline=False)
  await ctx.send(embed=embed)


@client.command()
async def where(ctx):
  embed = discord.Embed(title="🗺️Ummm... Where am I??", color=0x00D18D)
  embed.add_field(name='Feeling lost, eh?',value=f'{ctx.author.name}, if you feel lost, dont be!\n\nYou are currently in {ctx.guild.name}!\n\nYou are in the channel called {ctx.channel.mention}!')
  message = await ctx.send(embed=embed)
  await message.add_reaction('🗺️')


import time

def time_convert(sec):
  start_time = time.time()
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60

@client.command()
async def uptimechecker(ctx):
  sec = 0
  mn = 0
  hr = 12

  while sec <= 60:
    print (str(hr).zfill(2),":",str(mn).zfill(2),":",str(sec).zfill(2))
    await ctx.send(str(hr).zfill(2))
    await ctx.send(str(mn).zfill(2))
    await ctx.send(str(sec).zfill(2))
    await ctx.send("_ _")
    time.sleep(1)
    sec+=1
    if sec == 60:
        mn+=1
        sec = 0
    if mn == 60:
    	hr+=1
    	mn = 0
    	sec = 0
    if hr == 12 and mn == 59 and sec == 59:
    	hr = 1
    	mn = 0
    	sec = 0

#---------------------------------------
anime = ['Soo cute 😋', 'Those noses....', 'Soooo Kawaii!', 'Awwwwwwwww','Those manga eyes....']
animecolor = [0xff79bf, 0xff91dc, 0xe486ff, 0xffa7e1, 0xff2586, 0xff58a2, 0xd358ff]
@client.command()
async def kawaii(ctx):
	cute = random.choice(piclinks.kawaii)
	animee = random.choice(anime)
	colora = random.choice(animecolor)
	embed = discord.Embed(title="Pure Kawaii 🥰", description=animee, color=colora)
	embed.set_image(url=cute)
	await ctx.send(embed=embed)
#---------------------------------------
turt2 = [0x00fc2b, 0x00b61f, 0x008116, 0x00530f, 0x7aff92, 0x50ff70, 0x50ffbb]
@client.command()
async def turtle(ctx):
	t1 = random.choice(piclinks.turtle)
	t3 = random.choice(turt2)

	embed = discord.Embed(title="Here is a Turtle", description='Lil Turtle', color=t3)
	embed.set_image(url=t1)
	await ctx.send(embed=embed)
#---------------------------------------
aa = [
    0xffc2c2, 0xffd7c4, 0xf5ffb6, 0xc2ffb2, 0xbdfeff, 0xd9cdff, 0xffd3f6,
    0xffaaaa, 0xffc3a5, 0xf0ff91, 0xa8ff92, 0x9ffdff, 0xbda8ff, 0xffaaee,
    0x818eff, 0xb181ff, 0xff81ab, 0x81ff9a, 0x81ffc7
]
@client.command()
async def aesthetic(ctx):
	aa2 = random.choice(piclinks.aesthetics)
	aa1 = random.choice(aa)
	embed = discord.Embed(title="Aesthetics!", description='Sooo cool', color=aa1)
	embed.set_footer(text="Kawaii! 🥰")
	embed.set_image(url=aa2)
	await ctx.send(embed=embed)
#---------------------------------------
m2 = [0xff9696, 0xf08282, 0xc33e3e, 0x801f1f, 0x4a2323, 0xde7e51]
@client.command()
async def memes(ctx):
	memes1 = random.choice(piclinks.memes)
	memes2 = random.choice(m2)
	embed = discord.Embed(title="**DANK OR NOT**", description='Very memes', color=memes2)
	embed.set_image(url=memes1)
	await ctx.send(embed=embed)
#---------------------------------------
@client.command()
async def mail(ctx,member: discord.Member,*,mssg,):
	await member.create_dm()
	await member.dm_channel.send(f'''**{ctx.author}**:\t**{mssg}**''')
#----------------------------------------
@client.command()
async def help(ctx):
  embed = discord.Embed(title = "Hello! And thanks for choosing Starry!", description = "Type in the command for a category you want, I will DM you with the command list for that specific category!", color=random.randint(0, 16777215))
  embed.add_field(name = "Fun Commnands!", value = "``star+funcom``", inline = False)
  embed.add_field(name = "Utility Commands!", value = "``star+utilitycom``", inline = False)
  embed.add_field(name = "Moderation Commands!", value = "``star+modcom``", inline = False)
  embed.add_field(name = "Invite Me/Owner Contact!", value = "``star+invown``", inline = False)
  await ctx.send(embed=embed)
  
@client.command()
async def funcom(ctx):
  await ctx.author.create_dm()
  embed = discord.Embed(title = "For Fun Commands!",description = "You want to have fun?", color=random.randint(0, 16777215))
  embed.add_field(name = "Parrot", value = "``star+parrot <message>``")
  embed.add_field(name = "Reverse", value = "``star+reverse <message>``")
  embed.add_field(name = "Human", value = "``star+human <message>``")
  embed.add_field(name = "Grade", value = "``star+grade``")
  embed.add_field(name = "Corny Joke", value = "``star+corny``")
  embed.add_field(name = "Facts", value = "``star+facts``")
  embed.add_field(name = "Sushi", value = "``star+sushi``")
  embed.add_field(name = "Meme", value = "``star+meme``")
  embed.add_field(name = "Cat", value = "``star+cat``")
  embed.add_field(name = "Dog", value = "``star+dog``")
  embed.add_field(name = "Bird", value = "``star+bird``")
  embed.add_field(name = "Trivia", value = "``star+trivia``")
  embed.add_field(name = "Turtle!", value = "``star+turtle``")
  embed.add_field(name = "Aesthetics!", value = "``star+aesthetic``")
  embed.add_field(name = "Kawaii!", value = "``star+kawaii``")
  embed.add_field(name = "Google", value = "``star+google <term>``")
  embed.add_field(name = "Twitter", value = "``star+tweet <name> <message>``")
  embed.add_field(name = "Swapcase", value = "``star+swapcase <text>``")
  embed.add_field(name = "Lowercase", value = "``star+lower <text>``")
  embed.add_field(name = "Uppercase", value = "``star+upper <text>``")
  embed.add_field(name = "Coinflip", value = "``star+flip``")
  await ctx.author.dm_channel.send(embed=embed)

@client.command()
async def utilitycom(ctx):
  embed = discord.Embed(title = "Utility Commands!",description = "Let's Get to Work!", color=random.randint(0, 16777215))
  embed.add_field(name = "SimplTime", value = "``star+simpltime``")
  embed.add_field(name = "Server Pop.", value = "``star+serverpop``")
  embed.add_field(name = "Feedback", value = "``star+feedback <message>``")
  embed.add_field(name = "Ping Latency", value = "``star+ping``")
  embed.add_field(name = "Server Info", value = "``star+serverinfo``")
  embed.add_field(name = "Identity", value = "``star+identity <member>``")
  embed.add_field(name = "All Info", value = "``star+allinfo <member>``")
  embed.add_field(name = "Where Am I?", value = "``star+where``")
  embed.add_field(name = "Mail", value = "``star+mail <member> <message>``")
  await ctx.author.dm_channel.send(embed=embed)

@client.command()
async def modcom(ctx):
  embed = discord.Embed(title = "Moderate!",description = "Have security!", color=random.randint(0, 16777215))
  embed.add_field(name = "Kick", value = "``star+kick <member> <reason>``")
  embed.add_field(name = "Ban", value = "``star+ban <member> <reason>``")
  embed.add_field(name = "Channel Mute*", value = "``star+chanmute <member>``")
  embed.add_field(name = "Channel UnMute*", value = "``star+unchanmute <member>``")
  embed.add_field(name = "Change Nickname", value = "``star+changenickname <member> <newnick>``")
  embed.add_field(name = "*Channel Muting/Unmuting",value = "The Channel Mute command **must** be run in the channel in which you want to mute the member. This muting only occurs in that channel and doesn't get taken off automatically", inline = False)
  await ctx.author.dm_channel.send(embed=embed)  

@client.command()
async def invown(ctx):
  embed = discord.Embed(title = "Invite Link Me!", description = "And contact creator!", color=random.randint(0, 16777215))
  embed.add_field(name = "Admin Perms:", value = "https://discord.com/api/oauth2/authorize?client_id=742030317451214888&permissions=8&scope=bot", inline = False)
  embed.add_field(name = "No Admin Perms:", value = "https://discord.com/api/oauth2/authorize?client_id=742030317451214888&permissions=2080767094&scope=bot", inline = False)
  embed.add_field(name = "Creator:", value = "<@717822288375971900>", inline = False)
  await ctx.author.dm_channel.send(embed=embed)


#-----------------------------------------------


B.b()
client.run(os.getenv('TOKENA'))
