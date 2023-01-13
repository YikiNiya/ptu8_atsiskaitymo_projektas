import random
from zodziai import sarasas
import string

def gauti_tinkama_zodi(sarasas):
    zodis = random.choice(sarasas)
    while '-' in zodis or ' ' in zodis:
        zodis = random.choice(sarasas)
    return zodis.upper()
    
def pakaruoklis():
    zodis = gauti_tinkama_zodi(sarasas)
    raides = set(zodis)
    abecele = set(string.ascii_uppercase)
    naudotos_raides = set()

    gyvybes = 7

    while len(raides) > 0 and gyvybes > 0:
        print(f'Turite {gyvybes} gyvybes, ir jusu ivestos raides yra: ', ' '.join(naudotos_raides))
        
        zodzis_is_saraso = [raide 
        if raide in naudotos_raides else '-' for raide in zodis]
        print(f'Spejamas zodis: ', ' '.join(zodzis_is_saraso))

        spejama_raide = input('Kokia raide: ').upper()
        if spejama_raide in abecele - naudotos_raides:     
            naudotos_raides.add(spejama_raide)
            if spejama_raide in raides:
                raides.remove(spejama_raide)

            else:
                gyvybes = gyvybes - 1
                print('Tokia raide neegzistuoja siame zodyje.')

        elif spejama_raide in naudotos_raides:
            print('Sita raide jau buvo speta, bandykite kita raide.')

        else:
            print('Turi buti ivesta raide. Bandykite dar karta.')

    if gyvybes == 0:
        print(f'Jus mirete. Zodis buvo: ', zodis)
    else:
        print('Jus laimejote!', zodis)


pakaruoklis()
#zaidejas = input('Spekite raide: ')
#print(zaidejas)