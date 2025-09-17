from enum import Enum
#
class Gender(Enum):
    GIRL = "girl"
    MALE = "mand"
#
class EyeColor(Enum):
    BLUE = "blue"
    GREEN = "green"
    BROWN = "brown"
    BLACK = "black"
    OTHER = "other"
#
#superclass
class Person:
    """
    Dette er superclass Person
    __init__ tager køn, fødselsdato, øjenfarve, højde og vægt som parametre
    ageInDecimals tager det nuværende år som parameter og returnerer alder i decimaler
    """
    def __init__(self, gender: Gender, birthDate: str, 
                 EyeColor: EyeColor, height: float, weight:float) -> None:
        
        self.birthDate = birthDate
        self.gender = gender
        self.EyeColor = EyeColor
        self.height = height
        self.weight = weight
        pass
    
    def ageInDecimals(self, currentYear: int) -> float:
        """
        currentYear: det år vi er i nu
        return: alder i decimaler
        """
        birthYear = int(self.birthDate.split("-")[0])
        age = currentYear - birthYear
        # Regner med et halvt år ekstra for at tage højde for fødselsdatoen

        return age + 0.5 
    
    def bmi(self) -> float:
        """
        return: BMI
        BMI = vægt / højde^2
        Vægt i kg og højde i meter
        """
        return self.weight / (self.height ** 2)
#  
class uddannelse:
    """
    Dette er subclass uddannelse
    __init__ tager køn, fødselsdato, øjenfarve, højde og vægt som parametre
    Arver fra Person
    """
    def __init__(self, uddannelse: str) -> None:
        self.uddannelse = uddannelse
        pass

    def get_uddannelse(self) -> str:
        return self.uddannelse
#Subclass    
class teacher(Person, uddannelse):
    """
    Dette er subclass Teacher
    __init__ tager køn, fødselsdato, øjenfarve, højde og vægt som parametre
    Arver fra Person
    """
    def __init__(
            self, gender: Gender, birthDate: str, 
            EyeColor: EyeColor, height: float, 
            weight:float, uddannelsee: str
            ) -> None:
        
        super().__init__(gender, birthDate, EyeColor, height, weight)
        uddannelse.__init__(self, uddannelsee)
        
        pass
#
class student(Person, uddannelse):
    """
    Dette er subclass Student
    __init__ tager køn, fødselsdato, øjenfarve, højde og vægt som parametre
    Arver fra Person
    """
    def __init__(self, gender, birthDate, 
                 EyeColor, height, weight, uddannelsee: str) -> None:
        
        super().__init__(gender, birthDate, EyeColor, height, weight)
        uddannelse.__init__(self, uddannelsee)
        pass
#
if __name__ == "__main__":
    #sUbclass instances
    magnus = student(Gender.MALE, "2005-10-20", EyeColor.BLUE, 1.80, 92, uddannelsee="student")
 
    Peter = teacher(Gender.MALE, "2003-03-30", EyeColor.BROWN, 1.75, 100, uddannelsee="teacher")

    print(f"Peter is a {Peter.get_uddannelse()} og er {Peter.ageInDecimals(2025)} years old with a BMI of {Peter.bmi():.2f}")

    print(f"Magnus is a {magnus.get_uddannelse()} og er {magnus.ageInDecimals(2025)} years old with a BMI of {magnus.bmi():.2f}")