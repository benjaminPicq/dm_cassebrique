import pyxel

# taille de la fenetre 128x128 pixels
# ne pas modifier
pyxel.init(128, 128, title="Nuit du c0de")

# position initiale du vaisseau
# (origine des positions : coin haut gauche)
plateau_x = 60
plateau_y = 110

def plateau_deplacement(x, y):
    """déplacement avec les touches de directions"""

    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 120) :
            x = x + 1
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 0) :
            x = x - 1
    return x, y
# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global plateau_x, plateau_y

    # mise à jour de la position du vaisseau
    plateau_x, plateau_y = plateau_deplacement(plateau_x, plateau_y)

# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)

    # plateau (polygone de 6 côtés)
    pyxel.rect(plateau_x, plateau_y, 20, 10, 3)
    pyxel.tri(plateau_x, plateau_y, plateau_x, plateau_y+11, plateau_x-11, plateau_y+11, 3)
    pyxel.tri(plateau_x+20, plateau_y, plateau_x+20, plateau_y+11, plateau_x+31, plateau_y+11, 3)
    pyxel.rect(plateau_x-11, plateau_y+11, 43, 4, 3)
    
    pyxel.rect(10, 5, 7, 7, 8)
    pyxel.rect(20, 5, 7, 7, 8)
    pyxel.rect(30, 5, 7, 7, 8)
    pyxel.rect(40, 5, 7, 7, 8)
    pyxel.rect(50, 5, 7, 7, 8)
    pyxel.rect(60, 5, 7, 7, 8)
    pyxel.rect(70, 5, 7, 7, 8)
    pyxel.rect(80, 5, 7, 7, 8)
    pyxel.rect(90, 5, 7, 7, 8)
    pyxel.rect(100, 5, 7, 7, 8)
    pyxel.rect(110, 5, 7, 7, 8)
    
    pyxel.rect(10, 15, 7, 7, 8)
    pyxel.rect(20, 15, 7, 7, 8)
    pyxel.rect(30, 15, 7, 7, 8)
    pyxel.rect(40, 15, 7, 7, 8)
    pyxel.rect(50, 15, 7, 7, 8)
    pyxel.rect(60, 15, 7, 7, 8)
    pyxel.rect(70, 15, 7, 7, 8)
    pyxel.rect(80, 15, 7, 7, 8)
    pyxel.rect(90, 15, 7, 7, 8)
    pyxel.rect(100, 15, 7, 7, 8)
    pyxel.rect(110, 15, 7, 7, 8)
    
    pyxel.rect(10, 25, 7, 7, 8)
    pyxel.rect(20, 25, 7, 7, 8)
    pyxel.rect(30, 25, 7, 7, 8)
    pyxel.rect(40, 25, 7, 7, 8)
    pyxel.rect(50, 25, 7, 7, 8)
    pyxel.rect(60, 25, 7, 7, 8)
    pyxel.rect(70, 25, 7, 7, 8)
    pyxel.rect(80, 25, 7, 7, 8)
    pyxel.rect(90, 25, 7, 7, 8)
    pyxel.rect(100, 25, 7, 7, 8)
    pyxel.rect(110, 25, 7, 7, 8)

pyxel.run(update, draw)
