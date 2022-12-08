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
xballe_speed = 3
yballe_speed = 3
blocs_x = [30, 40, 50, 60, 70, 80, 90]
blocs_y = [5, 5, 5, 5, 5, 5, 5]
blocs_x1 = [30, 40, 50, 60, 70, 80, 90]
blocs_y1 = [15, 15, 15, 15, 15, 15, 15]
blocs_x2 = [30, 40, 50, 60, 70, 80, 90]
blocs_y2 = [25, 25, 25, 25, 25, 25, 25]

def plateau_deplacement(x, y):
    """déplacement avec les touches de directions"""
    
    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 96.5) :
            x = x + 1
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 23.5) :
            x = x - 1
    return x, y

def balle_deplacement(x, y) :
    "mouvement de la balle si elle touche le plateau ou l'un des cotes sauf le bas"
    global xballe_speed, yballe_speed, plateau_x, plateau_y, blocs_x, blocs_y, blocs_x1, blocs_y1, blocs_x2, blocs_y2
    x -= xballe_speed
    y -= yballe_speed
    if (x < 3) or (x > 123):
        xballe_speed = -xballe_speed
        yballe_speed = yballe_speed
    elif (y < 3):
        xballe_speed = xballe_speed
        yballe_speed = -yballe_speed
    if  108 <= y <= (119):
        if (plateau_x -18) <= x < (plateau_x) or (plateau_x + 13) < x <= (plateau_x + 25):
            xballe_speed = -xballe_speed
            yballe_speed = -yballe_speed
        elif plateau_x <= x <= (plateau_x +15):
            xballe_speed = xballe_speed 
            yballe_speed = -yballe_speed
    else:
        xballe_speed = xballe_speed
        yballe_speed = yballe_speed
    
    for bloc_x in blocs_x and bloc_y in blocs_y :
        if bloc_x[0] - 4.5 <= x <= bloc_x[0] + 4.5 and bloc_y[0] - 4.5 <= bloc_y[0] + 4.5 :
            blocs_x.remove(bloc_x)
            blocs_y.remove(bloc_y)
            xballe_speed = xballe_speed
            yballe_speed = -yballe_speed
        if bloc_x[1] - 4.5 <= x <= bloc_x[1] + 4.5 and bloc_y[0] - 4.5 <= bloc_y[0] + 4.5 :
            blocs_x.remove(bloc_x)
            blocs_y.remove(bloc_y)
            xballe_speed = xballe_speed
            yballe_speed = -yballe_speed
        if bloc_x[2] - 4.5 <= x <= bloc_x[2] + 4.5 and bloc_y[0] - 4.5 <= bloc_y[0] + 4.5 :
            blocs_x.remove(bloc_x)
            blocs_y.remove(bloc_y)
            xballe_speed = xballe_speed
            yballe_speed = -yballe_speed
        if bloc_x[3] - 4.5 <= x <= bloc_x[3] + 4.5 and bloc_y[0] - 4.5 <= bloc_y[0] + 4.5 :
            blocs_x.remove(bloc_x)
            blocs_y.remove(bloc_y)
            xballe_speed = xballe_speed
            yballe_speed = -yballe_speed
        if bloc_x[4] - 4.5 <= x <= bloc_x[4] + 4.5 and bloc_y[0] - 4.5 <= bloc_y[0] + 4.5 :
            blocs_x.remove(bloc_x)
            blocs_y.remove(bloc_y)
            xballe_speed = xballe_speed
            yballe_speed = -yballe_speed
        if bloc_x[5] - 4.5 <= x <= bloc_x[5] + 4.5 and bloc_y[0] - 4.5 <= bloc_y[0] + 4.5 :
            blocs_x.remove(bloc_x)
            blocs_y.remove(bloc_y)
            xballe_speed = xballe_speed
            yballe_speed = -yballe_speed
        if bloc_x[6] - 4.5 <= x <= bloc_x[6] + 4.5 and bloc_y[0] - 4.5 <= bloc_y[0] + 4.5 :
            blocs_x.remove(bloc_x)
            blocs_y.remove(bloc_y)
            xballe_speed = xballe_speed
            yballe_speed = -yballe_speed
    for bloc_x1 in blocs_x1 and bloc_y1 in blocs_y1 :
        if bloc_x1[0] - 4.5 <= x <= bloc_x1[0] + 4.5 and bloc_y1[1] - 4.5 <= bloc_y1[1] + 4.5 :
            blocs_x1.remove(bloc_x)
            blocs_y1.remove(bloc_y)
            xballe_speed = xballe_speed
            yballe_speed = -yballe_speed
        if bloc_x1[1] - 4.5 <= x <= bloc_x1[1] + 4.5 and bloc_y1[1] - 4.5 <= bloc_y1[1] + 4.5 :
            blocs_x1.remove(bloc_x)
            blocs_y1.remove(bloc_y)
            xballe_speed = xballe_speed
            yballe_speed = -yballe_speed
        if bloc_x1[2] - 4.5 <= x <= bloc_x1[2] + 4.5 and bloc_y1[1] - 4.5 <= bloc_y1[1] + 4.5 :
            blocs_x1.remove(bloc_x)
            blocs_y1.remove(bloc_y)
            xballe_speed = xballe_speed
            yballe_speed = -yballe_speed
        if bloc_x1[3] - 4.5 <= x <= bloc_x1[3] + 4.5 and bloc_y1[1] - 4.5 <= bloc_y1[1] + 4.5 :
            blocs_x1.remove(bloc_x)
            blocs_y1.remove(bloc_y)
            xballe_speed = xballe_speed
            yballe_speed = -yballe_speed
        if bloc_x1[4] - 4.5 <= x <= bloc_x1[4] + 4.5 and bloc_y1[1] - 4.5 <= bloc_y1[1] + 4.5 :
            blocs_x1.remove(bloc_x)
            blocs_y1.remove(bloc_y)
            xballe_speed = xballe_speed
            yballe_speed = -yballe_speed
        if bloc_x1[5] - 4.5 <= x <= bloc_x1[5] + 4.5 and bloc_y1[1] - 4.5 <= bloc_y1[1] + 4.5 :
            blocs_x1.remove(bloc_x)
            blocs_y1.remove(bloc_y)
            xballe_speed = xballe_speed
            yballe_speed = -yballe_speed
        if bloc_x1[6] - 4.5 <= x <= bloc_x1[6] + 4.5 and bloc_y1[1] - 4.5 <= bloc_y1[1] + 4.5 :
            blocs_x1.remove(bloc_x)
            blocs_y1.remove(bloc_y)
            xballe_speed = xballe_speed
            yballe_speed = -yballe_speed
    for bloc_x2 in blocs_x2 and bloc_y2 in blocs_y2 :
        if bloc_x2[0] - 4.5 <= x <= bloc_x2[0] + 4.5 and bloc_y2[2] - 4.5 <= bloc_y2[2] + 4.5 :
            blocs_x2.remove(bloc_x)
            blocs_y2.remove(bloc_y)
            xballe_speed = xballe_speed
            yballe_speed = -yballe_speed
        if bloc_x2[1] - 4.5 <= x <= bloc_x2[1] + 4.5 and bloc_y2[2] - 4.5 <= bloc_y2[2] + 4.5 :
            blocs_x2.remove(bloc_x)
            blocs_y2.remove(bloc_y)
            xballe_speed = xballe_speed
            yballe_speed = -yballe_speed
        if bloc_x2[2] - 4.5 <= x <= bloc_x2[2] + 4.5 and bloc_y2[2] - 4.5 <= bloc_y2[2] + 4.5 :
            blocs_x2.remove(bloc_x)
            blocs_y2.remove(bloc_y)
            xballe_speed = xballe_speed
            yballe_speed = -yballe_speed
        if bloc_x2[3] - 4.5 <= x <= bloc_x2[3] + 4.5 and bloc_y2[2] - 4.5 <= bloc_y2[2] + 4.5 :
            blocs_x2.remove(bloc_x)
            blocs_y2.remove(bloc_y)
            xballe_speed = xballe_speed
            yballe_speed = -yballe_speed
        if bloc_x2[4] - 4.5 <= x <= bloc_x2[4] + 4.5 and bloc_y2[2] - 4.5 <= bloc_y2[2] + 4.5 :
            blocs_x2.remove(bloc_x)
            blocs_y2.remove(bloc_y)
            xballe_speed = xballe_speed
            yballe_speed = -yballe_speed
        if bloc_x2[5] - 4.5 <= x <= bloc_x2[5] + 4.5 and bloc_y2[2] - 4.5 <= bloc_y2[2] + 4.5 :
            blocs_x2.remove(bloc_x)
            blocs_y2.remove(bloc_y)
            xballe_speed = xballe_speed
            yballe_speed = -yballe_speed
        if bloc_x2[6] - 4.5 <= x <= bloc_x2[6] + 4.5 and bloc_y[2] - 4.5 <= bloc_y[2] + 4.5 :
            blocs_x2.remove(bloc_x)
            blocs_y2.remove(bloc_y)
            xballe_speed = xballe_speed
            yballe_speed = -yballe_speed
    return x, y

# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global plateau_x, plateau_y, balle_x, balle_y, blocs

    # mise à jour de la position du plateau
    plateau_x, plateau_y = plateau_deplacement(plateau_x, plateau_y)
    
    # mise à jour de la position de la balle
    balle_x, balle_y = balle_deplacement(balle_x, balle_y)
    
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
        pyxel.rect(plateau_x, plateau_y, 11, 7, 3)
        pyxel.tri(plateau_x, plateau_y, plateau_x, plateau_y+10, plateau_x-10, plateau_y+10, 3)
        pyxel.tri(plateau_x+11, plateau_y, plateau_x+11, plateau_y+10, plateau_x+21, plateau_y+10, 3)
        pyxel.rect(plateau_x-11, plateau_y+10, 32, 3, 3)
    
        # balle de rayon 3
        pyxel.circ(balle_x, balle_y, 3, 10)
        
        # blocs 9x9 couleur 8 sur trois lignes
        for bloc in range(0, len(blocs_x)) :
            bx = blocs_x[bloc-1]
            by = blocs_y[bloc-1]
            pyxel.rect(bx, by, 9, 9, 8)
        for bloc in range(0, len(blocs_x1)) :
            bx1 = blocs_x1[bloc-1]
            by1 = blocs_y1[bloc-1]
            pyxel.rect(bx1, by1, 9, 9, 8)
        for bloc in range(0, len(blocs_x2)) :
            bx2 = blocs_x2[bloc-1]
            by2 = blocs_y2[bloc-1]
            pyxel.rect(bx2, by2, 9, 9, 8)

    else :
        pyxel.text(50,64, 'GAME OVER', 12)
    
pyxel.run(update, draw)
