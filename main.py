import os, nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix=('$', '!'))

@bot.command()
async def ping(ctx):
    await ctx.reply('🏓 pong')

bot.run(os.environ['token'])
