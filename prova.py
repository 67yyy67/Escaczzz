N = "Na1c2"
T = [a for a in N]
T = [a if T[0] == a else 0 if a == "a" or a == "1" else 1 if a == "b" or a == "2" else 2 if a == "c" or a == "3" else 3 if a == "d" or a == "4" else 4 if a == "e" or a == "5" else 5 if a == "f" or a == "6" else 6 if a == "g" or a == "7" else 7 if a == "h" or a == "8" else a for a in T]
print(T)
