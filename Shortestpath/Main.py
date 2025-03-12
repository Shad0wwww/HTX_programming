Rute = {
    "Start": ["A", 5],
    "A": [["B", 60], ["E", 20]],
    "B": [["C", 50], ["F", 5]],
    "C": ["D", 40],
    "E": [["F", 40], ["I", 20]],
    "F": [["G", 35], ["J", 40]],
    "G": [["H", 35], ["K", 15]],
    "H": ["K", 20],
    "I": [["J", 20], ["L", 20]],
    "J": [["M", 40], ["N", 60]],
    "K": ["N", 10],
    "L": ["M", 50],
    "M": ["N", 20],
    "N": "Slut",
}

class Dijkstras:
    def __init__(self)-> None:
        print(self)
        

shortest_path = []
for k, v in Rute.items():
    print(k)
    print(v)


       
