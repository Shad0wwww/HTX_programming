class MediaItem:
    """
    Basisklasse for medieprodukter som bøger, film og lydbøger.
    Indeholder fælles attributter som titel, forfatter/instruktør og udgivelsesår.
    """
    def __init__(self, title:str, author_director: str, year:str) -> None:
        self.title: str = title
        self.author_director: str = author_director
        self.year:str = year
        pass

    def display_info(self):
        print(f"Title: {self.title} \nAf: {self.author_director} \nUdgivelsesår: {self.year}")
#______________________________________________________________________________________________________________
class Book(MediaItem):
    """
    Klasse for bøger, der nedarver fra MediaItem-klassen.
    Indeholder yderligere attributter for antal sider og ISBN.
    """

    def __init__(self, title: str, 
                 author_director:str, 
                 year:str, 
                 pages:int, 
                 isbn:str):
        super().__init__(title, author_director, year)

        
        self.pages: int = pages
        self.isbn: int = isbn

    
    def display_info(self):
        return super().display_info(), print(f"Sider: {self.pages} \nISBN: {self.isbn}")
#______________________________________________________________________________________________________________
class Movie(MediaItem):
    """
    Klasse for film, der nedarver fra MediaItem-klassen.
    Indeholder yderligere attributter for spilletid og genre.
    """

    def __init__(self, 
                 title: str, 
                 author_director:str, 
                 year:str, 
                 runtime_minutes:int, 
                 genre:str):
        super().__init__(title, author_director, year)

        self.runtime_minutes: int = runtime_minutes
        self.genre: str = genre

    def display_info(self):
        return super().display_info(), print(f"Spilletid: {self.runtime_minutes} minutter \nGenre: {self.genre}")
#_______________________________________________________________________________________________________________
class AudioBook(Book):
    """
    Klasse for lydbøger, der nedarver fra Book-klassen.
    Indeholder yderligere attributter for varighed og fortæller.
    """

    def __init__(self, 
                 title: str, 
                 author_director:str, 
                 year:str, 
                 pages:int, 
                 isbn:str, 
                 duration_minutes:int, 
                 narrator:str):
        super().__init__(title, author_director, year, pages, isbn)

        self.duration_minutes: int = duration_minutes
        self.narrator: str = narrator

    def display_info(self):
        return super().display_info(), print(f"Varighed: {self.duration_minutes} minutter \nFortæller: {self.narrator}")
#______________________________________________________________________________________________________________
if __name__ == "__main__":

    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1925", 180, "9780743273565")
    book2 = Book("1984", "George Orwell", "1949", 328, "9780451524935")

    movie1 = Movie("Inception", "Christopher Nolan", "2010", 148, "Science Fiction")
    movie2 = Movie("The Godfather", "Francis Ford Coppola", "1972", 175, "Crime")

    audiobook1 = AudioBook("Becoming", "Michelle Obama", "2018", 448, "9781524763138", 1140, "Michelle Obama")
    audiobook2 = AudioBook("The Subtle Art of Not Giving a F*ck", "Mark Manson", "2016", 224, "9780062457714", 300, "Roger Wayne")

    media_catalog: list[MediaItem] = [book1, book2, movie1, movie2, audiobook1, audiobook2]

    for item in media_catalog:
        print(30 * "-")
        print("Classen: ", item.__class__.__name__)
        print("")
        item.display_info()