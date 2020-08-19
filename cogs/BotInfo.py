from time import monotonic
import datetime

import discord
from discord.ext import commands



class BotInfo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    async def botinfo(self, ctx, *, bot: discord.User):
        if not bot.bot:
            return await ctx.send("That's no bot")

        async with ctx.channel.typing():

            db_bot = await self.bot.db.bots.find_one({"_id": str(bot.id)})

            if not db_bot:
                raise NoSomething(bot)

            bot_owner = await self.bot.db.users.find_one({"_id": db_bot["owner"]["id"]})

            embed = discord.Embed(colour=await self.embed_colour(ctx))

            embed.add_field(name=f"{self.bot.settings['emoji']['shadows']} Bot Name", value=db_bot["name"])
            embed.add_field(name=f"{self.bot.settings['emoji']['id']} ID", value=db_bot["_id"])
            embed.add_field(name=f"{self.bot.settings['emoji']['crown']} Developer",
                            value=f"[{bot_owner['fullUsername']}]({self.bot.settings['website']['url']}/users/{bot_owner['_id']})")
            embed.add_field(name=f"{self.bot.settings['emoji']['infoBook']} Library", value=db_bot["library"])
            embed.add_field(name=f"{self.bot.settings['emoji']['speech']} Prefix", value=db_bot["prefix"])
            embed.add_field(name=f"{self.bot.settings['emoji']['shield']} Server Count",
                            value=db_bot["serverCount"])
            embed.add_field(name=f"{self.bot.settings['emoji']['url']} Listing URL",
                            value=f"{self.bot.settings['website']['url']}/bots/{db_bot['_id']}", inline=False)
            embed.set_thumbnail(url=f"{db_bot['avatar']['url']}")

            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(BotInfo(client))