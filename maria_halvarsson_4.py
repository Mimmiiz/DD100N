# Namn: Maria Halvarsson
# Datum: 2021-03-15
# Kurskod: DD100N

# Detta är ett program för spelet tre-i-rad (luffarschack) där två spelare spelar mot varandra.
# Varje spelare anger sitt namn innan spelet börjar och turas om att lägga sina "brickor" på spelplanen.
# För att en spelare ska kunna vinna måste spelaren få tre i rad, antingen på raden, kolumnen eller diagonalen.
# Om ingen spelare vinner är spelet oavgjort.

#För att rita ut spelplanen används Box Drawing Characters": https://en.wikipedia.org/wiki/Box-drawing_character
def skrivUtSpelplan(spelplan):
    """ Skriver ut spelplanen utifrån hur spelplansmatrisen ser ut.
    Inparameter: spelplan(matris)
    Returvrde: inget returvärde
    """
    print('    A   B   C  ')
    print('  ┏━━━┳━━━┳━━━┓')
    radRäknare = 0
    for rad in spelplan:
        radRäknare += 1
        print(str(radRäknare) +' ┃', end=' ')
        for ruta in rad:
            print('' + ruta, end=' ')
            print('┃', end=' ')
        print()
        if radRäknare < 3:          #Efter sista raden vill vi inte göra detta
            print('  ┣━━━╋━━━╋━━━┫')
    print('  ┗━━━┻━━━┻━━━┛')          #Utan istället detta


def kontrolleraRader(spelplan):
    """Kontrollerar om det finns tre likadana tecken på någon rad och returnerar då True, annars False
    Inparameter: spelplan (matris)
    Returvärde: True om det finns vinnare annars False (booleskt värde)
    """
    
    for i in range(3):
        if ' ' not in [spelplan[i][0], spelplan[i][1], spelplan[i][2]]:
            if spelplan[i][0] == spelplan[i][1] == spelplan[i][2]:
                return True

    return False


def kontrolleraKolumner(spelplan):
    """Kontrollerar om det finns tre likadana tecken i rad i kolumnen, om det finns returneras True, annars False.
    Inparameter: spelplan (matris)
    Returvärde: True om det finns tre likadana tecken (en vinnare), annars False (booleskt värde)
    """

    for i in range(3):
        if ' ' not in [spelplan[0][i], spelplan[1][i], spelplan[2][i]]:
            if spelplan[0][i] == spelplan[1][i] == spelplan[2][i]:
                return True

    return False


def kontrolleraDiagonaler(spelplan):
    """Kontrollerar om det finns tre likadana tecken på någon av diagonalerna, om det finns returneras True, annars False.
    Inparameter: spelplan (matris)
    Returvärde: True om det finns tre likadana tecken (en vinnare), annars False (booleskt värde)
    """

    #första diagonalen, uppe till vänster till nere till höger
    if ' ' not in [spelplan[0][0], spelplan[1][1], spelplan[2][2]] and spelplan[0][0] == spelplan[1][1] == spelplan[2][2]:
        return True
    elif ' ' not in [spelplan[0][2], spelplan[1][1], spelplan[2][0]] and spelplan[0][2] == spelplan[1][1] == spelplan[2][0]:
        return True
    else:
        return False

def ledigRuta(spelplan, rad, kolumn):
    """Kontrollerar om rutan på spelplanen med den angivna raden och kolumnen är ledig.
    Om rutan är ledig returneras True, annars False.
    Inparameter: spelplan (matris), rad (integer), kolumn(integer)
    Returvärde: True om rutan är ledig, annars False (booleskt värde)
    """
    if ' ' in spelplan[rad][kolumn]:
        return True
    else:
        return False

def finnsVinnare(spelplan):
    """Kontrollerar ifall det finns en vinnare genom att analysera spelplanen, om en vinnare finns
    returneras True, annars False.
    Inparameter: spelplan (matris)
    Returvärde: True om det finns vinnare, annars False (booleskt värde)
    """

    if kontrolleraKolumner(spelplan) or kontrolleraDiagonaler(spelplan) or kontrolleraRader(spelplan):
        return True
    else:
        return False

def oavgjort(spelplan):
    """ Kontrollerar om det har blivit oavgjort, om det är oavgjort returneras True, annars False.
    Inparameter: spelplan (matris)
    Returvärde: True om det är oavgjort, annars False (booleskt värde)
    """
    if finnsVinnare(spelplan):
        return False

    for rad in spelplan:
        for element in rad:
            if element ==' ':
                return False
    return True

def tolkaInmatning(inmatning):
    """ Tolkar inmatningen från användaren genom att omvandla den angivna bokstaven (kolumnen) till det korresponderande
    kolumnnummret i matrisen och returnerar värdet för rad och kolumn.
    Inparameter: inmatning (String)
    Returvärde: rad (integer), kolumn (integer)
    """

    bokstav = inmatning[0].upper() #Använder .upper() för att göra om alla inmatade bokstäver till versaler
    rad = int(inmatning[1])-1
    if bokstav == 'A':
        kolumn = 0
    elif bokstav == 'B':
        kolumn = 1
    elif bokstav == 'C':
        kolumn = 2
    return rad, kolumn


def startSpelare():
    """ Returnerar slumpmässigt ett tal mellan 0 och 1 som anger vilken spelare som ska börja.
    Inparameter: inget
    Returvärde: ett heltal som är 0 eller 1
    """
    from random import randint
    return randint(0, 2)


def spela(spelarNamn1, spelarNamn2):
    """ Startar spelet genom att ange spelare 1 och spelare 2. Varje spelare turas om att lägga på spelplanen.
    Efter varje runda kontrolleras det om det finns en vinnare, om det finns så avslutas spelet. Varje runda
    kontrolleras det även om spelet är oavgjort, då avslutas också spelet.
    Inparameter: spelarNamn1 (String), spelarNamn2 (String)
    Returvärde: inget returvärde
    """
    print("Då kör vi!")
    print("Ange de koordinater du vill lägga på på formatet A1, B3 osv.")
    spelplan = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

    spelarLista = [spelarNamn1, spelarNamn2]
    vemsTur = startSpelare()
    while finnsVinnare(spelplan) == False:
        vemsTur = (vemsTur+1)% 2 #vemsTur ska aldrig bli 2, utan börja om igen på 0, %-är modul dvs resten vid heltals division.
        skrivUtSpelplan(spelplan)
        if vemsTur == 0:
            markör = 'X'
        else:
            markör = 'O'
        inmatning = input(str(spelarLista[vemsTur]) + "s tur att spela: ")
        rad,kolumn = tolkaInmatning(inmatning)
        while ledigRuta(spelplan, rad, kolumn) == False:
            print("Rutan är upptagen, ange ett nytt värde: ")
            inmatning = input(str())
            rad,kolumn = tolkaInmatning(inmatning)
        spelplan[rad][kolumn] = markör
        if oavgjort(spelplan) == True:
            skrivUtSpelplan(spelplan)
            print("Det blev oavgjort!")
            break
        
    if not oavgjort(spelplan):
        skrivUtSpelplan(spelplan)
        print("Grattis " + str(spelarLista[vemsTur]) + " du vann!")


def huvudfunktion():
    """ Detta är huvudfunktionen där programmet startas.
    Inparameter: inget
    Utparamter: inget
    """
    print("Hej och väkommen till Tre-i-rad!")
    spelarNamn1 = input("Vad heter spelare 1? ")
    spelarNamn2 = input("Vad heter spelare 2? ")
    spela(spelarNamn1, spelarNamn2)

huvudfunktion()
