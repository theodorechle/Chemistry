from tab_avancement import *
from kandinsky import *
from ion import *


def dessiner_tableau(deplace, etats, Tableaux, Texte, lesx, valeurs):
    """
    The dessiner_tableau function draws the tableau of the reaction.
    It takes as input:
    - deplace, which is a list containing two integers that represent how many pixels to move horizontally and vertically respectively;
    - etats, which is a list containing four strings representing what each reactant and product are in their state before and after
    
    :param deplace: Move the tableau to the right and down
    :param etats: Display the reactants and products
    :param Tableaux: Display the tableaux
    :param Texte: Display the name of each reactant and product
    :param lesx: Determine the number of reactants
    :param valeurs: Give the values of the coefficients and the reactants
    :return: Nothing
    :doc-author: Trelent
    """
    deph, depv, valeurh, valeurv = deplace[0], deplace[1], valeurs[0], valeurs[1]
    couleur1 = (200, 200, 250)
    couleur2 = (255, 255, 255)

    if valeurv+depv <= valeurv:
        fill_rect(0, 0, 320, 55, couleur1)  # horizontal

    if valeurh+deph <= valeurh*2:
        fill_rect(0, 0, valeurh*2+deph, valeurv*4-depv, couleur1)  # vertical

    for g in range(4):
        couleur = couleur2
        for nb in range(2):
            draw_string(etats[g][nb], 10+100*nb+deph, 20+55*g-depv, (0, 0, 0), couleur1)  # +55
            for h, i in enumerate(Tableaux[g][nb]):
                a = ""
                place = 1
                coeffin = ""
                if g == 0:
                    couleur = couleur1
                    if Tableaux[0][nb][h][0] > 1:
                        place = 20
                        draw_string(str(Tableaux[0][nb][h][0]), (valeurh*2+1)+valeurh*(h+len(tableaux[g][nb-1])*nb)+deph, 20+55*g-depv, (255, 0, 0), couleur)
                    a += str(Tableaux[0][nb][h][1])
                else:
                    a = str(i)
                signe = "-"
                if nb == 1:
                    signe = "+"
                if Tableaux[0][nb][h][0] > 1:
                    coeffin = "*"+str(Tableaux[0][nb][h][0])
                sup = 20
                nba = 0
                if g > 1:
                    sup = 35
                    if g == 3:
                        nba = 1

                    draw_string((str(Tableaux[1][nb][h])+signe+str(lesx[nba])+coeffin), (valeurh*2+place)+valeurh*(h+len(Tableaux[g][nb-1])*nb)+deph, 5+55*g-depv, (0, 0, 0), couleur)
                draw_string(a, (valeurh*2+place)+valeurh*(h+len(Tableaux[g][nb-1])*nb)+deph, sup+55*g-depv, (0, 0, 0), couleur)  # +85
            if nb == 0:
                sup = 19
                place = 85
                draw_string("→", (valeurh*2+place)+valeurh*(h+len(Tableaux[g][nb-1])*nb)+deph, sup+55*g-depv, (0, 0, 0), couleur)
    draw_string("Le(s) reactif(s) limitant(s) est/sont:", deph, 5+valeurv*4-depv)

    for y, z in enumerate(Texte):
        draw_string(z, 100*y+deph, 35+valeurv*4-depv)

    for i in range(len(tabr)+len(tabp)+1):  # horizontal
        for j in range(valeurv*4-depv+1):
            set_pixel(i*valeurh, j, (0, 0, 0))
    for j in range(valeurv*4+1):
        set_pixel(i*valeurh+1, j, (0, 0, 0))

    for i in range(5-depv//valeurv):  # horizontal
        for j in range(valeurh*3+1):
            set_pixel(j, i*valeurv, (0, 0, 0))

    for j in range(valeurh*3+2):
        set_pixel(j, valeurv*i+1, (0, 0, 0))

    return deplace


def tracer():
    """
    The tracer function is the main function of the program. It is responsible for drawing all elements on screen, and
    for moving them when necessary. The tracer function also checks if a transition can be made from one state to another.
    
    :return: The tableaux
    :doc-author: Trelent
    """
    global tableaux
    tabinterrea, tabinterpro, tabfinrea, tabfinpro, texte, x, xmax = creer_tableau()
    tableaux = [[tabelementsr, tabelementsp], [tabr, tabp], [tabinterrea, tabinterpro], [tabfinrea, tabfinpro]]
    xfin = "X="+str(x)
    xmaxfin = "Xmax="+str(xmax)
    etats = [["etat", "avanc."], ["Init.", "X=0"], ["Inter.", xfin], ["Final", xmaxfin]]

    nbho = 106
    nbve = 55
    deplacementho = 0
    deplacementve = 0
    dessiner_tableau((0, 0), etats, tableaux, texte, (x, xmax), (nbho, nbve))
    while not False:  # Qu'est ce que t'as pas compris ?
        if keydown(KEY_RIGHT) and nbho*(len(tabr)+len(tabp)+len(etats[0])-3)+deplacementho >= nbho:
            fill_rect(0, 0, 320, 222, (255, 255, 255))
            deplacementho, deplacementve = dessiner_tableau((deplacementho-nbho, deplacementve), etats, tableaux, texte, (x, xmax), (nbho, nbve))
        elif keydown(KEY_LEFT) and deplacementho-nbho <= -nbho*2:
            fill_rect(0, 0, 320, 222, (255, 255, 255))
            deplacementho, deplacementve = dessiner_tableau((deplacementho+nbho, deplacementve), etats, tableaux, texte, (x, xmax), (nbho, nbve))
        if keydown(KEY_UP) and deplacementve >= nbve:
            fill_rect(0, 0, 320, 222, (255, 255, 255))
            deplacementho, deplacementve = dessiner_tableau((deplacementho, deplacementve-nbve), etats, tableaux, texte, (x, xmax), (nbho, nbve))
        elif keydown(KEY_DOWN) and deplacementve <= 0:
            fill_rect(0, 0, 320, 222, (255, 255, 255))
            deplacementho, deplacementve = dessiner_tableau((deplacementho, deplacementve+nbve), etats, tableaux, texte, (x, xmax), (nbho, nbve))


tracer()
