import pandas as pd
import openpyxl 

class ExcelReader:
    file_path = None
    sheet = None
    excel = None

    def __init__(self, file_path, sheet) -> None:
        self.file_path = file_path
        self.sheet = sheet
        self.excel = pd.read_excel(self.file_path, sheet_name = self.sheet)

    def read(self):
        print(f"Reading file {self.file_path}")
        
    
 
    
class Cabltree:
    lenght: int = None
    CableTag: str = None
    F9: str = None
    F18: str = None

    def __init__(self, lenght, CableTag, F9, F18) -> None:
        self.lenght = lenght
        self.CableTag = CableTag
        self.F9 = F9
        self.F18 = F18

 
def main():
    excel_reader = ExcelReader("public/Cabletree/cabletree.xlsx", "Query")
    excel_reader.read()


if __name__ == "__main__":
    main()