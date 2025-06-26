import discord
from discord.ext import commands
import os
import random
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f" Logged in as {bot.user.name}")

@bot.command()
async def maestro(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(" Sono entrato nel canale vocale!")
    else:
        await ctx.send(" Devi essere in un canale vocale per farmi entrare.")

@bot.command()
async def meme(ctx):
    voice_client = ctx.guild.voice_client
    if voice_client and not voice_client.is_playing():
        mp3_folder = "mp3"
        files = [f for f in os.listdir(mp3_folder) if f.endswith(".mp3")]
        if not files:
            await ctx.send("❌ Nessun file MP3 trovato nella cartella.")
            return
        chosen_file = random.choice(files)
        filepath = os.path.join(mp3_folder, chosen_file)
        source = discord.FFmpegPCMAudio(filepath)
        voice_client.play(source)
        await ctx.send(f"🎶 Sto riproducendo {chosen_file}")
    else:
        await ctx.send("❌ Il bot non è connesso a un canale vocale o sta già riproducendo qualcosa.")

@bot.command()
async def leave(ctx):
    voice_client = ctx.guild.voice_client
    if voice_client:
        await voice_client.disconnect()
        await ctx.send(" Uscito dal canale vocale.")
    else:
        await ctx.send(" Non sono in un canale vocale.")

@bot.command()
async def fuori(ctx):
    voice_client = ctx.guild.voice_client
    if voice_client and not voice_client.is_playing():
        source = discord.FFmpegPCMAudio("mp3/Esci fuori.mp3")
        voice_client.play(source)
        await ctx.send(" Sto riproducendo l'audio!")
    else:
        await ctx.send(" Non sono connesso a un canale vocale.") 

@bot.command()
async def stile(ctx):
    voice_client = ctx.guild.voice_client
    if voice_client and not voice_client.is_playing():
        source = discord.FFmpegPCMAudio("mp3/Retegui.mp3")
        voice_client.play(source)
        await ctx.send(" Sto riproducendo l'audio!")
    else:
        await ctx.send(" Non sono connesso a un canale vocale.") 

@bot.command()
async def serena(ctx):
    voice_client = ctx.guild.voice_client
    if voice_client and not voice_client.is_playing():
        source = discord.FFmpegPCMAudio("mp3/Serena.mp3")
        voice_client.play(source)
        await ctx.send(" Sto riproducendo l'audio!")
    else:
        await ctx.send(" Non sono connesso a un canale vocale.") 

@bot.command()
async def clown(ctx):
    voice_client = ctx.guild.voice_client
    if voice_client and not voice_client.is_playing():
        source = discord.FFmpegPCMAudio("mp3/Clown.mp3")
        voice_client.play(source)
        await ctx.send(" Sto riproducendo l'audio!")
    else:
        await ctx.send(" Non sono connesso a un canale vocale.") 

if __name__ == "__main__":
    keep_alive()
    import time
    import traceback
    while True:
        try:
            token = os.getenv("DISCORD_TOKEN")
            if not token:
                print("⚠️ DISCORD_TOKEN non impostato nelle variabili d'ambiente!")
                break
            bot.run(token)
        except Exception:
            print("Bot crashato, riavvio in 5 secondi...")
            traceback.print_exc()
            time.sleep(5)
