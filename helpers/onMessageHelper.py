# onMessage.py
import discord
from discord.ext import commands


async def userMessage(message, bot):
    # won't reply to self
    if message.author == bot.user:
        return

    # cloud to butt translator
    if 'cloud' in message.content.lower():
        if message.author != 'l0xzer#0':
            await message.channel.send('Did you mean butt(s)?')
