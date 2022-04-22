from utilFunctions import embedMsg
from random import randint
from math import floor, log

async def simpleDiceRoll(ctx, faces, dice = 1):    
    try:
        dice = int(dice)
    except ValueError:
        dice = 1

    if dice > 1000:
        await embedMsg(ctx, '🎲', 'too many dice', 'max: 1000 dice')
    elif faces > 100000:
        await embedMsg(ctx, '🎲', 'too many faces', 'max: 100000 faces per die')
    elif dice <= 1:
        await embedMsg(ctx, '🎲', randint(1, faces))
    else:
        total = 0
        desc = ''
        
        if dice <= 10:
            for i in range(dice):
                rand = randint(1, faces+1)
                total += rand
                desc += f'roll #{i+1}:  {rand}\n'
        elif faces <= 20:
            res = [0] * faces
            
            for i in range(dice):
                rand = randint(0, faces-1)
                res[rand] += 1
                total += rand
    
            for idx, i in enumerate(res):
                desc += f'rolled {idx+1}:  {i} times\n'
        else:
            power10 = 10**floor(log(faces//2, 10))
            res = [0] * (faces // power10)
            
            for i in range(dice):
                rand = randint(1, faces)
                res[((rand-1) // power10)] += 1
                total += rand
    
            for idx, i in enumerate(res):
                desc += f'rolled {(power10*idx)+1}-{min(faces, power10*(1+idx))}:  {i} times\n'
        
        await embedMsg(ctx, '🎲', total, desc)
