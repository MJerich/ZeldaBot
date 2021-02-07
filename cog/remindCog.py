# remindCog.py
import os
import discord
from asyncio import sleep as s
from dotenv import load_dotenv
from discord.ext import commands

bot = commands.Bot(command_prefix='!',
                   case_insensitive=True, help_command=None)

class remindMe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='RemindMe')
    async def remindMeFunction(self, ctx, time: int, timeType: str, *, message):

        remindResponce = ctx.send(f'{ctx.author.mention}: {message}')

        if timeType.lower() == 's':
            await ctx.send(f'{ctx.author.mention} I will remind you in {time} second(s): {message}')
            await s(time)
            await remindResponce

        elif timeType.lower() == 'm':
            await ctx.send(f'{ctx.author.mention} I will remind you in {time} minute(s): {message}')
            await s(60*time)
            await remindResponce

        elif timeType.lower() == 'h':
            await ctx.send(f'{ctx.author.mention} I will remind you in {time} hour(s): {message}')
            await s(3600*time)
            await remindResponce

        elif timeType.lower() == 'd':
            await ctx.send(f'{ctx.author.mention} I remind you in {time} day(s): {message}')
            await s(86400*time)
            await remindResponce

def setup(bot):
    bot.add_cog(remindMe(bot))
