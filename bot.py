import discord
from discord.ext import commands
import json
import random

with open('setting.json','r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

bot = commands.Bot(command_prefix='-')

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    print(f'{member} join!')
    channel = bot.get_channel(int(jdata["Welcom_channel"]))
    await channel.send(f'{member}join!')

@bot.event
async def on_member_remove(member):
    print(f'{member} leave!')

    channel = bot.get_channel(int(jdata["Leave_channel"]))
    await channel.send(f'{member}leave')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}毫秒')

@bot.command()
async def 大肥蛙(ctx):
    random_pic=random.choice(jdata['大肥蛙'])
    大肥蛙 = discord.File(random_pic)
    await ctx.send(file=大肥蛙)

@bot.command()
async def 大鼻子(ctx):
    random_pic=random.choice(jdata['大鼻子'])
    大鼻子 = discord.File(random_pic)
    await ctx.send(file=大鼻子)

@bot.command()
async def 阿蛙(ctx):
    random_pic=random.choice(jdata['阿蛙'])
    阿蛙 = discord.File(random_pic)
    await ctx.send(file=阿蛙)

@bot.command()
async def 黑熊(ctx):
    random_pic=random.choice(jdata['黑熊'])
    黑熊 = discord.File(random_pic)
    await ctx.send(file=黑熊)

bot.run(jdata["Token"])