
async def tictactoe(ctx):


def get_board(ctx, board):
    str = ''
    for row in board:
        str += ''.join(ctx.reply(map(asEmote, row))
    return str
            

async def asEmote(cell):
    if cell == 'x': return '❌'
    if cell == 'o': return '⭕'
    return ['1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣'][int(cell)]