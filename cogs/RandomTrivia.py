import discord
from discord.ext import commands
import random
import json
import aiohttp
import asyncio

class RandomTrivia(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def trivia(self, ctx):
    session = aiohttp.ClientSession()
    response = await session.get("https://opentdb.com/api.php?amount=10")
    data = await response.json()
    await session.close()

    question = random.choice(data['results'])
    incorrect_answers = question['incorrect_answers']
    correct_answer = question['correct_answer']
   
    letters = ["A", "B", "C", "D"]
    correct_letter = random.choice(letters)
    letters.remove(correct_letter)

    value_str = ""
   
    if correct_letter == "A":
      value_str += f"A. {correct_answer}\nB. {incorrect_answers[0]}\nC. {incorrect_answers[1]}\nD. {incorrect_answers[2]}"
    
    elif correct_letter == "B":
      value_str += f"A. {incorrect_answers[0]}\nB. {correct_answer}\nC. {incorrect_answers[1]}\nD. {incorrect_answers[2]}"
    
    elif correct_letter == "C":
      value_str += f"A. {incorrect_answers[0]}\nB. {incorrect_answers[1]}\nC. {correct_answer}\nD. {incorrect_answers[2]}"
    
    elif correct_letter == "D":
      value_str += f"A. {incorrect_answers[0]}\nB. {incorrect_answers[1]}\nC. {incorrect_answers[2]}\nD. {correct_answer}"
   
    embed=discord.Embed(color=0xFF69B4)
    embed.add_field(name=question['question'], value=value_str)
    message = await ctx.send(embed=embed)
    await message.add_reaction('🇦')
    await message.add_reaction('🇧')
    await message.add_reaction('🇨')
    await message.add_reaction('🇩')
  
    emote = ['🇦', '🇧', '🇨', '🇩']
  
    def check(reaction, user):
      return (reaction.message.id == message.id) and (user.id == ctx.author.id) and (str(reaction) in emote)

    try:
      reaction, user = await self.client.wait_for('reaction_add', check=check, timeout=60)
  
    except asyncio.TimeoutError:
      return await ctx.send("Timed out")

    if str(reaction) == "🇦":
      if correct_letter == "A":
        embed = discord.Embed(description="Correct!", color=discord.Color.green())
        await message.edit(embed=embed)
      
      else:
        embed = discord.Embed(description=f"Wrong! It was {correct_letter}. {correct_answer}", color=discord.Color.red())
        await message.edit(embed=embed)
        
    elif str(reaction) == "🇧":
      if correct_letter == "B":
        embed = discord.Embed(description="Correct!", color=discord.Color.green())
        await message.edit(embed=embed)
      else:
        embed = discord.Embed(description=f"Wrong! It was {correct_letter}. {correct_answer}", color=discord.Color.red())
        await message.edit(embed=embed)
        
    elif str(reaction) == "🇨":
      if correct_letter == "C":
        embed = discord.Embed(description="Correct!", color=discord.Color.green())
        await message.edit(embed=embed)
      else:
        embed = discord.Embed(description=f"Wrong! It was {correct_letter}. {correct_answer}", color=discord.Color.red())
        await message.edit(embed=embed)
        
    elif str(reaction) == "🇩":
      if correct_letter == "D":
        embed = discord.Embed(description="Correct!", color=discord.Color.green())
        await message.edit(embed=embed)
      else:
        embed = discord.Embed(description=f"Wrong! It was {correct_letter}. {correct_answer}", color=discord.Color.red())
        await message.edit(embed=embed) 
  
def setup(client):
    client.add_cog(RandomTrivia(client))