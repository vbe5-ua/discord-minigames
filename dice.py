from utilFunctions import embedMsg
from random import randint
from math import log, floor
import d20

async def simpleDiceRoll(ctx, faces, dice = 1):    
    try:
        dice = int(dice)
    except ValueError:
        await embedMsg(ctx, '🎲', 'invalid query', '⚠️ dice count must be an integer.')
        return

    if dice > 1000:
        await embedMsg(ctx, '🎲', 'too many dice', '⚠️ tried to roll more than 1000 dice.')
    elif faces <= 0:
        await embedMsg(ctx, '🎲', 'negative faces', f'⚠️ cannot roll a {faces}-sided die.')
    elif faces > 1_000_000_000_000:
        await embedMsg(ctx, '🎲', 'too many faces', '⚠️ tried to roll a dice with more than a trillion faces.')
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

async def complexDiceRoll(ctx, expr):
    try:
        result = d20.roll(expr, stringifier=CustomStringifier())
        if result.total > 1_000_000_000_000:
            await embedMsg(ctx, '🎲', 'result too large', f'⚠️ result was bigger than 1 trillion.')
        else:
            await embedMsg(ctx, '🎲', result.total, str(result))
    except (d20.RollSyntaxError, d20.RollValueError) as e:
        await embedMsg(ctx, '🎲', 'invalid query', f'⚠️ {str(e).lower()}')
    except d20.TooManyRolls:
        await embedMsg(ctx, '🎲', 'too many dice', '⚠️ tried to roll more than 1000 dice.')

class CustomStringifier(d20.MarkdownStringifier):        
    def _str_expression(self, node):
        return f"{self._stringify(node.roll)} = {node.total}"

    def _str_die(self, node):
        rolls = []        
        for val in node.values:
            inside = self._stringify(val)
            rolls.append(inside)

        return ' '.join(rolls)
    
    def _str_dice(self, node):
        if len(node.values) > 10:
            total = 0
            for val in node.values:
                total += int(self._stringify(val))

            print(f'total = {total}')
            return f'{node.num}d{node.size} ({total})'
        else:
            rolls = []
            total = 0
            for val in node.values:
                str = self._stringify(val)
                rolls.append(str)
                total += int(str)
    
            print(rolls);
            return f'{node.num}d{node.size} ({total}, ' + ' '.join(rolls) + ')'