#############################################
# Magnus Pins
# 2.W   
# 02-12-2024
#############################################

#Har ikke valgt at lave et input (altså et input hvor folk kan skrive deres eget cpr nummer ind, da jeg mener det ikke er sikkert nok)
#Der er kun 526 mulige kombinationer af cpr numre.

#Importere nødvendige biblioteker
from datetime import date
from numpy import random

class validater:
    kontrol :int = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]
    cpr: int = 0
    sum: int = 0

    #Initialisere cpr nummeret
    def __init__(self, cpr: int) -> None:
        self.cpr = cpr

    #Kontrol beregning af cpr nr. er gyldigt med en 10 cifret kontrol.
    def kontrolberegning(self) -> int:
        cpr = self.cpr.replace('-', '')

        #Tjekker om cpr nummeret er 10 cifre langt og kun indeholder tal
        if len(cpr) != 10:
            ValueError("CPR nummeret skal være 10 cifre langt")
        if not cpr.isdigit():
            ValueError("CPR nummeret må kun indeholde tal")

        #Laver cpr om til en liste af integers
        cpr : int = [int(x) for x in cpr]

        #Beregner summen af cpr nummeret
        for i in range(10):
            self.sum += cpr[i] * self.kontrol[i]
        
        return self.sum
    
    #Tjekker om cpr nummeret er mand eller kvinde
    def sex(self) -> str:
        if int(self.cpr[10]) % 2 == 0:
            return "Kvinde"
        else:
            return "Mand"

    #Checker om cpr nummeret er gyldigt
    def check(self) -> bool:
        #Tjekker om summen af cpr nummeret er deleligt med 11
        if self.sum % 11 == 0:
            print("CPR nummeret er gyldigt \n")
            return True
        else:
            print("CPR nummeret er ugyldigt \n")
            return False

class generate:
    dato = date.today()
    
    #Generere et cpr nummer
    def bruceforce(self) -> str:
        while True:
            #Generere de første 6 cifre i cpr nummeret
            cpr = self.dato.strftime('%d%m%y')
            cpr = [int(x) for x in cpr]

            #Tilføjer 4 random tal, til at være de sidste 4 cifre i cpr nummeret
            while len(cpr) != 10:
                cpr.append(random.randint(0, 9))

            #Formaterer cpr nummeret
            cpr_str = ''.join(map(str, cpr))
            #Tilføjer bindestreg mellem de første 6 cifre og de sidste 4 cifre
            formatted_cpr = f"{cpr_str[:6]}-{cpr_str[6:]}"

            print("Genereret CPR nummer:", formatted_cpr)
    
            #Validerer cpr nummeret
            v = validater(formatted_cpr)
            
            #Kontrol beregning
            v.kontrolberegning()
            #printer hvilket køn det er
            print(v.sex())

            #Hvis cpr nummeret er gyldigt, stopper while loopet
            if v.check():
                break

        return formatted_cpr
        
#generere et cpr nummer
print("Generer et cpr nummer")
generate = generate()
generate.bruceforce()

#CPR validater
print("\n")
print("CPR validater")
#Indtast et cpr nummer
cpr = ''
#Valider cpr nummeret
validater = validater(cpr)
#Kontrol beregning
validater.kontrolberegning()
#Printer kønnet
print(validater.sex())
#Tjekker om cpr nummeret er gyldigt
validater.check()