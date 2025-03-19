import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# ---------------------------
# Definition af netværket
# ---------------------------
# Her defineres et simpelt netværk som en dictionary, hvor hver nøgle er en node,
# og værdien er en dictionary med noder den forbinder til samt vægten (f.eks. afstand i km).
network = {
    "Start": {"A": 5},
    "A": {"B": 60, "E": 20},
    "B": {"A": 60, "C": 50, "F": 5},
    "C": {"B": 50, "D": 40},
    "D": {"C": 40, "H": 30},
    "E": {"A": 20, "F": 40, "I": 20},
    "F": {"B": 5, "E": 40, "G": 35, "J": 40},
    "G": {"F": 35, "H": 35, "K": 15},
    "H": {"D": 30, "G": 35, "K": 20},
    "I": {"E": 20, "J": 20},
    "J": {"F": 40, "I": 20, "M": 40, "N": 60},
    "K": {"G": 25, "H": 20, "N": 10},
    "L": {"I": 20, "M": 50},
    "M": {"J": 40, "N": 20},
    "N": {"K": 10, "M": 20, "Slut": 5},
    "Slut": {}
}

# ---------------------------
# Graph klassen
# ---------------------------
class Graph:
    def __init__(self, network):
        # Gemmer netværket (dictionary) i instansen
        self.network = network

    def find_all_paths(self, start, end, path=None, cost=0):
        """
        Rekursiv metode til at finde alle simple stier fra 'start' til 'end'.
        - path: den aktuelle sti (liste af noder)
        - cost: den akkumulerede omkostning (f.eks. km)
        Returnerer en liste af tuples, hvor hver tuple indeholder en sti og den samlede omkostning.
        """
        # Hvis ingen sti er givet, start med en tom liste
        if path is None:
            path = []
        # Tilføj den nuværende node til stien (kopiering for at undgå sideeffekter)
        path = path + [start]
        
        # Basis-tilfælde: hvis vi har nået slutnoden, returneres stien og costen
        if start == end:
            return [(path, cost)]
        
        paths = []
        # Gennemgå alle naboer til den aktuelle node
        for neighbor, weight in self.network.get(start, {}).items():
            # For at undgå cykler, spring noder over der allerede er besøgt
            if neighbor not in path:
                # Rekursivt kald til find_all_paths for naboen
                new_paths = self.find_all_paths(neighbor, end, path, cost + weight)
                for p, c in new_paths:
                    paths.append((p, c))
        return paths

# ---------------------------
# PathFinder klassen
# ---------------------------
class PathFinder:
    def __init__(self, graph):
        # Gemmer en Graph-instans
        self.graph = graph

    def get_all_paths(self, start, end):
        # Henter alle stier fra start til slut via Graph-klassens metode
        return self.graph.find_all_paths(start, end)

    def get_min_cost_paths(self, start, end):
        """
        Filtrerer de stier, der har den mindste samlede omkostning (f.eks. total km).
        Returnerer en tuple:
            ([liste over stier med min cost], min_cost)
        """
        all_paths = self.get_all_paths(start, end)
        if not all_paths:
            return [], None
        # Bestem minimum cost blandt alle fundne stier
        min_cost = min(cost for _, cost in all_paths)
        # Filtrer stierne, så kun de med denne minimum cost bevares
        min_cost_paths = [(p, c) for p, c in all_paths if c == min_cost]
        return min_cost_paths, min_cost

    def get_min_steps_path(self, paths):
        """
        Udvælger den sti, der har færrest antal noder (steps).
        Returnerer den sti, som har minimal længde.
        """
        if not paths:
            return None
        # Find det mindste antal noder (steps) blandt stierne
        min_steps = min(len(p) for p, _ in paths)
        for p, c in paths:
            if len(p) == min_steps:
                return (p, c)
        return None

# ---------------------------
# GraphVisualizer klassen
# ---------------------------
class GraphVisualizer:
    def __init__(self, network):
        # Gemmer netværket og opbygger en NetworkX DiGraph
        self.network = network
        self.G = nx.DiGraph()
        self._build_graph()

    def _build_graph(self):
        """
        Bygger NetworkX-grafen ud fra den givne network dictionary.
        Hver node og kant (med vægt) tilføjes til grafen.
        """
        for node, edges in self.network.items():
            for neighbor, weight in edges.items():
                self.G.add_edge(node, neighbor, weight=weight)

    def draw_graph(self, paths=[], best_path=None):
        """
        Visualiserer grafen med et circular layout.
        - Tegner hele grafen med noder og kantlabels.
        - Tegner hver sti (route) med en unik farve.
        - Den sti, der har færrest steps (best_path), fremhæves med sort, stiplet linje.
        - Der oprettes en dynamisk legend, så hver rute vises med et label.
        """
        # Brug circular layout for et overskueligt visuelt udtryk
        pos = nx.circular_layout(self.G)
        plt.figure(figsize=(12, 8))
        
        # Tegn alle noder og kanter i grafen
        nx.draw(self.G, pos, with_labels=True, node_color='lightblue', arrows=True,
                node_size=1500, font_size=10)
        # Hent kantvægtene og tegn dem som labels
        edge_labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=edge_labels)
        
        # Liste med farver til at skelne de forskellige stier
        colors = ["red", "blue", "green", "orange", "purple", "cyan", "magenta"]
        legend_elements = []  # Dummy handles til at bygge legenden dynamisk

        # Gennemløb alle stier og tegn dem med NetworkX
        for idx, (path, cost) in enumerate(paths):
            # Opret liste af kanter fra stien: (node1, node2), (node2, node3), osv.
            path_edges = list(zip(path, path[1:]))
            if best_path and path == best_path[0]:
                # Hvis denne sti er den udvalgte "bedste" (med færrest steps), brug sort, stiplet linje
                nx.draw_networkx_edges(self.G, pos, edgelist=path_edges,
                                       edge_color="black", width=4, style="dashed")
                label = "Min Steps"
                # Dummy handle for legenden for best route
                handle = Line2D([0], [0], color='black', lw=4, linestyle='dashed', label=label)
            else:
                # For andre stier bruges en unik farve (baseret på index)
                color = colors[idx % len(colors)]
                nx.draw_networkx_edges(self.G, pos, edgelist=path_edges,
                                       edge_color=color, width=3)
                label = f"Route {idx + 1}"
                # Dummy handle til legenden for denne rute
                handle = Line2D([0], [0], color=color, lw=3, label=label)
            legend_elements.append(handle)
        
        # Sæt en titel for grafen med den samlede omkostning (cost) for de viste stier
        plt.title("Visualisering af alle korteste stier (samlet Km = {})".format(
            paths[0][1] if paths else "N/A"))
        # Opret og vis legenden med de dynamiske handles
        plt.legend(handles=legend_elements)
        plt.show()

# ---------------------------
# Hovedprogram
# ---------------------------
if __name__ == '__main__':
    # Opret en instans af Graph med det definerede netværk
    graph = Graph(network)
    # Opret en instans af PathFinder for at søge efter stier
    finder = PathFinder(graph)
    
    # Find alle stier fra "Start" til "Slut" ved hjælp af DFS
    all_paths = finder.get_all_paths("Start", "Slut")
    
    # Filtrer stierne til kun at inkludere dem med den laveste samlede Km
    min_cost_paths, min_cost = finder.get_min_cost_paths("Start", "Slut")
    print("Alle korteste stier med samlet Km =", min_cost)
    for p, c in min_cost_paths:
        steps = len(p) - 1  # Beregn antal "steps" (antal overgange mellem noder)
        print("Sti:", p, "Km:", c, "Steps:", steps)
    
    # Udvælg den sti, der har færrest steps blandt de korteste stier
    best_path = finder.get_min_steps_path(min_cost_paths)
    if best_path:
        print("\nSti med færrest steps:", best_path[0],
              "Km:", best_path[1], "Steps:", len(best_path[0]) - 1)
    
    # Visualiser grafen med de fundne stier og fremhæv den bedste sti
    visualizer = GraphVisualizer(network)
    visualizer.draw_graph(paths=min_cost_paths, best_path=best_path)
