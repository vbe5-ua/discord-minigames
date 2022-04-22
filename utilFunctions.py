from nextcord import Embed

# helper functions
async def embedMsg(ctx, emoji, title, desc = '', col = 0x5865F2):  
    if desc == None or desc == '':
        e = Embed(
            title = f'{emoji}  {title}', 
            description = desc,
            color = col
        )
    else:
        e = Embed(
            title = f'{emoji}  {title}', 
            description = desc,
            color = col
        )
    await ctx.reply('', embed = e)

def restoreOrder(iter):
    return map(lambda x: x[1], sorted(iter, key = lambda x: x[0]))

def bold(str): 
    return f'**{str}**'