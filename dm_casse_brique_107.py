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

blocs = [ [bx, by, 8], [bx1, by, 8], [bx2, by, 8], [bx3, by, 8], [bx4, by, 8], [bx5, by, 8], [bx6, by, 8], [bx, by1, 8], [bx1, by1, 8], [bx2, by1, 8], [bx3, by1, 8], [bx4, by1, 8], [bx5, by1, 8], [bx6, by1, 8], [bx, by2, 8], [bx1, by2, 8], [bx2, by2, 8], [bx3, by2, 8], [bx4, by2, 8], [bx5, by2, 8], [bx6, by2, 8] ]
    
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
        pyxel.rect(plateau_x, plateau_y, 11, 12, 14)
        pyxel.tri(plateau_x, plateau_y, plateau_x, plateau_y+11, plateau_x-11, plateau_y+11, 14)
        pyxel.tri(plateau_x+11, plateau_y, plateau_x+11, plateau_y+11, plateau_x+22, plateau_y+11, 14)
        pyxel.rect(plateau_x-11, plateau_y+11, 34, 3, 14)
    
        # balle de rayon 3
        pyxel.circ(balle_x, balle_y, 3, 10)
        
        # blocs 9x9 couleur 8 sur trois lignes
        for bloc in blocs :
            pyxel.rect(bloc[0], bloc[1], 9, 9, bloc[2])


    else :
        pyxel.text(50,64, 'GAME OVER', 12)
    
pyxel.run(update, draw)
