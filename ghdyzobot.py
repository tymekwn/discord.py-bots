#Made by @tymekn#3761.
#Inspiration and help from @nola#0258.

import discord
from discord.ext import commands
import random

version = "1.0.0: Initial release."

client = commands.Bot(command_prefix = "DYZO ", case_insensitive = True)

names = ["Beta male", "Moron", "Brainless idiot", "Soy boy"]

nice_names = ["Rather intelligent person", "9/10", "Friend", "Alpha male"]

insults = ["You look like you were created with your mum's left hand.",
    "I'm normally pro-life but you have turned me.",
    "Your mum's so ugly even the sweatiest gamer boys wouldn't buy her bathwater.",
    "Join us for the annual ugly contest! Actually, not you, this is amateurs only - no professionals.",
    "Were you cursed or is this genetic?",
    "They say love makes people blind, I hope I fall in love soon so I won't have to see you again."]

compliments = ["To beat you up, I would require a massive 40%(!) of power",
    "You are almost as incredible as tymekn.",
    "Your pfp looks nice today!",
    "My entity is slightly attached to yours."]

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("DYZO commands"))
    print("Bot is ready")

@client.command()
async def insult(ctx):
    await ctx.send("Dear " + random.choice(names) + ", " + random.choice(insults))

@client.command()
async def offend(ctx, member : discord.Member, *, reason=None):
    await ctx.send("Dear " + member.mention + ", " + random.choice(insults))

@client.command()
async def flatter(ctx, member : discord.Member, *, reason=None):
    await ctx.send("Dear " + member.mention + ", " + random.choice(compliments))

@client.command()
async def compliment(ctx):
    await ctx.send("Dear " + random.choice(nice_names) + ", " + random.choice(compliments))

@client.command()
async def commands(ctx):
    await ctx.send("Commands include: 'offend/flatter @name', 'insult/compliment', 'beef/friend',  as well as 'GitHub' and 'credits'.")

@client.command()
async def beef(ctx):
    beeef = random.choice(insults)
    rando = random.choice(tuple(member.mention for member in ctx.guild.members))
    await ctx.send(f"Dear {rando}, {beeef}" )

@client.command()
async def friend(ctx):
    beeef = random.choice(compliments)
    rando = random.choice(tuple(member.mention for member in ctx.guild.members))
    await ctx.send(f"Dear {rando}, {beeef}" )

@client.command()
async def GitHub(ctx):
    await ctx.send("Check out the official GitHub page at https://github.com/tymekwn/DyzoBot")

@client.command()
async def credits(ctx):
    await ctx.send(f"Made by tymekn#3761 and helped along by nola#0258. Version {version}.")

client.run("Token goes here.")
