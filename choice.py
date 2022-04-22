from utilFunctions import embedMsg
from random import choices, shuffle

async def chooseList(ctx, list):
    try:
        amount = int(list[0])
        list = list[1:]
    except (ValueError, IndexError):
        amount = 1

    if len(list) == 0:
        await embedMsg(ctx, '📚', 'none', '⚠️  list must contain at least 1 element')  
    elif amount > 50:
        await embedMsg(ctx, '📚', 'too many items', '⚠️  max: 50 item choices')
    else:
        c = choices(list, k = amount)
        await embedMsg(ctx, '📚', f'chose {amount} ' + ('item' if (amount == 1) else 'items'), ', '.join(c))

async def chooseTeams(ctx, list):
    try:
        teams = int(list[0])
        list = list[1:]
    except (ValueError, IndexError):
        teams = 2

    teamIcons = ['🟥  red team', 
                 '🟦  blue team', 
                 '🟨  yellow team', 
                 '🟩  green team', 
                 '🟧  orange team', 
                 '🟪  purple team', 
                 '⬜  white team',
                 '🟫  brown team',
                 '⬛  black team']
    
    if len(list) <= teams:
        await embedMsg(ctx, '🚩', 'too few people', '⚠️  each team must contain at least 1 person')
    elif teams > len(teamIcons):
        await embedMsg(ctx, '🚩', 'too many teams', '⚠️  max: 9 teams')
    else:
        list = [x for xs in list for x in xs] # tuple-to-array conversion
        shuffle(list)
        low = len(list) // teams
        hiCount = len(list) - low * teams
        desc = ''
        j = 0
        for i in range(teams):
            count = low + (1 if hiCount > 0 else 0)
            hiCount -= 1
            str = ', '.join(list[j:j+count])
            desc += f'{teamIcons[i]}: {str}\n'
            j += count

        await embedMsg(ctx, '🚩', f'{teams} teams', desc)