Tablero = [["0", "0", "0", "0", "0", "0", "0", "0"],
           ["0", "0", "0", "0", "0", "0", "0", "0"],
           ["0", "0", "0", "0", "0", "0", "0", "0"],
           ["0", "0", "0", "0", "0", "0", "0", "0"],
           ["0", "0", "0", "0", "0", "0", "0", "0"],
           ["0", "0", "0", "0", "0", "0", "0", "0"],
           ["0", "0", "0", "0", "0", "0", "0", "0"],
           ["0", "0", "0", "0", "0", "0", "0", "0"]
           ]

def mostrar(Tablero):
    print("  a,  b,  c,  d,  e,  f,  g,  h")
    i = 1
    for a in Tablero:
        print(f"{i}{a}")
        i = i + 1
def clear():
    return [["0", "0", "0", "0", "0", "0", "0", "0"],
           ["0", "0", "0", "0", "0", "0", "0", "0"],
           ["0", "0", "0", "0", "0", "0", "0", "0"],
           ["0", "0", "0", "0", "0", "0", "0", "0"],
           ["0", "0", "0", "0", "0", "0", "0", "0"],
           ["0", "0", "0", "0", "0", "0", "0", "0"],
           ["0", "0", "0", "0", "0", "0", "0", "0"],
           ["0", "0", "0", "0", "0", "0", "0", "0"]
           ]


Pieceslist = []


class Pawn():
    def __init__(self, x = [0, 0], team = 0):
        self.x = x
        Tablero[self.x[0]][self.x[1]] = "p"
        self.team = team
        Pieceslist.append(self)
        if self.team == 1:
            self.stq = 6
        elif self.team == 0:
            self.stq = 1
    def move(self, z = [0, 0]):
        if ((((z[0] == self.x[0] + 1) and (z[1] == self.x[1])) or (((z[1] == self.x[1]) and (z[0] == self.x[0] + 2)) and (self.x[0] == self.stq))) and self.team == 0) or ((((z[0] == self.x[0] - 1) and (z[1] == self.x[1])) or (((z[1] == self.x[1]) and (z[0] == self.x[0] - 2)) and (self.x[0] == self.stq))) and self.team == 1):
            nomou = False
            for a in Pieceslist:
                if a.x == z:
                    nomou = True
            if nomou == True:
                print("invalid")
            else:
                Tablero[self.x[0]][self.x[1]] = "0"
                self.x = z
                Tablero[z[0]][z[1]] = "p"
        elif (((z[0] == self.x[0] + 1) and (z[1] == self.x[1] + 1)) or ((z[1] == self.x[1] - 1) and (z[0] == self.x[0] + 1)) and self.team == 0) or (((z[0] == self.x[0] + 1) and (z[1] == self.x[1] - 1)) or ((z[1] == self.x[1] - 1) and (z[0] == self.x[0] - 1)) and self.team == 1):
            nomou = True
            for a in Pieceslist:
                if a.x == z and a.team == self.team:
                    nomou = False
            if nomou == True:
                print("invalid")
            else:
                Tablero[self.x[0]][self.x[1]] = "0"
                self.x = z
                Tablero[z[0]][z[1]] = "p"
        else:
            print("invalid")

class Knight():
    def __init__(self, x = [0, 0], team = 0):
        self.x = x
        Tablero[self.x[0]][self.x[1]] = "N"
        self.team = team
        Pieceslist.append(self)
    def move(self, z = [0, 0]):
        if (((z[0] == self.x[0] + 1) or (z[0] == self.x[0] - 1)) and ((z[1] == self.x[1] + 2) or (z[1] == self.x[1] - 2))) or (((z[1] == self.x[1] + 2) or (z[1] == self.x[1] - 2)) and ((z[1] == self.x[1] + 1) or (z[1] == self.x[1] - 1))):
            nomou = False
            for a in Pieceslist:
                if a.x == z and a.team == self.team:
                    nomou = True
            if nomou == True:
                print("invalid")
            else:
                Tablero[self.x[0]][self.x[1]] = "0"
                self.x = z
                Tablero[z[0]][z[1]] = "N"
        else:
            print("invalid")

Tablero = clear()
p1 = Pawn(x = [1, 1], team = 0)
p2 = Pawn(x = [3, 2], team = 1)
mostrar(Tablero)
p2.move(z = [2,2])
mostrar(Tablero)
p1.move(z = [2,2])
mostrar(Tablero)