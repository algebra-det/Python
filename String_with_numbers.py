
def total(unit):
    a = 1; b = 2; c = 3; d = 4; e = 5; f = 6; g = 7; h = 8; i = 9; j = 10; k = 11; l = 12; m = 13
    n = 14; o = 15; p = 16; q = 17; r = 18; s = 19; ti = 20; u = 21; v = 22; w = 23; x = 24; y = 25; z = 26
    t = 0
    for car in unit:
        if car == "A":
            t+=a
        elif car == "B":
            t+=b
        elif car == "C":
            t+=c
        elif car == "D":
            t+=d
        elif car == "E":
            t+=e
        elif car == "F":
            t+=f
        elif car == "G":
            t+=g
        elif car == "H":
            t+=h
        elif car == "I":
            t+=i
        elif car == "J":
            t+=j
        elif car == "K":
            t+=k
        elif car == "L":
            t+=l
        elif car == "M":
            t+=m
        elif car == "N":
            t+=n
        elif car == "O":
            t+=o
        elif car == "P":
            t+=p
        elif car == "Q":
            t+=q
        elif car == "R":
            t+=r
        elif car == "S":
            t+=s
        elif car == "T":
            t+=ti
        elif car == "U":
            t+=u
        elif car == "V":
            t+=v
        elif car == "W":
            t+=w
        elif car == "X":
            t+=x
        elif car == "Y":
            t+=y
        elif car == "Z":
            t+=z
    return t

def main():
    unit = "AKASH"
    print(total(unit))

if __name__=="__main__":
    main()





