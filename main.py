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
import DatabaseControl
import GlobalLinker
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
	print("Username:", client.user.name + " #8656")
	print("Client ID:", client.user.id)
	print("Bot Creator: Serenity#7879")
	print(today)
	print('-----------------------------')
	await client.change_presence(status=discord.Status.online,activity=discord.Activity(type=discord.ActivityType.streaming, name=" star+help"))

@client.command()
async def simpltime(ctx):
  embed = discord.Embed(title=day, color=0x10deb0)
  message = await ctx.send(embed=embed)
  await message.add_reaction('⌚')

@client.command
async def test(ctx, *args):
	retStr = str("""```css\nThis is some colored Text```""")
	embed = discord.Embed(title="Random test")
	embed.add_field(
	    name="Name field can't be colored as it seems", value=retStr)
	await ctx.send(embed=embed)

@client.command()
async def parrot(ctx, *, mssg=None):
  if mssg == None:
    embed = discord.Embed(title="🦜 Parrot Starry", color=0xE64885)
    embed.add_field(name="Slight Problem...", value='hmm whattya want me to copy?')
    await ctx.send(embed=embed)
  else:
    embed = discord.Embed(title="🦜 Parrot Starry", color=0x489AE6)
    embed.add_field(name="now gimme cracker pls 🍘", value=f'{mssg}')
    message = await ctx.send(embed=embed)
    await message.add_reaction('🍘')
    await message.add_reaction('🦜')

@client.command()
async def serverpop(ctx):
  embed = discord.Embed(title='🏭 Server Population', color=0xDD3C00)
  embed.add_field(name='How many members are in this server? (bots included)',value=f'There are {ctx.guild.member_count} members (including bots) in this server')
  message = await ctx.send(embed=embed)
  await message.add_reaction('🏭')

@client.command()
async def joinvc(ctx, channel):
	channel = ctx.message.author.voice.voice_channel
	await client.join_voice_channel(channel)

@client.command()
async def leavevc(ctx):
	guild = ctx.message.guild
	voice_client = guild.voice_client(server)
	await voice_client.disconnect()

@client.command()
async def playvc(ctx, url):
	guild = ctx.message.guild
	voice_client = guild.voice_client(server)
	player = await voice_client.create_ytdl_player(url)
	playerrs[server.id] = player
	player.start()

@client.command()
async def feedback(ctx, *, mssg=None):
  if mssg == None:
    embed = discord.Embed(title="Send feedback", color=0xE44865)
    embed.add_field(name="Slight Problem...", value='hmm whattya want to feedback on?')
    await ctx.send(embed=embed)
  else:
    message = await ctx.send(f'{ctx.author}, your feedback on me has been sent!')
    await message.add_reaction('👏')
    channel = client.get_channel(738792718964359340)
    embed = discord.Embed(title="We have feedback!", color=0x422AE6)
    embed.add_field(name=f'''{ctx.author} from {ctx.guild.name} says...''',value=f'{mssg}')
    await channel.send(embed=embed)

@client.command()
async def ping(ctx):
  embed = discord.Embed(title="📡 Ping Latency", color=0x105900)
  embed.add_field(name="📡",value=f'This is my ping -> ({round(client.latency * 10000)})ms')
  message = await ctx.send(embed=embed)
  await message.add_reaction('📡')

@client.command()
async def reverse(ctx, *, mssg=None):
  if mssg == None:
    embed = discord.Embed(title="🔄 Reverse that!", color=0xE64885)
    embed.add_field(name="hmmm", value='gimme something to reverse!')
    await ctx.send(embed=embed)
  else:
    embed = discord.Embed(title="🔄 Reverse that!", color=0x3258BF)
    embed.add_field(name="Pop poP", value=f'{mssg}' [::-1])
    message = await ctx.send(embed=embed)
    await message.add_reaction('🔄')

@client.command()
async def afk(ctx, *, mssg=None):
	if mssg == None:
		embed = discord.Embed(title="📴AFK Status", color=0xFF7034)
		embed.add_field(name="What is your AFK Status?", value='Set one up!')
		await ctx.send(embed=embed)
	else:
		embed = discord.Embed(title="📴AFK Status", color=0xFFA234)
		embed.add_field(name="Your AFK Status has been set to:", value=f"'{mssg}'")
		await ctx.send(embed=embed)

@client.command()
async def human(ctx, *, mssg=None, amount=1):
	if mssg == None:
		embed = discord.Embed(title="🙍‍♂️ Human Bot", color=0xC8FFED)
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
	embed = discord.Embed(title="All about Starry!!", color=0x7100FF)
	embed.add_field(name="I am Serenity's favored creation 😋",value="**Bot Name:** Starry\n**Creator:** Serenity#7879\n**Programming Language:** Python 3.8\n**Date Created:** June 7th, 2020 | 14:30:00 PM\n **Purpose:** it's a fun bot, so it doesn't use moderation, and is still in the making, but hopefully  𝑺𝒕𝒂𝒓𝒓𝒚 adds a passive, customized feel to any server that it is in!\nIt can do very basic stuff, but if you want more features, DM 'Serenity#7879', I'm always open to some nice feedback!")
	await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def changestatus(ctx, status):
  await client.change_presence(status=discord.Status.online,activity=discord.Activity(type=discord.ActivityType.playing, name=status))
  
@client.event
async def on_command_error(ctx, error):
  embed = discord.Embed(title="❗ Error ❗", color=0xA90000)
  embed.add_field(name="Uh oh...", value=f'{error}')
  message = await ctx.send(embed=embed)
  await message.add_reaction('❗')

@client.command()
async def greeting(ctx):
  gr1 = random.choice(piclinks.gr)
  embed = discord.Embed(title="Hello Starry! ✨", color=0xBD9EFF)
  embed.add_field(name="How are you today?", value=gr1)
  message = await ctx.send(embed=embed)
  await message.add_reaction('🥰')

@client.command()
async def time(ctx):
  embed = discord.Embed(title="⌚ Time in Coordinated Universal Time", color=0x575353)
  embed.add_field(name="Time (UTC):", value=today)
  message = await ctx.send(embed=embed)
  await message.add_reaction('⌚')

@client.command()
async def rate(ctx):
	ra1 = random.choice(piclinks.ra)
	await ctx.send(ra1)

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
	      'Whew, this is Serenity#7879 here, the creator of this bot. You just got saved from seeing a bunch of cringy jokes I stole from some "clean" websites 🤣🤣'
	]
	co1 = random.choice(co)
	embed = discord.Embed(title="🌽 Corny Jokes", color=0xC9FF92)
	embed.add_field(name="Ahhhh so corny!", value=co1)
	message = await ctx.send(embed=embed)

@client.command()
async def facts(ctx):
	fa = [
	    'Did you know that when ants die, they let off a unique stench only other ants can smell, and they will be attracted to the dead ant, and carry him away?',
	    'Did you know that Concorde, that supersonic plane, can burn as much fuel as the average car burns in a month, just by taxi\'ing towards the runway?'
	]

	fa1 = random.choice(fa)
	embed = discord.Embed(title="📔Random Facts", color=0xFFB694)
	embed.add_field(name="Here's a random fact 😋", value=fa1)
	message = await ctx.send(embed=embed)

@client.command()
async def invite(ctx):
	embed = discord.Embed(title="Invite 𝑺𝒕𝒂𝒓𝒓𝒚! 🥳",description="Heyyyy thank you sooo much, for requesting to invite me to your server 🥰! It will be a great pleasure of mine to bring that small sprinkle of comedy to your channel, and you won\'t regret this!😋\n𝑺𝒕𝒂𝒓𝒓𝒚 ⎰:sparkles:⎱ with administrator permissions: https://discord.com/api/oauth2/authorize?client_id=742030317451214888&permissions=8&scope=bot\n𝑺𝒕𝒂𝒓𝒓𝒚 ⎰:sparkles:⎱ with only text and general permissions (no administrator): https://discord.com/api/oauth2/authorize?client_id=742030317451214888&permissions=2084568823&scope=bot",color=0x8F40FF)
	embed.set_footer(text=f"Thank you {ctx.author}", icon_url=ctx.author.avatar_url)
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
async def role(ctx, *role: discord.Role):
	await ctx.author.add_roles(role)

@client.command()
@commands.has_permissions(administrator=True)
async def saymembers(ctx):
	for members in ctx.guild.members:
		await ctx.send(members)

@client.command()
async def join(ctx, *, mssg=None):
	if mssg == None:
		await ctx.send(f'{ctx.author.mention} re-run the command and also type in something that you would like to join characters to')
	else:
		await ctx.send(f'{mssg.join()}')

@client.command()
async def creator(ctx):
	embed = discord.Embed(title="🥳 𝑺𝒕𝒂𝒓𝒓𝒚's Creator", color=0xC592FF)
	embed.set_footer(text=f"{ctx.author} took interest", icon_url=ctx.author.avatar_url)
	embed.add_field(name="Keep in note that the creator changes names sometimes...",value="Currently Right Now: 'Serenity#7879'")
	embed.add_field(name="Previous name",value="'StarryAurora🌟#8018','Shaaaaddiii✨#8018','Shadi#7879'")
	await ctx.send(embed=embed)

@client.command()
async def serverinfo(ctx):
    roles = [role for role in ctx.guild.roles]
    channels = [channel for channel in ctx.guild.channels]
    embed = discord.Embed(title="Guild Info")
    embed.add_field(name='Server Name:',value=f'{ctx.guild.name}')
    embed.add_field(name='Server ID:',value=f'{ctx.guild.id}')
    embed.add_field(name='Server region:',value=f'{ctx.guild.region}')
    embed.add_field(name='Server Creation Date:',value=f'{ctx.guild.created_at}')
    embed.add_field(name='Server Owner:',value=f'{ctx.guild.owner}')
    embed.add_field(name='Member Count:',value=f'{ctx.guild.member_count}')
    embed.add_field(name='Amount of Channels:',value=f"{len(channels)}")
    embed.add_field(name='Amount of Roles:',value=f"{len(roles)}")
    await ctx.send(embed=embed)

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

@commands.cooldown(1, 3600, commands.BucketType.user)
@client.command()
@commands.has_permissions(administrator=True)
async def privid(ctx, member: discord.Member):
  user = ctx.author
  playinggame = user.activity
  roles = [role for role in member.roles]
  pfp = member.avatar_url
  embed = discord.Embed(title=f'This is {member.name}',colour=member.color,timestamp=ctx.message.created_at)
  embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
  embed.set_thumbnail(url=(pfp))
  embed.add_field(name="Account Creation Date:",value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
  embed.add_field(name="Join Date:",value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
  embed.add_field(name="Bot?", value=member.bot, inline=False)
  await ctx.send(embed=embed)

@client.command()
async def allinfo(ctx, member: discord.Member):
  user = ctx.author
  playinggame = user.activity
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
f2 = [0x97816e, 0x831300, 0x830000, 0x832600, 0xa88a88, 0x7e5c50, 0x7e5350]
@client.command()
async def frap(ctx):
	frap1 = random.choice(piclinks.homemadefrap)
	frap2 = random.choice(f2)
	embed = discord.Embed(title="Here is a homemade Frappuccino",description='Very emaculate',color=frap2)
	embed.set_image(url=frap1)
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
  embed = discord.Embed(title="🥳 𝑺𝒕𝒂𝒓𝒓𝒚 ⎰✨⎱ is here to have fun! 🥳",description="Choose an option below! This is a bot to have fun with, so... have fun!! 😁🤣",color=0x8F40FF)
  embed.set_footer(text=f"Welcome to Starry's interface, {ctx.author}!",icon_url=ctx.author.avatar_url)
  embed.set_image(url='https://media1.tenor.com/images/24b4cf8512e58420d0cdfea3df5a3cce/tenor.gif?itemid=14432583')
  embed.add_field(name="💬 Text Commands!", value="star+text")
  embed.add_field(name="🎈 Activities!", value="star+activity")
  embed.add_field(name="🤗 Socialize!", value="star+social")
  embed.add_field(name="🥳 Giveaway Commands!", value="star+giveaways")
  embed.add_field(name="📸 Media Sorts!", value="star+media")
  embed.add_field(name="🔧 Starry Utility!", value="star+utility")
  embed.add_field(name="🔨 Starry Moderation!", value="star+mod")
  embed.add_field(name="📙 About and Credits!", value="star+abocred")
  embed.add_field(name="The Cogs!",value="star+cogs")
  message = await ctx.send(embed=embed)
  await message.add_reaction('<:HyperDance:739831597083263048>')
  await message.add_reaction('<:kawaiibunny:738782552122196148>')

@client.command()
async def giveaways(ctx):
  embed = discord.Embed(title = "Starry is very happy to do Giveaways!!",color=0x000000)
  embed.add_field(name="Giveaway Syntax", value="```star+<giveaway_command> <winner_ammount> <item>```\nThese giveaways are preset times to choose from below, and you do not need to put a \"w\" in front of the amount of winners.")
  embed.add_field(name="5 Second Drop",value="star+fivesecgive")
  embed.add_field(name="5 Minute Giveaway",value="star+fivemingive")
  embed.add_field(name="10 Minute Giveaway",value="star+tenmingive")
  embed.add_field(name="30 Minute Giveaway",value="star+thirtymingive")
  embed.add_field(name="1 Hour Giveaway",value="star+onehrgive")
  embed.add_field(name="2 Hour Giveaway",value="star+twohrgive")
  embed.add_field(name="3 Hour Giveaway",value="star+threehrgive")
  embed.add_field(name="6 Hour Giveaway",value="star+sixhrgive")
  embed.add_field(name="12 Hour Giveaway",value="star+twelvehrgive")
  embed.add_field(name="1 Day Giveaway",value="star+onedaygive")
  embed.add_field(name="2 Day Giveaway",value="star+twodaygive")
  embed.add_field(name="3 Day Giveaway",value="star+threedaygive")
  embed.add_field(name="1 Week Giveaway",value="star+oneweekgive")
  message = await ctx.send(embed = embed)
  await message.add_reaction('🎉')
  await message.add_reaction('🥳')

@client.command()
async def cogs(ctx):
  embed = discord.Embed(title="Starry has cogs!",color=0xFFCCCA)
  embed.set_footer(text=f"Try the cogs out, {ctx.author}!",icon_url=ctx.author.avatar_url)
  embed.set_image(url='https://media1.tenor.com/images/24b4cf8512e58420d0cdfea3df5a3cce/tenor.gif?itemid=14432583')
  embed.add_field(name="Here are the cogs!", value="I decided to devote this section here to commands that rely upon Cogs to work!",inline = False)
  embed.add_field(name="❔ Wanna play some trivia?", value="star+randomtrivia")
  embed.add_field(name="🔎 Do a Google Search!", value="star+google")
  embed.add_field(name="📩 Post a tweet on Twitter!", value="star+twitter")
  embed.add_field(name="Get Some Memes!", value="star+meme")
  embed.add_field(name="Wanna see a cat?", value="star+cat")
  embed.add_field(name="Wanna see a dog?", value="star+dog")
  embed.add_field(name="🐦Wanna see a bird?", value="star+bird")
  await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def mod(ctx):
  embed = discord.Embed(title="𝑺𝒕𝒂𝒓𝒓𝒚 is here to MODERATE!", description="Experimental Module",color=0xcba1ff)
  embed.set_footer(text='Starry | Serenity#7879')
  embed.set_image(url='https://media1.tenor.com/images/24b4cf8512e58420d0cdfea3df5a3cce/tenor.gif?itemid=14432583'	)
  embed.add_field(name="🔨 Starry Moderation!",value="So far, very few commands that require admin privelages", inline=False)
  embed.add_field(name="🦶 Kick a Member", value="star+kick")
  embed.add_field(name="❌ Ban a Member", value="star+ban")
  embed.add_field(name="Channel Mute a Member",value="star+chanmute")
  embed.add_field(name="Unmute a Member from the Channel",value="star+unchanmute")
  embed.add_field(name="🔒 Personal User Info", value="star+privid")
  embed.add_field(name="🎈 Add a Role!", value="star+role")
  await ctx.send(embed=embed)

@client.command()
async def textmod(ctx):
	embed = discord.Embed(title="Text Modification Time!! 🥳",color=0x6A9EFF)
	embed.set_footer(text='Starry | Serenity#7879')
	embed.set_image(url='https://media1.tenor.com/images/24b4cf8512e58420d0cdfea3df5a3cce/tenor.gif?itemid=14432583')
	embed.add_field(name="Text Modifying!", value="Make Starry reverse, capitalize, lowercase, and do simple modifications to your text!",inline=False)
	embed.add_field(name='Swapcasing',value='star+swapcase')
	embed.add_field(name='Lowercasing', value='star+lowercase')
	embed.add_field(name="Uppercasing", value="star+uppercase")
	await ctx.send(embed=embed)

@client.command()
async def text(ctx):
	embed = discord.Embed(title="Welcome to the Text command module! 🥳",description="Text can be modified per the commands below!",color=0x6A9EFF)
	embed.set_footer(text='Starry | Serenity#7879')
	embed.set_image(url='https://media1.tenor.com/images/24b4cf8512e58420d0cdfea3df5a3cce/tenor.gif?itemid=14432583')
	embed.add_field(name="💬 Text Commands!", value="Here, you can make Starry say stuff, reverse stuff, humanize stuff, idk lol",inline=False)
	embed.add_field(name='Text Modifiers', value='star+textmod')
	embed.add_field(name="🙍‍♂️ Human", value="star+human")
	embed.add_field(name="🦜Parrot!", value="star+parrot")
	embed.add_field(name="🔄Reverse Speak", value="star+reverse")
	await ctx.send(embed=embed)

@client.command()
async def activity(ctx):
  embed = discord.Embed(title="Perform a simple activity! 🥳", description="Such as random generators, SUSHI.", color=0xFF756A)
  embed.set_footer(text='Starry | Serenity#7879')
  embed.set_image(url='https://media1.tenor.com/images/24b4cf8512e58420d0cdfea3df5a3cce/tenor.gif?itemid=14432583'
	)
  embed.add_field(name="🎈 Activities!", value="Simple activities!", inline=False)
  embed.add_field(name="💵Flip a Dollar", value="star+flip")
  embed.add_field(name="📝Test Grade", value="star+grade")
  embed.add_field(name="Make a Tweet!", value="star+tweet")
  embed.add_field(name="🍣Get Sushi", value="star+sushi")
  await ctx.send(embed=embed)

@client.command()
async def social(ctx):
	embed = discord.Embed(title="Socialize with Starry! 🥳",description="Tell a joke or greeting!",color=0x6AFFC5)
	embed.set_footer(text='Starry | Serenity#7879')
	embed.set_image(url='https://media1.tenor.com/images/24b4cf8512e58420d0cdfea3df5a3cce/tenor.gif?itemid=14432583')
	embed.add_field(name="🤗 Socialize!", value="Random test generation!", inline=False)
	embed.add_field(name="👋Hey Starry! How are you?", value="star+greeting")
	embed.add_field(name="🌽Corny Jokes", value="star+corny")
	embed.add_field(name="📔Random Facts", value="star+facts")
	embed.add_field(name="📈Rate Stuff", value="star+rate")
	await ctx.send(embed=embed)

@client.command()
async def media(ctx):
	embed = discord.Embed(title="Here is some Medias! 🥳",description="The Kawaii command, I give credit to the OwO bot!",color=0xFFFB6A)
	embed.set_footer(text='𝑺𝒕𝒂𝒓𝒓𝒚 | Serenity#7879')
	embed.set_image(url='https://media1.tenor.com/images/24b4cf8512e58420d0cdfea3df5a3cce/tenor.gif?itemid=14432583')
	embed.add_field(name="📸 Media Sorts!",value="You can do Kawaii! (inspired by the OwO bot!)\nOr you can see pictures and shots of a turtles I took myself!",inline=False)
	embed.add_field(name='🥰Kawaii!', value='star+kawaii')
	embed.add_field(name='🐢Turtle!', value='star+turtle')
	embed.add_field(name='☕Frappuccino!', value='star+frap')
	embed.add_field(name='🤣Memes! (under heavy work)', value='star+memes')
	embed.add_field(name='🌈Aesthetic!', value='star+aesthetic')
	await ctx.send(embed=embed)

@client.command()
async def utility(ctx):
	embed = discord.Embed( title="Some simple utility tools! 🥳",description="Very simple commands, not moderation",color=0x949494)
	embed.set_footer(text='Starry! | Serenity#7879')
	embed.set_image(url='https://media1.tenor.com/images/24b4cf8512e58420d0cdfea3df5a3cce/tenor.gif?itemid=14432583')
	embed.add_field(name="🔧 Starry Utility!", value="Simple tools", inline=False)
	embed.add_field(name='📤Mail Someone!', value='star+mail')
	embed.add_field(name='📁Identify a Member', value='star+identity')
	embed.add_field(name="📴AFK Status", value="star+afk")
	embed.add_field(name="🗺️Where am I?", value="star+where")
	embed.add_field(name="⌚Current Time (UTC)", value="star+time")
	embed.add_field(name="⏰SimplTime", value="star+simpltime")
	embed.add_field(name="📚About Me!", value="star+about")
	embed.add_field(name="📩Invite Me!", value="star+invite")
	embed.add_field(name="🏭 Server Population", value="star+serverpop")
	embed.add_field(name="📡Check Ping Latency", value="star+ping")
	embed.add_field(name="✨Bot Creators Current Tag", value="star+creator")
	embed.add_field(name="🎈About the Creator", value="star+createabout")
	await ctx.send(embed=embed)

@client.command()
async def abocred(ctx):
	embed = discord.Embed(title="Check my about, credits, updates, and invite me! 🥳",color=0xFF9974)
	embed.set_footer(text='Starry! | Serenity#7879')
	embed.set_image(url='https://media1.tenor.com/images/24b4cf8512e58420d0cdfea3df5a3cce/tenor.gif?itemid=14432583')
	embed.add_field(name="📙 About and Credits!",value="About, Credits, Invites, Update log",inline=False)
	embed.add_field(name="🔖Client ID (if you want to add me with customized permissions)", value='719944711972061274', inline=False)
	embed.add_field(name="📚About Me!", value="star+about")
	embed.add_field(name="📩Invite Me!", value="star+invite")
	embed.add_field(name="✨Bot Creators Current Tag", value="star+creator")
	embed.add_field(name="🎈About the Creator", value="star+createabout")
	await ctx.send(embed=embed)

#-----------------------------------------------


B.b()
client.run(os.getenv('TOKEN'))
