import  discord
from discord.ext import commands

intents = discord.Intents.all()

client = commands.Bot(command_prefix = '!', 
help_command = None, 
case_insensitive = True,
intents = intents)

@client.event
async def on_ready():
    print("i'm logged with {}".format(client.user))

@client.event
async def on_message(msg):
    if msg.author == client.user: return #For bot not respond self

    if msg.author.bot: return #For bot not to respond to other bots

    await client.process_commands(msg) #Process commands after this event

@client.command() #Syntax of a command
async def ping(ctx):
    await ctx.send('Pong!!') #Bot send message in channel

client.run('Token Here') #Your token bot here
