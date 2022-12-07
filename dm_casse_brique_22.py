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
blocs = []

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
    "mouvement de la balle si elle touche le plateau ou l'un des cotes sauf le bas"
    global xballe_speed, yballe_speed, plateau_x, plateau_y, balle_x, balle_y
    x -= xballe_speed
    y -= yballe_speed
    if (pyxel.frame_count % 300 == 0) :
        xballe_speed = xballe_speed + 1
        yballe_speed = yballe_speed + 1
    elif (pyxel.frame_count % 600 == 0) :
        xballe_speed = xballe_speed + 1
        yballe_speed = yballe_speed + 1
    elif (pyxel.frame_count % 900 == 0) :
        xballe_speed = xballe_speed + 1
        yballe_speed = yballe_speed + 1
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

def blocs_creation(blocs) :
    """création aléatoire des blocs"""
    if (pyxel.frame_count % 30 == 0) :
        blocs.append([random.radint(0, 120, 10, 30)])
    return blocs
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
    
    # insertion des données aleatoires dans la liste blocs
    blocs = blocs_creation(blocs)

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
        pyxel.rect(plateau_x, plateau_y, 16, 10, 3)
        pyxel.tri(plateau_x, plateau_y, plateau_x, plateau_y+15, plateau_x-15, plateau_y+15, 3)
        pyxel.tri(plateau_x+16, plateau_y, plateau_x+16, plateau_y+15, plateau_x+31, plateau_y+15, 3)
        pyxel.rect(plateau_x-15, plateau_y+15, 47, 4, 3)
    
        # balle de rayon 3
        pyxel.circ(balle_x, balle_y, 3, 10)
        
        # blocs 9x9 couleur 8
        for bloc in blocs :
            pyxel.rect(bloc[0], bloc[1], 9, 9, 8)        

    else :
        pyxel.text(50,64, 'GAME OVER', 12)
    
pyxel.run(update, draw)
