from utilFunctions import embedMsg, embedErr, restoreOrder, bold
from random import randint, shuffle, sample
from math import log, floor
import d20

async def simpleDice(ctx, faces, dice = 1):    
    try:
        dice = int(dice)
    except ValueError:
        await embedErr(ctx, '🎲', 'cantidad no válida', 'la cantidad de dados tiene que ser un enteror.')
        return

    if dice > 1000:
        await embedErr(ctx, '🎲', 'demasiados dados', 'se intentaron lanzar más de 1000 dados.')
    elif faces <= 1:
        await embedErr(ctx, '🎲', 'numero de caras no válido', 'el número de caras tiene que ser mayor que 1')
    elif faces > 1_000_000_000_000:
        await embedErr(ctx, '🎲', 'demasiadas caras', 'se ha intentado lanzar un dado con demasiadas caras.')
    elif dice <= 1:
        await embedMsg(ctx, '🎲', randint(1, faces))
    else:
        total = 0
        desc = ''
        
        if dice <= 10:
            for i in range(dice):
                rand = randint(1, faces)
                total += rand
                desc += f'tirada {i+1}:  {rand}\n'
        elif faces <= 20:
            res = [0] * faces
            
            for i in range(dice):
                rand = randint(0, faces-1)
                res[rand] += 1
                total += rand
    
            for idx, i in enumerate(res):
                desc += f'{idx+1}:  {i} dados\n'
        else:
            power10 = 10**floor(log(faces//2, 10))
            res = [0] * (faces // power10)
            
            for i in range(dice):
                rand = randint(1, faces)
                res[((rand-1) // power10)] += 1
                total += rand
    
            for idx, i in enumerate(res):
                desc += f'{(power10*idx)+1}-{min(faces, power10*(1+idx))}:  {i} dados\n'
        
        await embedMsg(ctx, '🎲', total, desc)

async def simpleDiceParse(ctx, args):    
    if len(args) == 0:
        await simpleDice(ctx, 6)
        return
    
    try:
        faces = int(args[0])
    except ValueError:
        await embedErr(ctx, '🎲', 'cantidad no válida', 'la cantidad de caras tiene que ser un número entero.')
        return

    try:
        amount = int(args[1])
    except (ValueError, IndexError):
        amount = 1

    await simpleDice(ctx, faces, amount)

async def complexDice(ctx, expr):
    try:
        result = d20.roll(expr, stringifier=CustomStringifier())
        if result.total > 1_000_000_000_000:
            await embedErr(ctx, '🎲', 'resultado demasiado grande', 'se han intentado tirar dados demasiado grandes.')
        else:
            await embedMsg(ctx, '🎲', result.total, str(result))
    except (d20.RollSyntaxError, d20.RollValueError):
        await embedErr(ctx, '🎲', 'consulta no válida', 'la consulta contiene errores de sintaxis')
    except d20.TooManyRolls:
        await embedErr(ctx, '🎲', 'demasiados dados', 'se han intentado tirar demasiados dados.')

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
        total = 0
        for val in node.values:
            total += int(self._stringify(val))

        return f'{node.num}d{node.size} ({total})'

async def chooseList(ctx, l):
    try:
        amount = int(l[0])
        l = l[1:]
    except (ValueError, IndexError):
        amount = 1

    if len(l) == 0:
        await embedErr(ctx, '📚', 'lista vacía', 'la lista tiene que contener al menos 1 elemento')
    elif amount > 50:
        await embedErr(ctx, '📚', 'demasiados elementos', '⚠️  50 item choices max.')
    else:
        c = map(bold, restoreOrder(sample(list(enumerate(l)), k = amount)))
        await embedMsg(ctx, '📚', f'choose {amount} out of {len(l)}', 'chosen: ' + ', '.join(c))

async def shuffleList(ctx, l):
    l = list(l)
    
    if len(l) < 2:
        await embedMsg(ctx, '🔀', 'none', '⚠️  list must contain at least 2 elements.')  
    elif len(l) > 50:
        await embedMsg(ctx, '🔀', 'too many items', '⚠️  50 items max.')
    else:
        shuffle(l)
        l = map(bold, l)
        await embedMsg(ctx, '🔀', f'shuffle {len(l)} items', ', '.join(l))

async def chooseTeams(ctx, l):
    try:
        teams = int(l[0])
        l = l[1:]
    except (ValueError, IndexError):
        teams = 2
    teams = max(teams, 2)

    teamIcons = ['🟥  equipo 1', 
                 '🟦  equipo 2', 
                 '🟨  equipo 3', 
                 '🟩  equipo 4', 
                 '🟧  equipo 5', 
                 '🟪  equipo 6', 
                 '⬜  equipo 7',
                 '🟫  equipo 8',
                 '⬛  equipo 9']
    
    if len(l) < teams:
        await embedErr(ctx, '🚩', 'pocas personas', 'cada equipo tiene que tener al menos una persona.')
    elif teams > len(teamIcons):
        await embedMsg(ctx, '🚩', 'demasiados equipos', f'maximo de {len(teamIcons)} equipos')
    else:
        l = list(enumerate(l)) # tuple-to-array conversion
        shuffle(l)
        low = len(l) // teams
        hiCount = len(l) - low * teams
        desc = ''
        j = 0
        for i in range(teams):
            count = low + (1 if hiCount > 0 else 0)
            hiCount -= 1
            str = ', '.join(map(bold, restoreOrder(l[j:j+count])))
            desc += f'{teamIcons[i]}: {str}\n'
            j += count

        await embedMsg(ctx, '🚩', f'{teams} equipos', desc)