import pyxel, random
# taille de la fenetre 128x128 pixels
# ne pas modifier
pyxel.init(128, 128, title="Nuit du c0de")

# position initiale du plateau
plateau_x = 60
plateau_y = 110

# position initiale de la balle
balle_x = 60
balle_y = 90

# vitesse de la balle
xballe = 1
yballe = 1

# coordonnes des blocs
bx = 30
bx1 = 40
bx2 = 50
bx3 = 60
bx4 = 70
bx5 = 80
bx6 = 90
by = 5
by1 = 15
by2 = 25

blocs = [ [[bx, by], [bx1, by], [bx2, by], [bx3, by], [bx4, by], [bx5, by], [bx6, by], [bx, by1], [bx1, by1], [[bx2, by1], [bx3, by1], [bx4, by1], [bx5, by1], [bx6, by1], [bx, by2], [bx1, by2], [[bx2, by2], [bx3, by2], [bx4, by2], [bx5, by2], [bx6, by2]
    
def plateau_deplacement(x, y):
    """déplacement avec les touches de directions"""
    
    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 105) :
            x = x + 1
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 12) :
            x = x - 1
    return x, y

def balle_deplacement(x, y) :
    "mouvement de la balle si elle touche le plateau ou l'un des cotes sauf le bas"
    global xballe, yballe, plateau_x, plateau_y
    y -= yballe
    x -= xballe
    if (x < 3) or (x > 123):
        xballe = -xballe
    elif (y < 3):
        yballe = -yballe
    
    if (plateau_y + 7) >= y >= (plateau_y -5) and (plateau_x) <= x <= (plateau_x + 10) :
        yballe = -yballe
    if (106) <= y < (128) :
        if (plateau_x -17) <= x <= (plateau_x) or (plateau_x + 17) <= x <= (plateau_x + 25):
            xballe = -xballe
            yballe = -yballe
        elif plateau_x <= x <= (plateau_x +15):
            yballe = -yballe
            xballe = -xballe
    else:
        xballe = xballe
        yballe = yballe
    
    return x, y

def blocs_suppression(x, y) :
    global xballe, yballe, blocs_x, blocs_y, blocs_x1, blocs_y1, blocs_x2, blocs_y2
    
    x -= xballe
    y -= yballe
    
    for bloc in blocs :
        if (39) >= x >= (30) and (15) >= y >= (5) :
            if balle_y == 15 or balle_y == 5 :
                yballe = -yballe
            if balle_x == 30 or balle_x == 39 :
                xballe = -xballe
            if balle_x == 30 or balle_x == 39 and balle_y == 5 or balle_y == 15 :
                xballe = -xballe
                yballe = -yballe
            blocs.remove(bloc)
        if (49) >= x >= (40) and (15) >= y >= (5) :
            if balle_y == 15 or balle_y == 5 :
                yballe = -yballe
            if balle_x == 40 or balle_x == 49 :
                xballe = -xballe
            if balle_x == 40 or balle_x == 49 and balle_y == 5 or balle_y == 15 :
                xballe = -xballe
                yballe = -yballe
            blocs.remove(bloc)
        if (59) >= x >= (50) and (15) >= y >= (5) :
            if balle_y == 15 or balle_y == 5 :
                yballe = -yballe
            if balle_x == 50 or balle_x == 59 :
                xballe = -xballe
            if balle_x == 50 or balle_x == 59 and balle_y == 5 or balle_y == 15 :
                xballe = -xballe
                yballe = -yballe
            blocs.remove(bloc)
        if (69) >= x >= (60) and (15) >= y >= (5) :
            if balle_y == 15 or balle_y == 5 :
                yballe = -yballe
            if balle_x == 60 or balle_x == 69 :
                xballe = -xballe
            if balle_x == 60 or balle_x == 69 and balle_y == 5 or balle_y == 15 :
                xballe = -xballe
                yballe = -yballe
            blocs.remove(bloc)
        if (79) >= x >= (70) and (15) >= y >= (5) :
            if balle_y == 15 or balle_y == 5 :
                yballe = -yballe
            if balle_x == 70 or balle_x == 39 :
                xballe = -xballe
            if balle_x == 70 or balle_x == 79 and balle_y == 5 or balle_y == 15 :
                xballe = -xballe
                yballe = -yballe
            blocs.remove(bloc)
        if (89) >= x >= (80) and (15) >= y >= (5) :
            if balle_y == 15 or balle_y == 5 :
                yballe = -yballe
            if balle_x == 80 or balle_x == 89 :
                xballe = -xballe
            if balle_x == 80 or balle_x == 89 and balle_y == 5 or balle_y == 15 :
                xballe = -xballe
                yballe = -yballe
            blocs.remove(bloc)
        if (99) >= x >= (90) and (15) >= y >= (5) :
            if balle_y == 15 or balle_y == 5 :
                yballe = -yballe
            if balle_x == 90 or balle_x == 99 :
                xballe = -xballe
            if balle_x == 90 or balle_x == 99 and balle_y == 5 or balle_y == 15 :
                xballe = -xballe
                yballe = -yballe 
            blocs.remove(bloc)
        if (39) >= x >= (30) and (25) >= y >= (15) :
            if balle_y == 25 or balle_y == 15 :
                yballe = -yballe
            if balle_x == 30 or balle_x == 39 :
                xballe = -xballe
            if balle_x == 30 or balle_x == 39 and balle_y == 15 or balle_y == 25 :
                xballe = -xballe
                yballe = -yballe
            blocs.remove(bloc)    
        if (49) >= x >= (40) and (25) >= y >= (15) :
            if balle_y == 15 or balle_y == 25 :
                yballe = -yballe
            if balle_x == 40 or balle_x == 49 :
                xballe = -xballe
            if balle_x == 40 or balle_x == 49 and balle_y == 25 or balle_y == 15 :
                xballe = -xballe
                yballe = -yballe
            blocs.remove(bloc)    
        if (59) >= x >= (50) and (25) >= y >= (15) :
            if balle_y == 15 or balle_y == 25 :
                yballe = -yballe
            if balle_x == 50 or balle_x == 59 :
                xballe = -xballe
            if balle_x == 50 or balle_x == 59 and balle_y == 25 or balle_y == 15 :
                xballe = -xballe
                yballe = -yballe
            blocs.remove(bloc)    
        if (69) >= x >= (60) and (25) >= y >= (15) :
            if balle_y == 15 or balle_y == 25 :
                yballe = -yballe
            if balle_x == 60 or balle_x == 69 :
                xballe = -xballe
            if balle_x == 60 or balle_x == 69 and balle_y == 25 or balle_y == 15 :
                xballe = -xballe
                yballe = -yballe
            blocs.remove(bloc)    
        if (79) >= x >= (70) and (25) >= y >= (15) :
            if balle_y == 15 or balle_y == 25 :
                yballe = -yballe
            if balle_x == 70 or balle_x == 39 :
                xballe = -xballe
            if balle_x == 70 or balle_x == 79 and balle_y == 25 or balle_y == 15 :
                xballe = -xballe
                yballe = -yballe
            blocs.remove(bloc)    
        if (89) >= x >= (80) and (25) >= y >= (15) :
            if balle_y == 15 or balle_y == 25 :
                yballe = -yballe
            if balle_x == 80 or balle_x == 89 :
                xballe = -xballe
            if balle_x == 80 or balle_x == 89 and balle_y == 25 or balle_y == 15 :
                xballe = -xballe
                yballe = -yballe
            blocs.remove(bloc)    
        if (99) >= x >= (90) and (25) >= y >= (15) :
            if balle_y == 15 or balle_y == 25 :
                yballe = -yballe
            if balle_x == 90 or balle_x == 99 :
                xballe = -xballe
            if balle_x == 90 or balle_x == 99 and balle_y == 25 or balle_y == 15 :
                xballe = -xballe
                yballe = -yballe 
            blocs.remove(bloc)    
        if (39) >= x >= (30) and (35) >= y >= (25) :
            if balle_y == 25 or balle_y == 35 :
                yballe = -yballe
            if balle_x == 30 or balle_x == 39 :
                xballe = -xballe
            if balle_x == 30 or balle_x == 39 and balle_y == 35 or balle_y == 25 :
                xballe = -xballe
                yballe = -yballe
            blocs.remove(bloc)    
        if (49) >= x >= (40) and (35) >= y >= (25) :
            if balle_y == 35 or balle_y == 25 :
                yballe = -yballe
            if balle_x == 40 or balle_x == 49 :
                xballe = -xballe
            if balle_x == 40 or balle_x == 49 and balle_y == 25 or balle_y == 35 :
                xballe = -xballe
                yballe = -yballe
            blocs.remove(bloc)    
        if (59) >= x >= (50) and (35) >= y >= (25) :
            if balle_y == 35 or balle_y == 25 :
                yballe = -yballe
            if balle_x == 50 or balle_x == 59 :
                xballe = -xballe
            if balle_x == 50 or balle_x == 59 and balle_y == 25 or balle_y == 35 :
                xballe = -xballe
                yballe = -yballe
            blocs.remove(bloc)    
        if (69) >= x >= (60) and (35) >= y >= (25) :
            if balle_y == 35 or balle_y == 25 :
                yballe = -yballe
            if balle_x == 60 or balle_x == 69 :
                xballe = -xballe
            if balle_x == 60 or balle_x == 69 and balle_y == 25 or balle_y == 35 :
                xballe = -xballe
                yballe = -yballe
            blocs.remove(bloc)    
        if (79) >= x >= (70) and (35) >= y >= (25) :
            if balle_y == 35 or balle_y == 25 :
                yballe = -yballe
            if balle_x == 70 or balle_x == 39 :
                xballe = -xballe
            if balle_x == 70 or balle_x == 79 and balle_y == 25 or balle_y == 35 :
                xballe = -xballe
                yballe = -yballe
            blocs.remove(bloc)    
        if (89) >= x >= (80) and (35) >= y >= (25) :
            if balle_y == 35 or balle_y == 25 :
                yballe = -yballe
            if balle_x == 80 or balle_x == 89 :
                xballe = -xballe
            if balle_x == 80 or balle_x == 89 and balle_y == 25 or balle_y == 35 :
                xballe = -xballe
                yballe = -yballe
            blocs.remove(bloc)    
        if (99) >= x >= (90) and (35) >= y >= (25) :
            if balle_y == 35 or balle_y == 25 :
                yballe = -yballe
            if balle_x == 90 or balle_x == 99 :
                xballe = -xballe
            if balle_x == 90 or balle_x == 99 and balle_y == 25 or balle_y == 35 :
                xballe = -xballe
                yballe = -yballe
            blocs.remove(bloc)    
        else : 
            xballe = xballe
            yballe = yballe
    return x, y

# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global plateau_x, plateau_y, balle_x, balle_y
    
    # mise à jour de la position du plateau
    plateau_x, plateau_y = plateau_deplacement(plateau_x, plateau_y)
    
    # mise à jour de la position de la balle

    balle_x, balle_y = balle_deplacement(balle_x, balle_y)
        
    balle_x, balle_y = blocs_suppression(balle_x, balle_y)
    
# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)
    
    # si la balle est sur l'ecran 128x128
    if balle_y <= 128 :
        # polygone de 6 cotes
        pyxel.rect(plateau_x, plateau_y, 11, 12, 14)
        pyxel.tri(plateau_x, plateau_y, plateau_x, plateau_y+11, plateau_x-11, plateau_y+11, 14)
        pyxel.tri(plateau_x+11, plateau_y, plateau_x+11, plateau_y+11, plateau_x+22, plateau_y+11, 14)
        pyxel.rect(plateau_x-11, plateau_y+11, 34, 3, 14)
    
        # balle de rayon 3
        pyxel.circ(balle_x, balle_y, 3, 10)
        
        # blocs 9x9 couleur 8 sur trois lignes
        for bloc in blocs :
            pyxel.rect(bloc[0], bloc[1], 9, 9, 8)


    else :
        pyxel.text(50,64, 'GAME OVER', 12)
    
pyxel.run(update, draw)
