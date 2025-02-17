import discord
from discord.ext import commands
TOKEN =''
Channel_ID = ''
intents = discord.Intents.default()
intents.members = True
intents.message_content = True



bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("testing")
    channel = bot.get_channel(Channel_ID)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

bot.run(TOKEN)
