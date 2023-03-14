a = ["|","|",""]
b = ["__","__","__"]
class Matrix:
    def __init__(self) -> None:
        pass
class Player():
    def __init__(self,name):
        self.name = name
        self.wins = 0

class Game:
    def __init__(self):
        name1 = input("PLAYER 1 NAME:")
        name2 = input("PLAYER 2 NAME:")
        self.player1 = Player(name1)
        self.player2 = Player(name2)
    def play_game(self):
        self.player1.input = input("")
for i in range(0,3):
    for j in range(0,3):
        if(i<2):
          print(b[j],end="")
        else:
            print("  ",end="")
        print(a[j],end="")
    print()