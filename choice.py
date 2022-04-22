from utilFunctions import embedMsg
from random import choices

async def chooseList(ctx, list):
    try:
        amount = int(list[0])
        list = list[1:]
    except (ValueError, IndexError):
        amount = 1

    if len(list) == 0:
        await embedMsg(ctx, '📚', 'none', 'list must contain at least 1 element.')  
    elif amount > 50:
        await embedMsg(ctx, '📚', 'too many items', 'max: 50 item choices.')
    else:
        c = choices(list, k = amount)
        await embedMsg(ctx, '📚', f'chose {amount} ' + ('item' if (amount == 1) else 'items'), ', '.join(c))
