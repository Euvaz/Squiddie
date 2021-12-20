"""Class file for music."""

import discord
from discord.ext import commands
from youtube_dl import YoutubeDL


class Music(commands.Cog):
    """Music class."""
    def __init__(self, client):
        """Initialize"""
        self.client = client
    
        # Initialize state
        self.is_playing = False

        # Initialize music queue [song, channel]
        self.music_queue = []

        # Initialize YDL and FFMPEG parameters
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

        self.vc = ""

    # Search for item on YouTube
    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try: 
                info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
            except Exception: 
                return False

        return {'source': info['formats'][0]['url'], 'title': info['title']}

    def play_next(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            # Get first URL of list
            m_url = self.music_queue[0][0]['source']

            # Remove song from list when played
            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    # Prevent infinite loop
    async def play_music(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            m_url = self.music_queue[0][0]['source']
            
            # Connect to voice channel if not connected
            if self.vc == "" or not self.vc.is_connected() or self.vc == None:
                self.vc = await self.music_queue[0][1].connect()
            else:
                await self.vc.move_to(self.music_queue[0][1])
            
            # Remove song from list when played
            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    # Play command
    @commands.command(name="play")
    async def play(self, ctx, *args):
        """Play a selected song from YouTube."""
        query = " ".join(args)
        
        voice_channel = ctx.author.voice.channel

        if voice_channel is None:
            # Connect to voice channel of message author
            await ctx.send("Connect to a voice channel!")
        else:
            song = self.search_yt(query)
            if type(song) == type(True):
                await ctx.send("Could not download the song. Incorrect format try another keyword. This could be due to playlist or a livestream format.")
            else:
                await ctx.send("Song added to the queue")
                self.music_queue.append([song, voice_channel])
                
                if self.is_playing == False:
                    await self.play_music()

    # Queue command
    @commands.command(name="queue")
    async def queue(self, ctx):
        """Display the current songs in queue."""
        retval = ""
        for i in range(0, len(self.music_queue)):
            retval += self.music_queue[i][0]['title'] + "\n"

        #print(retval)
        if retval != "":
            await ctx.send(retval)
        else:
            await ctx.send("No music in queue")

    # Skip command
    @commands.command(name="skip")
    async def skip(self, ctx):
        """Skip current song being played."""
        if self.vc != "" and self.vc:
            self.vc.stop()
            await self.play_music()

    # Disconnect command
    @commands.command(name="disconnect")
    async def disconnect(self, ctx):
        """Disconnect bot from current voice channel."""
        await self.vc.disconnect()


def setup(client):
    """Load cog."""
    client.add_cog(Music(client))
