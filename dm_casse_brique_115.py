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
bx = [30, 5]
bx1 = [40, 5]
bx2 = [50, 5]
bx3 = [60, 5]
bx4 = [70, 5]
bx5 = [80, 5]
bx6 = [90, 5]
bx_ = [30, 15]
bx_1 = [40, 15]
bx_2 = [50, 15]
bx_3 = [60, 15]
bx_4 = [70, 15]
bx_5 = [80, 15]
bx_6 = [90, 15]
bx7 = [30, 25]
bx8 = [40, 25]
bx9 = [50, 25]
bx10 = [60, 25]
bx11 = [70, 25]
bx12 = [80, 25]
bx13 = [90, 25]
    
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

def suppression_blocs(x, y) :
    global xballe, yballe, bx, bx1, bx2, bx3, bx4, bx5, bx6, bx_, bx_1, bx_2, bx_3, bx_4, bx_5, bx_6, bx7, bx8, bx9, bx10, bx11, bx12, bx13
    x -= yballe
    y -= xballe
    if bx[0] >= x >= bx[0] + 9 and y == bx[1] or bx1[0] >= x >= bx1[0] + 9 and y == bx1[1] or bx2[0] >= x >= bx2[0] + 9 and y == bx2[1] \
    or bx3[0] >= x >= bx3[0] + 9 and y == bx3[1] or bx4[0] >= x >= bx4[0] + 9 and y == bx4[1] or bx5[0] >= x >= bx5[0] + 9 and y == bx5[1] \
    or bx6[0] >= x >= bx6[0] + 9 and y == bx6[1] or bx_[0] >= x >= bx_[0] + 9 and y == bx_[1] or bx_1[0] >= x >= bx_1[0] + 9 and y == bx_1[1] \
    or bx_2[0] >= x >= bx_2[0] + 9 and y == bx_2[1] or bx_3[0] >= x >= bx_3[0] + 9 and y == bx_3[1] or bx_4[0] >= x >= bx_4[0] + 9 and y == bx_4[1] \
    or bx7[0] >= x >= bx7[0] + 9 and y == bx7[1] or bx8[0] >= x >= bx8[0] + 9 and y == bx8[1] or bx9[0] >= x >= bx9[0] + 9 and y == bx9[1] \
    or bx10[0] >= x >= bx10[0] + 9 and y == bx10[1] or bx11[0] >= x >= bx11[0] + 9 and y == bx11[1] or bx12[0] >= x >= bx12[0] + 9 and y == bx12[1] \
    or bx13[0] >= x >= bx13[0] + 9 and y == bx13[1] :
        xballe = -xballe
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
        pyxel.rect(bx[0], bx[1], 9, 9, 8)
        pyxel.rect(bx1[0], bx1[1], 9, 9, 8)
        pyxel.rect(bx2[0], bx2[1], 9, 9, 8)
        pyxel.rect(bx3[0], bx3[1], 9, 9, 8)
        pyxel.rect(bx4[0], bx4[1], 9, 9, 8)
        pyxel.rect(bx5[0], bx5[1], 9, 9, 8)
        pyxel.rect(bx6[0], bx6[1], 9, 9, 8)
        
        pyxel.rect(bx_[0], bx_[1], 9, 9, 8)
        pyxel.rect(bx_1[0], bx_1[1], 9, 9, 8)
        pyxel.rect(bx_2[0], bx_2[1], 9, 9, 8)
        pyxel.rect(bx_3[0], bx_3[1], 9, 9, 8)
        pyxel.rect(bx_4[0], bx_4[1], 9, 9, 8)
        pyxel.rect(bx_5[0], bx_5[1], 9, 9, 8)
        pyxel.rect(bx_6[0], bx_6[1], 9, 9, 8)
        
        pyxel.rect(bx7[0], bx7[1], 9, 9, 8)
        pyxel.rect(bx8[0], bx8[1], 9, 9, 8)
        pyxel.rect(bx9[0], bx9[1], 9, 9, 8)
        pyxel.rect(bx10[0], bx10[1], 9, 9, 8)
        pyxel.rect(bx11[0], bx11[1], 9, 9, 8)
        pyxel.rect(bx12[0], bx12[1], 9, 9, 8)
        pyxel.rect(bx13[0], bx13[1], 9, 9, 8)

    else :
        pyxel.text(50,64, 'GAME OVER', 12)
    
pyxel.run(update, draw)
