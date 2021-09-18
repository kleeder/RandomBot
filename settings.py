import random
import discord
import yaml
from discord.ext import commands

Client = discord.Client()
client = commands.Bot(command_prefix = "!")
client.remove_command('help')