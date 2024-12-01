from datetime import date
from numpy import random

class validater:
    kontrol :int = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]
    cpr: int = 0
    sum: int = 0

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
        if self.sum % 11 == 0:
            print("CPR nummeret er gyldigt \n")
            return True
        else:
            print("CPR nummeret er ugyldigt \n")
            return False

class generate:
    dato = date.today()
    
    def bruceforce(self) -> str:
        while True:
            cpr = self.dato.strftime('%d%m%y')
            cpr = [int(x) for x in cpr]

            #Tilføjer 4 random tal, til at være de sidste 4 cifre i cpr nummeret
            while len(cpr) != 10:
                cpr.append(random.randint(0, 9))

            cpr_str = ''.join(map(str, cpr))
            formatted_cpr = f"{cpr_str[:6]}-{cpr_str[6:]}"

            print("Genereret CPR nummer:", formatted_cpr)
    
            #Validerer cpr nummeret
            v = validater(formatted_cpr)
            
            v.kontrolberegning()
            print(v.sex())

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
# cpr = ''

# validater = validater(cpr)
# validater.kontrolberegning()
# print(validater.sex())
# validater.check()