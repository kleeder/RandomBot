import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
Client = discord.Client(intents=intents)
client = commands.Bot(command_prefix="!", intents=intents)
client.remove_command('help')
