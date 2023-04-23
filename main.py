# main.py
import asyncio
import os
import discord
import onMessageHelper
from dotenv import load_dotenv
from discord.ext import commands

# import token from env file
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# set variables
cogsList = ['cog.standardCog', 'cog.remindCog']
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

zeldaBot = commands.Bot(command_prefix='!', case_insensitive=True, help_command=None, intents=intents)


# setup cogs
# class zeldaBot(commands.Bot(command_prefix='!', case_insensitive=True, help_command=None, intents=intents)):
#     async def setup_hook(self):
#         await self.load_extension(name='cog.standardCog')
#         print('Successfully loaded cogs')

async def start():
    async with zeldaBot:
        for extension in cogsList:
            await zeldaBot.load_extension(extension)
        await zeldaBot.start(token)


# setup when the bot starts
@zeldaBot.event
async def on_ready():
    await zeldaBot.change_presence(activity=discord.Streaming(name='type "!help"', url='https://www.twitch.tv'
                                                                                       '/MattyReign'))
    print(f'{zeldaBot.user.name} has connected to Discord!')


# function to load adn watch for non-standard commands
@zeldaBot.event
async def on_message(message):
    await onMessageHelper.userMessage(message, zeldaBot)
    await zeldaBot.process_commands(message)


# run the bot
asyncio.run(start())
