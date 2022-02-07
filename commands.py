import discord

from discord.ext import commands

with open('token.txt', 'r') as file:
    TOKEN = file.read()

client = commands.Bot(command_prefix="!")


@client.command()
async def hello(ctx, arg):
    print(ctx.author)
    print(ctx.message)
    print(ctx.guild)


client.run(f"{TOKEN}")
