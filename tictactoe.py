a = ["|","|",""]
b = ["__","__","__"]
arr = [['#' for i in range(3)] for j in range(3)]
class Matrix:
    def __init__(self) -> None:
        pass
class Player():
    def __init__(self,name):
        self.name = name
        self.input = None
        self.wins = 0

class Game:
    def __init__(self):
        name1 = input("PLAYER 1 NAME:")
        name2 = input("PLAYER 2 NAME:")
        self.player1 = Player(name1)
        self.player2 = Player(name2)
    def play_game(self):
        x=0
        response = None
        response=input("q to quit.Any other key to continue")
        while(response!='q'):
          while x<9:
            self.player1.input = input("")
            arr[int(self.player1.input[0])-1][int(self.player1.input[2])-1]='X'
            printf(arr)
            x=x+1
            if(win(arr,'X')or x>8):
                break
            self.player2.input = input("")
            arr[int(self.player2.input[0])-1][int(self.player2.input[2])-1]='O'
            printf(arr)
            if(win(arr,'O')):
                break
            x=x+1
          print(x)
          if(not win(arr,'X')and x==9):
              print("It's a Draw")
          elif(win(arr,'X')):
              self.player1.wins += 1
              print("{} won the match".format(self.player1.name))
          else:
              self.player2.wins += 1
              print("{} won the match".format(self.player2.name))
        if(self.player1.wins>self.player2.wins):
            print("Congratulations!!{} won the game".format(self.player1.name))
        elif(self.player1.wins<self.player2.wins):
            print("Congratulations!!{} won the game".format(self.player2.name))
        elif(self.player1.wins==self.player2.wins):
            print("It's a Draw")
def printf(a):
    for i in range(0,3):
       for j in range(0,3):
          print(a[i][j],end=" ")
       print()
def win(arr,x):
    n_row = None
    n_col = None
    o_row = None
    o_col = None
    diff_row=None
    diff_col=None
    for i in range(3):
        for j in range(3):
            if(arr[i][j]==x):
                o_row = n_row
                o_col = n_col
                if(diff_row!=None):
                    if(diff_row==i-o_row and diff_col==j-o_col):
                        return True
                if(o_row!=None):
                    diff_row = i - o_row
                    diff_col = j-o_col
                n_row = i
                n_col = j
    return False

game = Game()
game.play_game()
