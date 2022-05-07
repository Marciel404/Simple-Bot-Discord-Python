import  discord
from discord.ext import commands

intents = discord.Intents.all()

client = commands.Bot( #Declarate bot
command_prefix = '!', #Prefix Bot
help_command = None, #remove default command help
case_insensitive = True, #Response the command 
intents = intents #Intents discord
)

@client.event
async def on_ready():
    print("i'm logged with {}".format(client.user))

@client.event
async def on_message(msg):
    if msg.author == client.user: return #For bot not respond self

    if msg.author.bot: return #For bot not to respond to other bots

    await client.process_commands(msg) #Process commands after this event

@client.command() #Sintax command
async def ping(ctx):

    ping = client.latency * 1000 #Get bot latency

    e = discord.Embed( #Create embed
    title ='Ping', #Set title for embed
    description = 'My ping is {}'.format(int(ping)), #Set body for embed
    color = 15552 #Set color for embed
    )

    await ctx.send(embed = e) #Send embed in channel

client.run('Token bot here')
