import pyxel

# taille de la fenetre 128x128 pixels
# ne pas modifier
pyxel.init(128, 128, title="Nuit du c0de")

# position initiale du vaisseau
# (origine des positions : coin haut gauche)
plateau_x = 60
plateau_y = 90

#initialisation blocs
bloc1_x = 10
bloc1_y = 5
bloc2_x = 20
bloc2_y = 5
bloc3_x = 30
bloc3_y = 5
bloc4_x = 40
bloc4_y = 5
bloc5_x = 50
bloc5_y = 5

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

    # vaisseau (rectangle 12x4)
    pyxel.rect(plateau_x, plateau_y, 12, 4, 3)
    
    # blocs (7x7)
    pyxel.rect(bloc1_x, bloc1_y, 7, 7, 8)
    pyxel.rect(bloc2_x, bloc2_y, 7, 7, 8)
    pyxel.rect(bloc3_x, bloc3_y, 7, 7, 8)
    pyxel.rect(bloc4_x, bloc4_y, 7, 7, 8)
    pyxel.rect(bloc5_x, bloc5_y, 7, 7, 8)

pyxel.run(update, draw)

