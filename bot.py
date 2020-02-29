import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    print(f'{member} join!')
    channel = bot.get_channel(683270358026944512)
    await channel.send(f'{member}join!')

@bot.event
async def on_member_remove(member):
    print(f'{member} leave!')

    channel = bot.get_channel(683270402616590367)
    await channel.send(f'{member}leave')


bot.run('NjgzMjU3MTI0NTAzMjg5ODY2.XlpBeQ.6KVh5iEg7RKuxB9bYisJlQASvb0')