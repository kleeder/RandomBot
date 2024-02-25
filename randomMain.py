import discord
import SECRETS
import settings


timeChecker = 0


@settings.client.event
async def on_ready():
    print("Ready!")
    await settings.client.change_presence(status=discord.Status.online, activity=discord.Game(name='Den Server stalken'))


@settings.client.event
async def on_message(message):
    by_bot = message.author.bot
    bot_raum = message.channel.id == 208525203582615553
    if bot_raum and not by_bot:
        if message.content.lower() == "!notifyme":
            role = discord.utils.get(message.author.guild.roles, id=406761958952402944)
            if 406761958952402944 in [y.id for y in message.author.roles]:
                await message.author.remove_roles(role)
                await message.channel.send("Role removed")
            else:
                await message.author.add_roles(role)
                await message.channel.send("Role added")

settings.client.run(SECRETS.TOKEN)
