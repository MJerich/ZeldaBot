# remindCog.py
from asyncio import sleep as s
from discord.ext import commands


class remindMe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='RemindMe')
    async def remindMeFunction(self, ctx, time: int, timeType: str, *, message):

        remindResponse = ctx.send(f'{ctx.author.mention}: {message}')
        remindConfirm = ctx.send(
            f'{ctx.author.mention} I will remind you in {time} {timeType}: {message}')

        if timeType.lower() == 'second' or timeType.lower() == 'seconds':
            await remindConfirm
            await s(time)
            await remindResponse

        elif timeType.lower() == 'minute' or timeType.lower() == 'minutes':
            await remindConfirm
            await s(60*time)
            await remindResponse

        elif timeType.lower() == 'hour' or timeType.lower() == 'hours':
            await remindConfirm
            await s(3600*time)
            await remindResponse

        elif timeType.lower() == 'day' or timeType.lower() == 'days':
            await remindConfirm
            await s(86400*time)
            await remindResponse

        else:
            await ctx.send(f'{ctx.author.mention}, Your reminder was NOT formatted correctly.')


async def setup(bot):
    await bot.add_cog(remindMe(bot))
