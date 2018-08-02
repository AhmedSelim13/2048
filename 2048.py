import random

Tablo = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
TestTablo = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
puan = 0

def yazdır():
    print(puan)
    for i in range(4):
        for c in range(4):
            print(str(Tablo[i][c]) ,end = "")
            if c == 3:
                break
            print("|", end = "")
        print("\n", end = "")
            

def rastgele():
    y = random.randrange(4)
    z = random.randrange(4)
    x = Tablo[y][z]
    if x != 0:
        y, z = rastgele()
    return y, z


def yerlestir():
    konum = rastgele()
    Tablo[konum[0]][konum[1]] = 2 * (random.randrange(2) + 1)


def hareket(move):
    global TestTablo
    global Tablo
    global puan
    for z in range(4):
        TestTablo[z] = Tablo[z].copy()
    if move == "w":
        for i in range(4):
            sonhareket = 0
            t = 0
            move = [TestTablo[0][i], TestTablo[1][i], TestTablo[2][i], TestTablo[3][i]]
            for j in range(4):
                eleman = move[j]
                if eleman == 0:
                    continue
                elif j == 0:
                    sonhareket = eleman
                    t = t + 1
                    continue
                elif sonhareket == eleman:
                    move[j] = 0
                    move[t - 1] = eleman * 2
                    sonhareket = eleman * 2
                    puan = puan + eleman
                    continue
                move[j] = 0
                move[t] = eleman
                sonhareket = eleman
                t = t + 1
            for c in range(4):
                TestTablo[c][i] = move[c]
    elif move == "a":
        for i in range(4):
            sonhareket = 0
            t = 0
            move = [TestTablo[i][0], TestTablo[i][1], TestTablo[i][2], TestTablo[i][3]]
            for j in range(4):
                eleman = move[j]
                if eleman == 0:
                    continue
                elif j == 0:
                    sonhareket = eleman
                    t = t + 1
                    continue
                elif sonhareket == eleman:
                    move[j] = 0
                    move[t - 1] = eleman * 2
                    sonhareket = eleman * 2
                    puan = puan + eleman
                    continue
                move[j] = 0
                move[t] = eleman
                sonhareket = eleman
                t = t + 1
            for c in range(4):
                TestTablo[i][c] = move[c]
    elif move == "s":
        for i in range(4):
            sonhareket = 0
            t = 0
            move = [TestTablo[3][i], TestTablo[2][i], TestTablo[1][i], TestTablo[0][i]]
            for j in range(4):
                eleman = move[j]
                if eleman == 0:
                    continue
                elif j == 0:
                    sonhareket = eleman
                    t = t + 1
                    continue
                elif sonhareket == eleman:
                    move[j] = 0
                    move[t - 1] = eleman * 2
                    sonhareket = eleman * 2
                    puan = puan + eleman
                    continue
                move[j] = 0
                move[t] = eleman
                sonhareket = eleman
                t = t + 1
            for c in range(1, 5):
                TestTablo[c-1][i] = move[-c]
    elif move == "d":
        for i in range(4):
            sonhareket = 0
            t = 0
            move = [TestTablo[i][3], TestTablo[i][2], TestTablo[i][1], TestTablo[i][0]]
            for j in range(4):
                eleman = move[j]
                if eleman == 0:
                    continue
                elif j == 0:
                    sonhareket = eleman
                    t = t + 1
                    continue
                elif sonhareket == eleman:
                    move[j] = 0
                    move[t - 1] = eleman * 2
                    sonhareket = eleman * 2
                    puan = puan + eleman
                    continue
                move[j] = 0
                move[t] = eleman
                sonhareket = eleman
                t = t + 1
            for c in range(1, 5):
                TestTablo[i][c-1] = move[-c]
                              
    if TestTablo == Tablo:
        hareket(input("Geçersiz hareket girdiniz lütfen geçerli bir hareket giriniz: "))
    else:
        Tablo = TestTablo.copy()
            

yerlestir()
yerlestir()

while True:
    yazdır()
    hareket(input("Yapmak istediğiniz hareketi giriniz: "))
    yerlestir()
