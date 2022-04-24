from nextcord import Embed

# helper functions
def embed(emoji, title, desc = '', col = 0x5865F2):  
    if desc == None or desc == '':
        e = Embed(
            title = f'{emoji}  {title}', 
            color = col
        )
    else:
        e = Embed(
            title = f'{emoji}  {title}', 
            description = desc,
            color = col
        )
    return e

async def embedMsg(ctx, emoji, title, desc = '', col = 0x5865F2):  
    return await ctx.reply('', embed = embed(emoji, title, desc, col))

async def embedErr(ctx, emoji, title, desc = '', col = 0x5865F2):  
    return await embedMsg(ctx, emoji, title, desc=f'⚠️ {desc}')

async def embedView(ctx, emoji, title, view, desc = '', col = 0x5865F2):  
    return await ctx.reply('', embed = embed(emoji, title, desc, col), view = view)

def restoreOrder(iter):
    return map(lambda x: x[1], sorted(iter, key = lambda x: x[0]))

def bold(str): 
    return f'**{str}**'