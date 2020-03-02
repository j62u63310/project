import discord
from discord.ext import commands
import json
import random
import os

with open('setting.json','r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

bot = commands.Bot(command_prefix='-')

@bot.command()
async def load(ctx,extension):
    bot.load_extension(F'cmds.{extension}')
    await ctx.send(F'讀取 {extension} 完成')

@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(F'cmds.{extension}')
    await ctx.send(F'卸下 {extension} 完成')

@bot.command()
async def reload(ctx,extension):
    bot.reload_extension(F'cmds.{extension}')
    await ctx.send(F'重新讀取 {extension} 完成')

@bot.event
async def on_ready():
    print(">>Bot is online<<")

for filename in os.listdir('./cmds'):
    if filename.endswith('py'):
        bot.load_extension(F'cmds.{filename[:-3]}')

if __name__ =="__main__":
    bot.run(jdata["Token"])