import pyxel
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
nmbr_bl = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
blocsx = [30, 40, 50, 60, 70, 80, 90, 30, 40, 50, 60, 70, 80, 90, 30, 40, 50, 60, 70, 80, 90]
blocsy = [5, 5, 5, 5, 5, 5, 5, 15, 15, 15, 15, 15, 15, 15, 25, 25, 25, 25, 25, 25, 25]
c = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]

def plateau_deplacement(x, y):
    """déplacement avec les touches de directions"""
    
    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 105) :
            x = x + 1
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 11) :
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

    for n in range(0, len(nmbr_bl)) :
        if blocsx[n] <= x <= (blocsx[n] + 12) and blocsy[n] <= y <= (blocsy[n] + 5) :
            blocsx.pop(n)
            blocsy.pop(n)
            c.pop(0)
            nmbr_bl.pop(0)
            yballe = -yballe
            score += 10
    
    else:
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
        
    if pyxel.btnr(pyxel.KEY_SPACE):
        jeu = True
    
    if jeu is True :
        # mise à jour de la position de la balle
        balle_x, balle_y = balle_deplacement(balle_x, balle_y)
# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)
        
    # polygone de 6 cotes
    pyxel.rect(plateau_x, plateau_y, 11, 12, 14)
    pyxel.tri(plateau_x, plateau_y, plateau_x, plateau_y+11, plateau_x-11, plateau_y+11, 14)
    pyxel.tri(plateau_x+11, plateau_y, plateau_x+11, plateau_y+11, plateau_x+22, plateau_y+11, 14)
    pyxel.rect(plateau_x-11, plateau_y+11, 34, 3, 14)
    
    # balle de rayon 3
    pyxel.circ(balle_x, balle_y, 3, 10)
        
    # blocs 9x2 couleur 8 sur trois lignes
    for n in range(0, len(nmbr_bl)) :
        pyxel.rect(blocsx[n], blocsy[n], 9, 2, c[n])
       
pyxel.run(update, draw)
