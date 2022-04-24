from utilFunctions import embedMsg, embedErr
from pytz import timezone
from datetime import datetime
from collections import namedtuple

TZ = namedtuple('TZ', ('zone', 'aliases'))

tzs = {
    '🇪🇸 es': TZ('Europe/Madrid', ('es', 'esp', 'españa', 'spain')),
    '🇮🇨 ic': TZ('Atlantic/Canary', ('ic', 'ica', 'isl', 'is', 'islas canarias', 'canarias', 'canary', 'canary islands')),
    '🇲🇽 mx': TZ('America/Mexico_City', ('mx', 'me', 'mex', 'méxico')),
    '🇦🇷 ar': TZ('America/Argentina/Buenos_Aires', ('ar', 'arg', 'argentina')),
    '🇨🇴 co': TZ('America/Bogota', ('co', 'col', 'colombia')),
    '🇧🇴 bo': TZ('America/La_Paz', ('bo', 'bol', 'bolivia')),
}

def getAlias(zone):
    for tz, al in tzs.items():
        if zone in al.aliases:
            return tz
    return None

async def clock(ctx, zonesRaw):    
    if len(zonesRaw) == 0 or zonesRaw[0] == 'all':
        zones = list(tzs.keys())
    else:
        zones = list(map(getAlias, zonesRaw))
        for z, raw in zip(zones, zonesRaw):
            if z == None:
                await embedErr(ctx, '🕒', 'zona horaria invalida', f'la zona horaria \'{raw}\' no es válida.)')
                return

    if len(zones) == 1:
        await embedMsg(ctx, '🕒', f'{datetime.now(tz=timezone(tzs[zones[0]].zone)) :%H:%M} ({zones[0]})')
    else:
        desc = ''
        print(zones)
        for zone in zones[1:]:
            desc += f'{zone}: {datetime.now(tz=timezone(tzs[zone].zone)) :%H:%M}\n'
            
        await embedMsg(ctx, '🕒', f'{datetime.now(tz=timezone(tzs[zones[0]].zone)) :%H:%M} ({zones[0]})', desc)