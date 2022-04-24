from utilFunctions import embedMsg
from asyncio import TimeoutError

async def tictactoe(ctx, bot, currentUser, otherUser):
    def is_correct(m):
        return m.author == currentUser

    answerRange = range(1, 10)
    board = [':one:', ':two:', ':three:', ':four:', ':five:', ':six:', ':seven:', ':eight:', ':nine:']
    playerSymbol = ':x:'
    otherSymbol = ':o:'
    while True:
        answer = None
        await ctx.send(f'it\'s your turn <@{currentUser.id}>')
        await printBoard(ctx, board)

        while answer == None or answer not in answerRange or board[answer-1] == 'x' or board[answer-1] == 'o':
            try:
                msg = await bot.wait_for('message', check=is_correct, timeout = 60)
                answer = int(msg.content)
            except TimeoutError:
                return await embedMsg(ctx, '⚔️', f'{otherUser} won', f'{currentUser} took too long to play (> 60s).')
            except ValueError:
                await ctx.send('{currentUser}, please send a valid image!')
    
        board[answer-1] = playerSymbol
        # TODO: check for game over
    
async def printBoard(ctx, board):
    for i in range(3):
        j = 3*i
        str = f'{board[j]} {board[j+1]} {board[j+2]}'
        await ctx.send(str)

def asEmote(cell):
    if cell == 'x': return '❌'
    if cell == 'o': return '⭕'
    return ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣'][int(cell) - 1]