# remindCog.py
import sqlite3
import os
import discord
from asyncio import sleep as s
from dotenv import load_dotenv
from discord.ext import commands

bot = commands.Bot(command_prefix='!',
                   case_insensitive=True, help_command=None)

# connect to our database
remindDB = sqlite3.connect('database/remindDB.db')

# a short variable for the cursor method
c = remindDB.cursor()

# *** THE CODE BELOW WAS ONLY EXECUTED ONCE TO CREATE THE TABLE ***
#c.execute("""Create TABLE reminders (
#            user text,
#            time integer,
#            timeType text,
#            message text
#            )""")

class remindMe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='RemindMe')
    async def remindMeFunction(self, ctx, time: int, timeType: str, *, message):

        remindResponce = ctx.send(f'{ctx.author.mention}: {message}')
        remindConfirm = ctx.send(
            f'{ctx.author.mention} I will remind you in {time} {timeType}: {message}')

        if timeType.lower() == 'second' or timeType.lower() == 'seconds':
            await remindConfirm
            await s(time)
            await remindResponce

        elif timeType.lower() == 'minute' or timeType.lower() == 'minutes':
            await remindConfirm
            await s(60*time)
            await remindResponce

        elif timeType.lower() == 'hour' or timeType.lower() == 'hours':
            await remindConfirm
            await s(3600*time)
            await remindResponce

        elif timeType.lower() == 'day' or timeType.lower() == 'days':
            await remindConfirm
            await s(86400*time)
            await remindResponce

        else:
            await ctx.send(f'{ctx.author.mention}, Your reminder was NOT formated correctly.')

        

def setup(bot):
    bot.add_cog(remindMe(bot))
