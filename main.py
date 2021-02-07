# main.py
import os
import discord
import onMessageHelper
import sys
import traceback
from dotenv import load_dotenv
from discord.ext import commands

# import token from env file
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# import our cogs
cogsList = ['cog.standardCog', 'cog.musicBotCog']


bot = commands.Bot(command_prefix='!', case_insensitive=True, help_command=None)

# load our cogs listed above in [cogsList].
if __name__ == '__main__':
    for extension in cogsList:
        bot.load_extension(extension)

# connect the bot to discord
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name='type "!help"', url='https://www.twitch.tv/MattyReign'))
    print(f'{bot.user.name} has connected to Discord!')

# function for standard commands
@bot.event
async def on_message(message):
    await onMessageHelper.userMessage(message, bot)
    await bot.process_commands(message)



# run the bot
bot.run(token)
