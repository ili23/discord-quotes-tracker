import discord
from config import token
from discord.ext import commands
TOKEN = "OTgxNjcwODg2ODkxNDU0NTc0.GM5tv9.T1b5UDmGzqR20KsB6HQIypOG0tTvY5HaTSlPc0"
client = commands.Bot(command_prefix="$")


@client.command()
async def count(ctx, arg):
    if ctx.channel.name == "quotes":
        await ctx.message.delete()
        message_history = await ctx.channel.history(limit = 1000).flatten()
        counter = 0
        for msg in message_history:
            if arg in msg.content:
                counter += 1
        await ctx.send("Count: " + str(counter), delete_after = 10.0)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
client.run(TOKEN)
