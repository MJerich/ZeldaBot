# musicBotHelper.py
import youtube_dl
import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='*', case_insensitive=True)
# function to check if the bot is already connected to the voice channel
def is_connected(ctx):
    voice_client = discord.utils.get(ctx.bot.voice_clients)
    return voice_client and voice_client.is_connected()

class musicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # play command, must be followed with a youtube url
    @bot.command(name='play', hidden=True)
    async def play(self, ctx, url: str):
        songPlaying = os.path.isfile('song.mp3')
        try:
            if songPlaying:
                os.remove('song.mp3')
        except PermissionError:
            await ctx.send('wait for the current song to finish please.')
            return

        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='Reign\'s music studio')

        if not is_connected(ctx):
            await voiceChannel.connect()

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir('./'):
            if file.endswith('.mp3'):
                os.rename(file, 'song.mp3')

        ctx.voice_client.play(discord.FFmpegPCMAudio('song.mp3'))

    # make bot leabve the voice channel
    @bot.command(name='leave', hidden=True)
    async def leave(self, ctx):
        if ctx.voice_client.is_connected():
            await ctx.voice_client.disconnect()
        else:
            await ctx.send('The bot is not in a voice channel.')

    # pause the music
    @bot.command(name='pause', hidden=True)
    async def pause(self, ctx):
        if ctx.voice_client.is_playing():
            ctx.voice_client.pause()
        else:
            await ctx.send('Nothing is playing.')

    #resume the music after pausing
    @bot.command(name='resume', hidden=True)
    async def resume(self, ctx):
        if ctx.voice_client.is_paused():
            ctx.voice_client.resume()
        else:
            await ctx.send('Audio is already playing.')

    # stop the music
    @bot.command(name='stop', hidden=True)
    async def stop(self, ctx):
        if ctx.voice_client.is_playing():
            ctx.voice_client.stop()
        else:
            await ctx.send('Nothing is playing.')


def setup(bot):
    bot.add_cog(musicCommands(bot))
