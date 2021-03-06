import discord
from discord.ext import commands


class   Main(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} (ms)')
    
    @commands.command()
    async def clean(self,ctx,num:int):
        await ctx.message.delete()
        await ctx.channel.purge(limit=num)

def setup(bot):
    bot.add_cog(Main(bot))