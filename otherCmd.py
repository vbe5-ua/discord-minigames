from utilFunctions import embedMsg, embedErr

async def repeatMessage(ctx, l):
    try:
        times = int(l[0])
        l = l[1:]
    except ValueError:
        times = 1

    content = ' '.join(l)

    if times > 25:
        await embedErr(ctx, '🔁', 'demasiadas veces', 'no se puede repetir mas de 25 veces.')
    else:
        times = max(times, 1)
        title = 'repetir' if times == 1 else f'repetir {times} veces'
        await embedMsg(ctx, '🔁', title, f'{content}\n' * times)

