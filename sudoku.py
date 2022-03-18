def negyzet(s, o):
    # pos_s = (s - 1) // 3 + 1
    # pos_o = (o - 1) // 3 + 1

    if s < 4:
        pos_s = 1
    elif s < 7:
        pos_s = 2
    else:
        pos_s = 3 
    if o < 4:
        pos_o = 1
    elif o < 7:
        pos_o = 2
    else:
        pos_o = 3
    return (pos_s - 1) * 3 + pos_o

def sorban_van(t, s, sz):
    return sz in t[s]

def oszlopban_van(t, o, sz):
    for sor in t:
        if sor[o] == sz:
            return True
    return False

def resztablaban_van(t, n, sz):
    for i,sor in enumerate(t):
        for j,szam in enumerate(sor):
            if negyzet(i, j) == n and szam == sz:
                return True
    return False


print("1. feladat")
tabla = []
lepesek = []
f = input("Adja meg a bemeneti fájl nevét: ")
s = int(input("Adja meg egy sor számát: "))
o = int(input("Adja meg egy oszlop számát: "))
with open(f, "r") as fajl:
    for i,sor in enumerate(fajl):
        row = []
        for szam in sor.split():
            row.append(int(szam))
        if i < 9:
            tabla.append(row)
        else:
            lepesek.append(row)

print("3. feladat")
print(f"Az adott helyen szereplő szám: {tabla[s - 1][o - 1]}")
print(f"A hely a(z) {negyzet(s,o)} résztáblázathoz tartozik.")

print("4. feladat")
ures = 0
for sor in tabla:
    for szam in sor:
        if szam == 0:
            ures += 1
print(f"Az üres helyek aránya {ures / 81:.1%}")

print("5. feladat")
for sor in lepesek:
    print(f"A kiválasztott sor: {sor[1]} oszlop: {sor[2]} a szám: {sor[0]}")
    if tabla[sor[1] - 1 ][sor[2] - 1] != 0:
        print("A helyet már kitöltötték.")
    elif sorban_van(tabla, sor[1] - 1, sor[0]):
        print("Az adott sorban már szerepel a szám.")
    elif oszlopban_van(tabla, sor[2] - 1, sor[0]):
        print("Az adott oszlopban már szerepel a szám.")
    elif resztablaban_van(tabla, negyzet(sor[1], sor[2]), sor[0]):
        print("A lépés megtehető.")