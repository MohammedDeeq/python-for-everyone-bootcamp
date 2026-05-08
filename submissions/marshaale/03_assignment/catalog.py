from dataclasses import dataclass

@dataclass
class Game:
    name:str
    year:str
    platform:str # pc, playstation, xbox, nintendo, mobile

    def __str__(self):
        return f"name: {self.name}, year: {self.year}, platform: {self.platform}"

class Catalog:
    def __init__(self):
        self.items = []
    
    def add(self,catalog):
        self.items.append(catalog)

    def list_all(self):
        for item in self.items:
            print(item)    


def load_catalog(path, catalog):
    try:
        with open(path,'r',encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                name, year, platform = line.strip().split('|')
                game = Game(name, year, platform)
                catalog.add(game)
    except FileNotFoundError:
        print(f"File {path} does not exists")

def save_catalog(path, catalog):
    pass

def main():
    file_path = "catalog.txt"
    game_catalog = Catalog()
    load_catalog(file_path, game_catalog)
    game_catalog.list_all()




if __name__ == "__main__":
    main()