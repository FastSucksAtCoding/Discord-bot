# Imports
import discord 
import json
from discord.ext import commands


# Prefix
def get_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = get_prefix)

@client.event 
async def on_guild_join(guild):
	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefixes[str(guild.id)] = ">>"

	with open("prefixes.json", "w") as f:
		json.dump(prefixes, f, indent = 4)

@client.event 
async def on_guild_remove(guild):
	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefixes.pop(str(guild.id))

	with open("prefixes.json", "w") as f:
		json.dump(prefixes, f, indent = 4)


# Prefix Command 
@client.command()
@commands.has_permissions(administrator=True)
async def prefix(ctx, prefix):
	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefixes[str(guild.id)] = prefix

	with open("prefixes.json", "w") as f:
		json.dump(prefixes, f, indent = 4)
		

# Bot Online print
@client.event
async def on_ready():
    print("Bot is online!")


# Bot status 
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="status"))


# Ping command 
@client.command()
async def ping(ctx):
    await ctx.send(f"Bot ping is {round(client.latency * 1000)}ms")


# ban command 
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)


# Kick command 
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)


# Clear command 
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)


# Info Command 
@client.command()
async def info(ctx):
	await ctx.send("**Info**\n"
    "Version: 1.2\n"
    "Source code: https://github.com/fastsucksatcoding/discord-bot")


# Help Command 
client.remove_command("help")
@client.command()
async def help(ctx):
    await ctx.send("**Help**\n"
    "Prefix - Changes prefix\n"
    "Ban - bans user from guild\n"
    "Kick - kicks user from guild\n"
    "Clear - clears messages\n"
    "Ping - shows bot ping\n"
    "Info - Shows bot information\n")


# Version command 
@client.command()
async def version(ctx):
    await ctx.send("Bot version: 1.2")


# Token
client.run("Token")
