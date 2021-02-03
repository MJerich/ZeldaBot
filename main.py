# bot.py
import os
import discord
import youtube_dl
import onMessageHelper
import musicBotHelper
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
myGuild = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='*', case_insensitive=True)

# connect the bot to discord
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# function for standard commands
@bot.event
async def on_message(message):
    await onMessageHelper.userMessage(message, bot)

@bot.command
async def musicBot(ctx, url: str):
    await musicBotHelper.play(ctx, url, bot)
    await musicBotHelper.leave(ctx, bot)
    await musicBotHelper.pause(ctx, bot)
    await musicBotHelper.resume(ctx, bot)
    await musicBotHelper.stop(ctx, bot)

#client.run(token)
bot.run(token)
