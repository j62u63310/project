import discord
from discord.ext import commands
import json
import random

with open('setting.json','r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class message(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        keyword=['你好麻','太帥了','真可怕','你好爛','好可怕','受不了','簡直喪心病狂']
        if  msg.content in keyword and msg.author !=self.bot.user:
            await msg.channel.send('真的ㄟ')
        if  msg.content == '真的ㄟ' and msg.author  !=self.bot.user:
            random_word = random.choice(['你好麻','太帥了','真可怕','你好爛','好可怕','受不了','簡直喪心病狂'])
            await msg.channel.send(random_word)
        if  msg.content == '大肥蛙' and msg.author  !=self.bot.user:
            await msg.channel.send('你好爛 :smile:')
        if  msg.content == '大鼻子' and msg.author  !=self.bot.user:
            await msg.channel.send('何等反社會人格的思想 :smile:')
        if  msg.content.endswith('老婆')    and msg.author  !=self.bot.user:
            await msg.channel.send('並沒有 不要瞎掰好嗎')

def setup(bot):
    bot.add_cog(message(bot))