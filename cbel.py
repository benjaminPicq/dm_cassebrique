import pyxel

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
# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global plateau_x, plateau_y, balle_x, balle_y

    # mise à jour de la position du vaisseau
    plateau_x, plateau_y = plateau_deplacement(plateau_x, plateau_y)

# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)

    # plateau (polygone de 6 côtés 20x4)
    pyxel.rect(plateau_x, plateau_y, 20, 4, 3)
    pyxel.tri(plateau_x, plateau_y, plateau_x, plateau_y+5, plateau_x-5, plateau_y+5, 3)
    pyxel.tri(plateau_x+20, vaisseau_y, vaisseau_x+20, vaisseau_y+5, vaisseau_x+25, vaisseau_y+5, 3)
    pyxel.rect(vaisseau_x-5, vaisseau_y+5, 20, 4, 3)
    
    # balle (cercle, rayon = 3, couleur)
    pyxel.circ(balle_x, balle_y, 3, 10)
    

pyxel.run(update, draw)

