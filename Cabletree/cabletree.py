import pandas as pd
import openpyxl 
from ete3 import Tree, TreeStyle

class ExcelReader:
    file_path = None
    sheet = None
    excel = None

    map = {}

    def __init__(self, file_path, sheet) -> None:
        self.file_path = file_path
        self.sheet = sheet
        self.excel = pd.read_excel(self.file_path, sheet_name=self.sheet, header=None)
    
    def translateToClass(self):
        #iterrows returnere rows som en tuple, hvor index er index og row er en pandas series
        for index, row in self.excel.iterrows():
            cable_tag = row[1] 
            length = row[6]
            f9 = row[8]   
            f18 = row[17]

            if cable_tag == 'Cable tag' and length == 'Length' and f9 == 'Component' and f18 == 'Component':
                continue
            
            if cable_tag == 'F2' or length == 'F7' or f9 == 'F9' or f18 == 'F18':
                continue

            self.map[index] = Cabletree(length, cable_tag, f9, f18)
    
class Cabletree:
    length: int = None
    CableTag: str = None
    F9: str = None
    F18: str = None

    def __init__(self, length, CableTag, F9, F18) -> None:
        self.length = length
        self.CableTag = CableTag
        self.F9 = F9
        self.F18 = F18

def drawCabletree(reader: ExcelReader):

    t = Tree(name="XD01")

    for index, cabltree_obj in reader.map.items():
        
        component1 = cabltree_obj.F9.replace('BGA10 EA363-', '').replace("BGA10 FC363-", "").strip()
        component2 = cabltree_obj.F18.replace('BGA10 EA363-', '').replace("BGA10 FC363-", "").strip()
    

        if component1 > component2:
            component1, component2 = component2, component1

        component1_node = t.search_nodes(name=component1)
        if not component1_node:
            component1_node = t.add_child(name=component1)
        else:
            component1_node = component1_node[0]
        
        
        if not component1_node.search_nodes(name=component2):
            component1_node.add_child(name=component2)


    print(t.get_ascii(show_internal=True))

def debug(reader: ExcelReader):
    for index, cabltree_obj in reader.map.items():
        print(f"Index: {index}")
        print(f"Length: {cabltree_obj.length}")
        print(f"Cable Tag: {cabltree_obj.CableTag}")
        print(f"F9: {cabltree_obj.F9}")
        print(f"F18: {cabltree_obj.F18}")

  
def main():
    reader = ExcelReader("public/Cabletree/cabletree.xlsx", "Query")
    reader.translateToClass()
    drawCabletree(reader)
    


if __name__ == "__main__":
    main()