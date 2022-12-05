import pyxel, random
# taille de la fenetre 128x128 pixels
# ne pas modifier
pyxel.init(128, 128, title="Nuit du c0de")

# position initiale du vaisseau
# (origine des positions : coin haut gauche)
plateau_x = 60
plateau_y = 110
balle_x = 60
balle_y = 50
xballe_speed = 3
yballe_speed = 3
exleft = 19
exright = 109
extop = 31
exbtom = 52
briques_x1 = []
briques_y1 = []
briques_x2 = []
briques_y2 = []
briques_x3 = []
briques_y3 = []
couleur1 = 8

def plateau_deplacement(x, y):
    """déplacement avec les touches de directions"""
    
    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 120) :
            x = x + 1
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 0) :
            x = x - 1
    return x, y

def balle_deplacement(x, y) :
    global xballe_speed, yballe_speed, plateau_x, plateau_y, balle_x, balle_y, exleft, exright, exbtom, extop
    x -= xballe_speed
    y -= yballe_speed
    if (x < 5) or (x > 123):
        xballe_speed = -xballe_speed
        yballe_speed = yballe_speed
    elif (y < 5):
        xballe_speed = xballe_speed
        balle_y = balle_y - 5
        yballe_speed = -yballe_speed
    if  107 <= y <= (119):
        if (plateau_x -20) <= x < (plateau_x) or (plateau_x + 15) < x <= (plateau_x + 35):
            balle_y = balle_y + 5
            xballe_speed = -xballe_speed
            yballe_speed = -yballe_speed
        elif plateau_x <= x <= (plateau_x +15):
            balle_y = balle_y + 5
            xballe_speed = xballe_speed 
            yballe_speed = -yballe_speed
    else:
        xballe_speed = xballe_speed
        yballe_speed = yballe_speed
    
    return x, y

def briques_creation(x, y) :
    for i in range(1) :
        briques_x1.append(10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110)
        briques_y1.append(5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
    for i in range(1) :
        briques_x2.append(10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110)
        briques_y2.append(15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15) 
    for i in range(1) :
        briques_x3.append(10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110)
        briques_y3.append(25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25)
    return x, y
# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global plateau_x, plateau_y, balle_x, balle_y

    # mise à jour de la position du vaisseau
    plateau_x, plateau_y = plateau_deplacement(plateau_x, plateau_y)
        
    balle_x, balle_y = balle_deplacement(balle_x, balle_y)

# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)
    
    if balle_y <= 128 :
        
        # polygone de 6 cotes
        pyxel.rect(plateau_x, plateau_y, 16, 10, 3)
        pyxel.tri(plateau_x, plateau_y, plateau_x, plateau_y+15, plateau_x-15, plateau_y+15, 3)
        pyxel.tri(plateau_x+16, plateau_y, plateau_x+16, plateau_y+15, plateau_x+31, plateau_y+15, 3)
        pyxel.rect(plateau_x-15, plateau_y+15, 47, 4, 3)
    

        pyxel.circ(balle_x, balle_y, 3, 10)
        
        pyxel.rect(briques_x1, briques_y1, 9, 9, couleur1)
        pyxel.rect(briques_x1, briques_y1, 9, 9, couleur1)
        pyxel.rect(briques_x3, briques_y3, 9, 9, couleur1)

    else :
        pyxel.text(50,64, 'GAME OVER', 12)
    
pyxel.run(update, draw)
