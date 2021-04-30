# Don't even dare to sell this, I dont care you can claim it that you made it, but if you dare to sell it ill slice your throat really slowly and painfully <3
# I'm not gonna update this ever unless it's minor bug or something similar, so yeah...

# Import 
import discord
from discord.ext import commands 

# Prefix 
bot = commands.Bot(command_prefix=">>")

# Bot Online print
@bot.event
async def on_ready():
    print("Bot is online!")

# Bot status 
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="status"))

# Ping command 
@bot.command()
async def ping(ctx):
    await ctx.send(f"Bot ping is {round(client.latency * 1000})ms")

# github command 
@bot.command()
async def github(ctx):
    await ctx.send("Github: https://github.com/fastsucksatcoding")

# ban command 
@bot.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

# Kick command 
@bot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

# Clear command 
@bot.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

# Token 
bot.run("token")

