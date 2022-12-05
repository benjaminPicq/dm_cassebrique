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
blocs = []
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

def blocs_creation(blocs):
    """création aléatoire des blocs"""
    for b in range(5)
        blocs.append([random.randint(0, 120), 0, 30])
    return blocs
# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global plateau_x, plateau_y, balle_x, balle_y, blocs

    # mise à jour de la position du vaisseau
    plateau_x, plateau_y = plateau_deplacement(plateau_x, plateau_y)
        
    balle_x, balle_y = balle_deplacement(balle_x, balle_y)
    
    blocs = blocs_creation(blocs)

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
        
        for bloc in blocs :
            pyxel.rect(bloc[0], bloc[1], 9, 9, 8)        

    else :
        pyxel.text(50,64, 'GAME OVER', 12)
    
pyxel.run(update, draw)
