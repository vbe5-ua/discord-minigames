import os
from random import randint
#from nextcord import Embed
from nextcord.ext import commands
from embed import embedMsg

bot = commands.Bot(command_prefix=('$', '!'))

# ping command
@bot.command()
async def ping(ctx):
    await embedMsg(ctx, '🏓', 'pong', f'latency: {int(1000 * bot.latency)} ms')

# d6 command
@bot.command()
async def d6(ctx, dice = 1):    
    try:
        dice = int(dice)
    except ValueError:
        dice = 1

    if dice > 1000:
        embedMsg(ctx, '🎲', 'too many dice')
    elif dice > 10:
        res = [0, 0, 0, 0, 0, 0]
        total = 0
        desc = ''
        for i in range(dice):
            rand = randint(0, 5)
            res[rand] += 1
            total += rand

        for idx, i in enumerate(res):
            desc += f'rolled {idx+1}:  {i}\n'

        await embedMsg(ctx, '🎲', total, desc)     
    elif dice <= 1:    
        await embedMsg(ctx, '🎲', randint(1, 6))
    else:
        total = 0
        desc = ''
        for i in range(dice):
            rand = randint(1, 6)
            total += rand
            desc += f'roll {i+1}:  {rand}\n'

        await embedMsg(ctx, '🎲', total, desc)
            
bot.run(os.environ['token'])