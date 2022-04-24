import os
from nextcord.ext import commands
from utilFunctions import embedMsg
import randomCmd, timeCmd, otherCmd
import tictactoeGame

bot = commands.Bot(command_prefix=('$', '!'))

# ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')


# basic commands
@bot.command()
async def ping(ctx): await embedMsg(ctx, '🏓', 'pong', f'latency: {int(1000 * bot.latency)} ms')

@bot.command(aliases=['repetir', 'rep'])
async def repeat(ctx, *args): await otherCmd.repeatMessage(ctx, args)

@bot.command(aliases=['spamear'])
async def spam(ctx, *args): await otherCmd.repeatMessage(ctx, [25] + list(args))


# choice commands
@bot.command(aliases=['elegir'])
async def choose(ctx, *args): await randomCmd.chooseList(ctx, args);

@bot.command(aliases=['barajar'])
async def shuffle(ctx, *args): await randomCmd.shuffleList(ctx, args);

@bot.command(aliases=['equipo'])
async def team(ctx, *args): await randomCmd.chooseTeams(ctx, args);


# dice commands
@bot.command(aliases=['tirar', 'lanzar', 'r'])
async def roll(ctx, *, str): await randomCmd.complexDice(ctx, str)

@bot.command(aliases=['die', 'dado', 'dados', 'd'])
async def dice(ctx, *args): await randomCmd.simpleDiceParse(ctx, args)

@bot.command()
async def d2(ctx, dice = '1'): await randomCmd.simpleDice(ctx, 2, dice)
    
@bot.command()
async def d4(ctx, dice = '1'): await randomCmd.simpleDice(ctx, 4, dice)
    
@bot.command()
async def d6(ctx, dice = '1'): await randomCmd.simpleDice(ctx, 6, dice)

@bot.command()
async def d8(ctx, dice = '1'): await randomCmd.simpleDice(ctx, 8, dice)

@bot.command()
async def d10(ctx, dice = '1'): await randomCmd.simpleDice(ctx, 10, dice)

@bot.command()
async def d12(ctx, dice = '1'): await randomCmd.simpleDice(ctx, 12, dice)

@bot.command()
async def d20(ctx, dice = '1'): await randomCmd.simpleDice(ctx, 20, dice)

@bot.command()
async def d60(ctx, dice = '1'): await randomCmd.simpleDice(ctx, 60, dice)

@bot.command()
async def d100(ctx, dice = '1'): await randomCmd.simpleDice(ctx, 100, dice)

# time commands

@bot.command(aliases = [])
async def clock(ctx, *args): await timeCmd.clock(ctx, args)
    
    
# game commands
@bot.command()
async def tictactoe(ctx): 
    await tictactoeGame.tictactoe(ctx)

# run the bot itself
bot.run(os.environ['token'])