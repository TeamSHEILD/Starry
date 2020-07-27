@client.command()
async def swapcase(ctx,*, mssg=None, amount = 1):
  if mssg == None:
    await ctx.channel.purge(limit = amount)
    await ctx.send(f'{ctx.author.mention} re-run the command and also type in something that you would like to swapcase')
  else:
    await ctx.channel.purge(limit = amount)
    await ctx.send(f'{mssg.swapcase()}')

@client.command()
async def lower(ctx,*, mssg=None, amount = 1):
  if mssg == None:
    await ctx.channel.purge(limit = amount)
    await ctx.send(f'{ctx.author.mention} re-run the command and also type in something that you would like to all lowercase')
  else:
    await ctx.channel.purge(limit = amount)
    await ctx.send(f'{mssg.lower()}')

@client.command()
async def upper(ctx,*, mssg=None, amount = 1):
  if mssg == None:
    await ctx.channel.purge(limit = amount)
    await ctx.send(f'{ctx.author.mention} re-run the command and also type in something that you would like to uppercase')
  else:
    await ctx.channel.purge(limit = amount)
    await ctx.send(f'{mssg.upper()}')

@client.command()
async def join(ctx,*, mssg=None, amount = 1):
  if mssg == None:
    await ctx.channel.purge(limit = amount)
    await ctx.send(f'{ctx.author.mention} re-run the command and also type in something that you would like to join characters to')
  else:
    await ctx.channel.purge(limit = amount)
    await ctx.send(f'{mssg.join('oH Ho')}')