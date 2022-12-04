import pyxel
import turtle

# taille de la fenetre 128x128 pixels
# ne pas modifier
pyxel.init(128, 128, title="Nuit du c0de")

# position initiale du vaisseau
# (origine des positions : coin haut gauche)
plateau_x = 60
plateau_y = 90
blocs = []
balle_x = 60
balle_y = 85

def plateau_deplacement(x, y):
    """déplacement avec les touches de directions"""

    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 120) :
            x = x + 1
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 0) :
            x = x - 1
    return x, y

def bloc_creation(blocs) :
    for x in range(10, 10) :
        pyxel.rect(blocs[1], 7, 7, 8)   
    return blocs

def balle_creation(balle) :
    turtle = turtle.Turtle()
    rayon = 20
    turtle.circle(rayon)
    return balle
# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global plateau_x, plateau_y, blocs, balle_x, balle_y

    # mise à jour de la position du vaisseau
    plateau_x, plateau_y = plateau_deplacement(plateau_x, plateau_y)
    
    blocs = bloc_creation(blocs)
    
    balle_x, balle_y = balle_creation(balle_x, balle_y)
# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)

    # vaisseau (rectangle 20x4)
    pyxel.rect(plateau_x, plateau_y, 20, 4, 3)
    

pyxel.run(update, draw)
