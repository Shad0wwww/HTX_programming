
class Resturant:
    def __init__(self, name: str):
        self.name = name
        pass

    def resturantMenu(self) -> None:
        print(f"Welcome to {self.name}")
        pass

class Retter(Resturant):
    def __init__(self, name: str, retter: dict[str, float]) -> None:
        super().__init__(name)
        self.retter: dict[str, float] = retter

    def getRetter(self) -> dict[str, float]:
        return self.retter

    def printMenu(self) -> None:
        print(f"--- Menu at {self.name} ---")
        for ret, pris in self.retter.items():
            print(f"{ret}: {pris} kr.")

class Guest(Resturant):
    def __init__(self, name: str, 
    reserveName: str, 
    guestNames: list[str]) -> None:
        self.orders: list[str] = []
        self.reserveName = reserveName
        self.guestNames: list[str] = guestNames
        super().__init__(name)

        pass

    def getGuestSize(self) -> int:
        return len(self.guestNames) + 1

    def orderDish(self, dish: str) -> None:
        self.orders.append(dish)

class Servant(Resturant):
    def __init__(self, name: str, servants: dict={}) -> None:
        super().__init__(name)
        self.servants: dict = servants
        pass

    def getServantName(self) -> dict:
        return self.servants
    
    def getServantWithSmallestTableSize(self) -> str:
        if not self.servants:
            return "No servants available"
        return min(self.servants, key=self.servants.get)
    
    
    def addServant(self, servantNames: str) -> None:
        if servantNames not in self.servants:
            self.servants[servantNames] = []  # Start med tom liste (ingen borde)
        else:
            print("Servant already exists")
        pass

    def updateServant(self, talbeID, servantNames: str) -> None:
        if servantNames in self.servants:
            self.servants[servantNames] = talbeID
        else:
            print("Servant does not exist")
        pass

    def distributeTables(self, total_tables: int) -> None:
        servant_names = list(self.servants.keys())
        num_servants = len(servant_names)
        # Nulstil alle borde
        for servant in servant_names:
            self.servants[servant] = []
        # Fordel borde jævnt
        for i in range(total_tables):
            servant = servant_names[i % num_servants]
            self.servants[servant].append(i + 1)


    def getServantsTasks(self) -> None:
        for servant, tables in self.servants.items():
            if tables:
                print(f"Servant {servant} is serving tables {', '.join(map(str, tables))}")
            else:
                print(f"Servant {servant} er ikke brug for lige nu")
        pass

class Table(Resturant):
    def __init__(self, name: str, 
    tableNumber: int=0, guesta : Guest = None, balance: float = 0.0, servant: Servant=None) -> None:
        super().__init__(name)
        self.guesta = guesta
        self.tableNumber: int = tableNumber
        self.balance: float = balance
        self.tableSize: int = 4
        self.servant = servant
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

    def addGuest(self, guestName: str) -> None:
        if len(self.guesta.guestNames) < self.tableSize - 1:
            self.guesta.guestNames.append(guestName)
        else:
            print("Table is full")
        pass

    def getBalance(self) -> float:
        return self.balance

    def getTableInfo(self) -> None:
        print(f"--- Table {self.tableNumber} Information ---")
        print(f'Table Size: {self.tableSize}')
        print(f'Reserved by: {self.guesta.reserveName}')
        print(f'Guests: {", ".join(self.guesta.guestNames)}')
        print(f'Orders: {", ".join(self.guesta.orders)}')
        print(f'Balance: {self.balance} kr.')
        self.servant.getServantsTasks()
        print('-------------------------------')
        
        pass

    def addOrder(self, menu: Retter, dish: str) -> None:
        if dish in menu.getRetter():
            self.guesta.orderDish(dish)
            self.balance += menu.getRetter()[dish]
            print(f"{dish} tilføjet til bestilling. Pris: {menu.getRetter()[dish]} kr.")
        else:
            print(f"{dish} findes ikke på menuen!")

    def addServantToTable(self, _obj: Servant, servantName: str) -> None:
        _obj.updateServant(self.tableNumber, servantName)
        pass


if __name__ == "__main__":


    #TJENER
    tjener = Servant("KFC")
    tjener.addServant("John")
    tjener.addServant("Doe")
    tjener.addServant("Jane")
    print(tjener.getServantName())
    
    #GÆSTER
    gæster = Guest("KFC", "Magnus", ["Lars", "Mikkel", "Nikolaj"])

    # MENU
    menu = Retter("KFC", {"Burger": 50.0, "Pommes": 20.0, "Cola": 15.0})
    menu.printMenu()

    #BORD
    bord = Table("KFC", 1, gæster)
    bord.createTable(1, gæster.getGuestSize())
    smallest_servant = tjener.getServantWithSmallestTableSize()
    bord.addServantToTable(tjener,smallest_servant)
    bord.servant = tjener
    tjener.distributeTables(bord.tableNumber)

    bord.addOrder(menu, "Burger")
    bord.addOrder(menu, "Cola")
    bord.addOrder(menu, "Pommes")

    bord.getTableInfo()
    

    pass