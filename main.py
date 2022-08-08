import os
hidden = os.environ.get('discordtoken')
from discord.ext import commands
TOKEN = hidden
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
