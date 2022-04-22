import os
from nextcord.ext import commands
from utilFunctions import embedMsg
from dice import simpleDiceRoll, complexDiceRoll
from choice import chooseList, chooseTeams, shuffleList

bot = commands.Bot(command_prefix=('$', '!'))

# ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')

# ping command
@bot.command()
async def ping(ctx): await embedMsg(ctx, '🏓', 'pong', f'latency: {int(1000 * bot.latency)} ms')

# choice commands
@bot.command()
async def choose(ctx, *args): await chooseList(ctx, args);

@bot.command()
async def shuffle(ctx, *args): await shuffleList(ctx, args);

@bot.command()
async def team(ctx, *args): await chooseTeams(ctx, args);

# dice commands
@bot.command()
async def roll(ctx, *, str): await complexDiceRoll(ctx, str)
    
@bot.command()
async def d2(ctx, dice = '1'): await simpleDiceRoll(ctx, 2, dice)
    
@bot.command()
async def d4(ctx, dice = '1'): await simpleDiceRoll(ctx, 4, dice)
    
@bot.command()
async def d6(ctx, dice = '1'): await simpleDiceRoll(ctx, 6, dice)

@bot.command()
async def d8(ctx, dice = '1'): await simpleDiceRoll(ctx, 8, dice)

@bot.command()
async def d10(ctx, dice = '1'): await simpleDiceRoll(ctx, 10, dice)

@bot.command()
async def d12(ctx, dice = '1'): await simpleDiceRoll(ctx, 12, dice)

@bot.command()
async def d20(ctx, dice = '1'): await simpleDiceRoll(ctx, 20, dice)

@bot.command()
async def d100(ctx, dice = '1'): await simpleDiceRoll(ctx, 100, dice)

bot.run(os.environ['token'])