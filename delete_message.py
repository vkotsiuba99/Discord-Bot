import discord

with open('token.txt', 'r') as file:
    TOKEN = file.read()

client = discord.Client()


@client.event
async def on_message(message):
    if str(message.channel) == "general" and message.content != "":
        await message.channel.purge(limit=1)


client.run(f"{TOKEN}")
