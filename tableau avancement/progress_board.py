tabelementsr = [(1, "Mg"), (2, "H+")]
tabelementsp = [(1, "Mg2+"), (1, "H2")]
tabr = [0.005, 0.04]
tabp = [0, 0]
x = 1
unite = "mol"


def creer_tableau():
    global tabelementsr, tabelementsp, tabr, tabp, x
    tabtest = []
    tabinterrea = [0]*len(tabelementsr)
    tabinterpro = [0]*len(tabelementsp)
    tabfinrea = [0]*len(tabelementsr)
    tabfinpro = [0]*len(tabelementsp)
    realimit = []
    rea = ""
    pro = ""
    for a, b in tabelementsr:
        rea += str(a)+str(b)+" "
    for a, b in tabelementsp:
        pro += str(a)+str(b)+" "
    print(rea, "->", pro)
    print(tabr, "->", tabp)
    ecrita = ""
    for i, valeur in enumerate(tabr):
        coef = tabelementsr[i][0]
        a = valeur-coef*x
        if a >= 0:
            tabinterrea[i] = a
        else:
            tabinterrea[i] = "impossible"
        ecrita += str(tabinterrea[i])
        if i < len(tabr)-1:
            ecrita += "+"
    ecritb = ""
    for i, valeur in enumerate(tabp):
        coef = tabelementsp[i][0]
        a = valeur+coef*x
        if a >= 0:
            tabinterpro[i] = a
        else:
            tabinterpro[i] = "impossible"
        ecritb += str(tabinterpro[i])
        if i < len(tabp)-1:
            ecritb += "+"
    print("x=", x)
    print(ecrita, "->", ecritb)
    for i, valeur in enumerate(tabr):
        a = True
        coef = tabelementsr[i][0]
        xtest = valeur/coef
        for i, valeur in enumerate(tabr):
            if a:
                if valeur-xtest*tabelementsr[i][0] < 0:
                    a = False
        if a:
            tabtest.append(xtest)
    xmax = 0
    for i in tabtest:
        if i > xmax:
            xmax = i
    print("xmax : ", xmax)
    b = ""
    for i, valeur in enumerate(tabr):
        coef = tabelementsr[i][0]
        tabfinrea[i] = valeur-xmax*coef
        if tabfinrea[i] == 0:
            realimit.append(tabelementsr[i][1])
        b += str(tabfinrea[i])
        if i < len(tabr)-1:
            b += "+"
    ecritlimit = ""
    for i in realimit:
        ecritlimit += str(i)+" "
    print("limit : ", ecritlimit)
    a = ""
    for i, valeur in enumerate(tabp):
        coef = tabelementsp[i][0]
        tabfinpro[i] = valeur+xmax*coef
        a += str(tabfinpro[i])
        if i < len(tabp)-1:
            a += "+"
    print(b, "->", a)
    return tabinterrea, tabinterpro, tabfinrea, tabfinpro, realimit, x, xmax
