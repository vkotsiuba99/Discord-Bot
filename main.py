import discord

with open('token.txt', 'r') as file:
    TOKEN = file.read()

client = discord.Client()


@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    if message.content.startwith("hello"):
        if str(message.author) == "user.f#3333":
            await message.channel.send("Hello" + message.author + "!")
        else:
            await message.channel.send("Hello, I am a Mipo Bot.")


client.run(f"{TOKEN}")
