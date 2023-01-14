import random
from zodziai import sarasas
import string

def pasleptas_zodis(sarasas):
    zodis = random.choice(sarasas)
    while '-' in zodis or ' ' in zodis:
        zodis = random.choice(sarasas)
    return zodis.upper()
    
def kartuves():
    zodis = pasleptas_zodis(sarasas)
    raides = set(zodis)
    abecele = set(string.ascii_uppercase)
    naudotos_raides = set()
    gyvybes = 10

    while len(raides) > 0 and gyvybes > 0:
        print(f'Turite {gyvybes} gyvybes, ir jūsų įvestos raidės yra: ', ' '.join(naudotos_raides))
        
        zodzis_is_saraso = [raide 
        if raide in naudotos_raides else '-' for raide in zodis]
        print(f'Spejamas žodis: ', ' '.join(zodzis_is_saraso))

        spejama_raide = input('Kokia raidė: ').upper()
        if spejama_raide in abecele - naudotos_raides:     
            naudotos_raides.add(spejama_raide)
            if spejama_raide in raides:
                raides.remove(spejama_raide)

            else:
                gyvybes = gyvybes - 1
                #print('Tokia raide neegzistuoja siame zodyje.')
                if gyvybes == 9:
                    print('           ')
                    print(' |         ')
                    print(' |         ')
                    print(' |         ')
                    print(' |         ')
                    print(' |         ')
                    print('_|___      ')
                    print('Tokia raide neegzistuoja šiame žodyje. Bandykite dar karta')
                if gyvybes == 8:
                     print('_________  ')                                                                   
                     print(' |         ')
                     print(' |         ')
                     print(' |         ')
                     print(' |         ')
                     print('_|___      ')
                     print('Tokia raide neegzistuoja šiame žodyje. Bandykite dar karta')
                    
                elif gyvybes == 7:
                    print('_________  ')
                    print(' | /       ')
                    print(' |/        ')
                    print(' |         ')
                    print(' |         ')
                    print(' |         ')
                    print('_|___      ')
                    print('Tokia raide neegzistuoja šiame žodyje. Bandykite dar karta')
                elif gyvybes == 6:
                    print('_________  ')
                    print(' | /   |   ')
                    print(' |/    |   ')
                    print(' |         ')
                    print(' |         ')
                    print(' |         ')
                    print('_|___      ')
                    print('Tokia raide neegzistuoja šiame žodyje. Bandykite dar karta')
                elif gyvybes == 5:
                    print('_________  ')
                    print(' | /   |   ')
                    print(' |/    |   ')
                    print(' |      O  ')
                    print(' |         ')
                    print(' |         ')
                    print('_|___      ')
                    print('Tokia raide neegzistuoja šiame žodyje. Bandykite dar karta')
                elif gyvybes == 4:
                    print('_________  ')
                    print(' | /   |   ')
                    print(' |/    |   ')
                    print(' |      O  ')
                    print(' |     |   ')
                    print(' |         ')
                    print('_|___      ')
                    print('Tokia raide neegzistuoja šiame žodyje. Bandykite dar karta')
                elif gyvybes == 3:
                    print('_________  ')
                    print(' | /   |   ')
                    print(' |/    |   ')
                    print(' |      O  ')
                    print(' |    /|   ')
                    print(' |         ')
                    print('_|___      ')
                    print('Tokia raide neegzistuoja šiame žodyje. Bandykite dar karta')
                elif gyvybes == 2:
                    print('_________  ')
                    print(' | /   |   ')
                    print(' |/    |   ')
                    print(' |      O  ')
                    print(' |    /|\  ')
                    print(' |         ')
                    print('_|___      ')
                    print('Tokia raide neegzistuoja šiame žodyje. Bandykite dar karta')
                elif gyvybes == 1:
                    print('_________  ')
                    print(' | /   |   ')
                    print(' |/    |   ')
                    print(' |      O  ')
                    print(' |    /|\  ')
                    print(' |    /    ')
                    print('_|___      ')
                    print('Tokia raide neegzistuoja šiame žodyje. Bandykite dar karta')

        elif spejama_raide in naudotos_raides:
            print('Šita raide jau buvo spėta, bandykite kita raide.')

        else:
            print('Turi būti įvesta raidė. Bandykite dar karta.')

    if gyvybes == 0:
        print('_________  ')
        print(' | /   |   ')
        print(' |/    |   ')
        print(' |      O  ')
        print(' |    /|\  ')
        print(' |    / \  ')
        print('_|___      ')
        print(f'Jus mirėte. Žodis buvo: ', zodis)
    else:
        print('_________       ')
        print(' | /   |        ')
        print(' |/    |        ')
        print(' |              ')
        print(' |         \O/  ')
        print(' |          |   ')
        print('_|___      / \  ')
        print('Jus laimėjote! Atspėjote žodi: ', zodis)

kartuves()