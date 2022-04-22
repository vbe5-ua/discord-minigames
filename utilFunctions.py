from nextcord import Embed
import re

# helper functions
async def embedMsg(ctx, emoji, title, desc = '', col = 0x5865F2):  
    if desc == None or desc == '':
        e = Embed(
            title = f'{emoji}    {title}', 
            description = desc,
            color = col
        )
    else:
        e = Embed(
            title = f'{emoji}    {title}', 
            description = desc,
            color = col
        )
    await ctx.reply('', embed = e)

async def parseMention(bot, msg):
    re.search()