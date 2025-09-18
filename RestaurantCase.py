


class Resturant:
    def __init__(self, name: str):
        self.name = name
        pass

class Guest(Resturant):
    def __init__(self, name: str, reserveName: str, guestNames: list[str]) -> None:
        self.reserveName = reserveName
        self.guestNames: list[str] = guestNames
        super().__init__(name)

        pass

    def getGuestSize(self) -> int:
        return len(self.guestNames) + 1

class Table(Resturant):
    def __init__(self, name: str, tableNumber: int=0, guesta : Guest = None) -> None:
        super().__init__(name)
        self.guesta = guesta
        self.tableNumber: int = tableNumber
        self.tableSize: int = 4
        self.tableInformation : dict = {}
        pass

    def createTable(self, tableNumber: int, tableSize: int) -> None:
        self.tableNumber = tableNumber
        self.tableSize = tableSize
        self.tableInformation = {
            "tableNumber": self.tableNumber,
            "tableSize": self.tableSize,
            self.guesta.reserveName: self.guesta.guestNames
        }
        pass

    

    def getTableInfo(self) -> None:
        print(self.tableInformation)
        print(f'Table number: {self.tableNumber}, Table size: {self.tableSize} guests: {self.guesta.guestNames}, reserved by: {self.guesta.reserveName}')
        



if __name__ == "__main__":
    
    gæster = Guest("KFC", "Magnus", ["Lars", "Mikkel", "Nikolaj"])

    bord = Table("KFC", 1, gæster)
    bord.createTable(1, gæster.getGuestSize())

    bord.getTableInfo()

    pass