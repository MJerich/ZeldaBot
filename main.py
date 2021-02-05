# main.py
import os
import discord
import youtube_dl
import onMessageHelper
import sys
import traceback
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
myGuild = os.getenv('DISCORD_GUILD')

# Below cogs represents our folder our cogs are in. Following is the file name. So 'meme.py' in cogs, would be cogs.meme
# Think of it like a dot path import
initial_extensions = ['cog.musicBotHelper']

bot = commands.Bot(command_prefix='*', case_insensitive=True)

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

# connect the bot to discord
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# function for standard commands
@bot.event
async def on_message(message):
    await onMessageHelper.userMessage(message, bot)
    await bot.process_commands(message)



#client.run(token)
bot.run(token)
