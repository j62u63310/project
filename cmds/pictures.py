import discord
from discord.ext import commands
import json
import random

with open('setting.json','r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class Pictures(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def 大肥蛙(self, ctx):
        random_pic=random.choice(jdata['大肥蛙'])
        大肥蛙 = discord.File(random_pic)
        await ctx.send(file=大肥蛙)

    @commands.command()
    async def 大鼻子(self, ctx):
        random_pic=random.choice(jdata['大鼻子'])
        大鼻子 = discord.File(random_pic)
        await ctx.send(file=大鼻子)

    @commands.command()
    async def 阿蛙(self, ctx):
        random_pic=random.choice(jdata['阿蛙'])
        阿蛙 = discord.File(random_pic)
        await ctx.send(file=阿蛙)

    @commands.command()
    async def 黑熊(self, ctx):
        random_pic=random.choice(jdata['黑熊'])
        黑熊 = discord.File(random_pic)
        await ctx.send(file=黑熊)

def setup(bot):
    bot.add_cog(Pictures(bot))