import textwrap  # Import library to help format text output

# Definition af en rute som en dictionary (kort over veje og afstande)
Rute = {
    "Start": [["A", 5]],
    "A": [["B", 60], ["E", 20]],
    "B": [["C", 50], ["F", 5]],
    "C": [["D", 40]],
    "E": [["F", 40], ["I", 20]],
    "F": [["G", 35], ["J", 40]],
    "G": [["H", 35], ["K", 15]],
    "H": [["K", 20]],
    "I": [["J", 20], ["L", 20]],
    "J": [["M", 40], ["N", 60]],
    "K": [["N", 10]],
    "L": [["M", 50]],
    "M": [["N", 20]],
    "N": [["Slut", 5]],
}

class Topologi:
    """
    Topologi-klassen bruges til at finde den korteste rute fra en start til en destination
    i en graf (netværk af punkter forbundet med vægte/afstande).
    """
    def __init__(self) -> None:
        # Liste til at gemme den/de korteste ruter
        self.shortest_paths = []
        # Variabel til at holde styr på den korteste distance, starter som uendelig
        self.shortest_distance = float('inf')
    
    def find_shortest_path(self, start, end, path=[], distance=0):
        """
        Finder den korteste vej ved hjælp af rekursion.
        start: Startpunktet i ruten
        end: Slutpunktet i ruten
        path: Den nuværende vej vi følger
        distance: Den samlede distance indtil nu
        """
        # Tilføj startpunktet til den nuværende rute
        path = path + [start]
        
        # Hvis vi når slutpunktet, tjek om det er den korteste rute
        if start == end:
            if distance < self.shortest_distance:
                self.shortest_distance = distance
                self.shortest_paths = [path]  # Opdater den korteste rute
            elif distance == self.shortest_distance:
                self.shortest_paths.append(path)  # Hvis der er flere ruter med samme distance
            return
        
        # Hvis startpunktet ikke findes i ruten (ingen vej videre), afslut funktionen
        if start not in Rute:
            return
        
        # Gå igennem alle naboer til det nuværende punkt
        for node in Rute[start]:
            if isinstance(node, list):  # Sikrer, at det er en liste med [næste punkt, afstand]
                next_node, dist = node  # Næste punkt og afstand til det punkt
                if next_node not in path:  # Undgå at besøge det samme punkt flere gange
                    self.find_shortest_path(next_node, end, path, distance + dist)
    
    def get_shortest_paths(self):
        """
        Starter søgningen efter den korteste rute fra "Start" til "Slut"
        Returnerer listen over korteste ruter og distancen.
        """
        self.find_shortest_path("Start", "Slut")
        return self.shortest_paths, self.shortest_distance

def print_pretty_paths(paths, distance):
    """
    Udskriver ruterne i et pænt format med ASCII-art.
    """
    print("\n" + "="*40)  # Print en separator-linje
    print(f" KORTESTE RUTE(R) FUNDEN ")
    print("="*40 + "\n")
    
    for i, path in enumerate(paths):
        ascii_path = " -> ".join(path)  # Formater ruten som en pil-forbundet sti
        wrapped_path = textwrap.fill(ascii_path, width=50)  # Wrap hvis det er for bredt
        print(f"Rute {i+1}:\n{wrapped_path}\n")
    
    print("-" * 40)  # Print en anden separator
    print(f"Samlet distance: {distance} Km")  # Udskriv den samlede afstand
    print("="*40 + "\n")

# Opret et objekt af Topologi-klassen
topologi = Topologi()
# Find de korteste ruter og distancer
paths, distance = topologi.get_shortest_paths()
# Udskriv resultatet på en pæn måde
print_pretty_paths(paths, distance)
