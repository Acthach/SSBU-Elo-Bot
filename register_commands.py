import discord
from discord.ext import commands

"""
import requests
import yaml

TOKEN ='MTM0MDUzMzI5OTQ1MzQ5NzM5NA.GlS_fa.BYJFUbPcxIZwqztyuh6GRldURsb1pvYyx67JkE'
Channel_ID = '1340551594697297930'
URL = f''
"""

TOKEN ='MTM0MDUzMzI5OTQ1MzQ5NzM5NA.GlS_fa.BYJFUbPcxIZwqztyuh6GRldURsb1pvYyx67JkE'
Channel_ID = '1340551594697297930'

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("testing")
    channel = bot.get_channel(Channel_ID)
    await channel.send("testing")

bot.run(TOKEN)
