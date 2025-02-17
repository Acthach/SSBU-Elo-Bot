import discord
from discord.ext import commands
TOKEN ='MTM0MDUzMzI5OTQ1MzQ5NzM5NA.GlS_fa.BYJFUbPcxIZwqztyuh6GRldURsb1pvYyx67JkE'
Channel_ID = '1340551594697297930'
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
