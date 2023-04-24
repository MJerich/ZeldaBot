# openaiCog.py
from discord.ext import commands
from helpers import requestHelper


class openaiCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # coin flip
    @commands.command(name='ai')
    async def coinFlip(self, ctx, *, message: str):
        msg = await ctx.send("getting your response...")
        aiResponse = requestHelper.aiChat(chatMessage=message)
        await msg.edit(content=aiResponse)


async def setup(bot):
    await bot.add_cog(openaiCommands(bot))
