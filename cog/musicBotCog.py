# musicBotHelper.py
import youtube_dl
import os
import discord
from discord.ext import commands

# function to check if the bot is already connected to the voice channel
def is_connected(ctx):
    voice_client = discord.utils.get(ctx.bot.voice_clients)
    return voice_client and voice_client.is_connected()

# variables for 'Bot-Command-Channel' and wrong channel responce
botCC = 801828129068023809
wrngChannel = f'Please use music bot commands in <#{botCC}>'

class musicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # play command, must be followed with a youtube url
    @commands.command(name='play')
    async def play(self, ctx, url: str):
        if ctx.message.channel.id == botCC:
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

                await ctx.send(f'Downloading...')

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
        else:
            #command attempted in non command channel - redirect user
            await ctx.message.channel.send(wrngChannel)

    # make bot leabve the voice channel
    @commands.command(name='leave')
    async def leave(self, ctx):
        if ctx.message.channel.id == botCC:
            if ctx.voice_client.is_connected():
                await ctx.voice_client.disconnect()
            else:
                await ctx.send('The bot is not in a voice channel.')
        else:
            #command attempted in non command channel - redirect user
            await ctx.message.channel.send(wrngChannel)

    # pause the music
    @commands.command(name='pause')
    async def pause(self, ctx):
        if ctx.message.channel.id == botCC:
            if ctx.voice_client.is_playing():
                ctx.voice_client.pause()
            else:
                await ctx.send('Nothing is playing.')
        else:
            #command attempted in non command channel - redirect user
            await ctx.message.channel.send(wrngChannel)

    #resume the music after pausing
    @commands.command(name='resume')
    async def resume(self, ctx):
        if ctx.message.channel.id == botCC:
            if ctx.voice_client.is_paused():
                ctx.voice_client.resume()
            else:
                await ctx.send('Audio is already playing.')
        else:
            #command attempted in non command channel - redirect user
            await ctx.message.channel.send(wrngChannel)

    # stop the music
    @commands.command(name='stop')
    async def stop(self, ctx):
        if ctx.message.channel.id == botCC:
            if ctx.voice_client.is_playing():
                ctx.voice_client.stop()
            else:
                await ctx.send('Nothing is playing.')
        else:
            #command attempted in non command channel - redirect user
            await ctx.message.channel.send(wrngChannel)



def setup(bot):
    bot.add_cog(musicCommands(bot))
