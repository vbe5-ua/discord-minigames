import os
from nextcord.ext import commands
from utilFunctions import embedMsg
from dice import simpleDiceRoll
from choice import chooseList

bot = commands.Bot(command_prefix=('$', '!'))

# ping command
@bot.command()
async def ping(ctx): await embedMsg(ctx, '🏓', 'pong', f'latency: {int(1000 * bot.latency)} ms')

# choice commands
@bot.command()
async def choose(ctx, *args): await chooseList(ctx, args);

# d[N] commands
@bot.command()
async def d2(ctx, dice = 1): await simpleDiceRoll(ctx, 2, dice)
    
@bot.command()
async def d4(ctx, dice = 1): await simpleDiceRoll(ctx, 4, dice)
    
@bot.command()
async def d6(ctx, dice = 1): await simpleDiceRoll(ctx, 6, dice)

@bot.command()
async def d8(ctx, dice = 1): await simpleDiceRoll(ctx, 8, dice)

@bot.command()
async def d10(ctx, dice = 1): await simpleDiceRoll(ctx, 10, dice)

@bot.command()
async def d12(ctx, dice = 1): await simpleDiceRoll(ctx, 12, dice)

@bot.command()
async def d20(ctx, dice = 1): await simpleDiceRoll(ctx, 20, dice)

@bot.command()
async def d100(ctx, dice = 1): await simpleDiceRoll(ctx, 100, dice)

bot.run(os.environ['token'])