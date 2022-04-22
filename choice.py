from utilFunctions import embedMsg, restoreOrder, bold
from random import shuffle, sample

async def chooseList(ctx, l):
    try:
        amount = int(l[0])
        l = l[1:]
    except (ValueError, IndexError):
        amount = 1

    if len(l) == 0:
        await embedMsg(ctx, '📚', 'none', '⚠️  list must contain at least 1 element.')  
    elif amount > 50:
        await embedMsg(ctx, '📚', 'too many items', '⚠️  50 item choices max.')
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

    teamIcons = ['🟥  team 1', 
                 '🟦  team 2', 
                 '🟨  team 3', 
                 '🟩  team 4', 
                 '🟧  team 5', 
                 '🟪  team 6', 
                 '⬜  team 7',
                 '🟫  team 8',
                 '⬛  team 9']
    
    if len(l) < teams:
        await embedMsg(ctx, '🚩', 'too few people', '⚠️  each team must contain at least 1 person')
    elif teams > len(teamIcons):
        await embedMsg(ctx, '🚩', 'too many teams', f'⚠️  maximum of {len(teamIcons)} teams')
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

        await embedMsg(ctx, '🚩', f'{teams} teams', desc)