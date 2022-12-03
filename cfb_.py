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
bloc6_x = 60
bloc6_y = 5
bloc7_x = 70
bloc7_y = 5
bloc8_x = 80
bloc8_y = 5
bloc9_x = 90
bloc9_y = 5
bloc10_x = 100
bloc10_y = 5
bloc11_x = 110
bloc11_y = 5



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

    # vaisseau (rectangle 20x4)
    pyxel.rect(plateau_x, plateau_y, 20, 4, 3)
    
    # blocs (7x7)
    pyxel.rect(bloc1_x, bloc1_y, 7, 7, 8)
    pyxel.rect(bloc2_x, bloc2_y, 7, 7, 8)
    pyxel.rect(bloc3_x, bloc3_y, 7, 7, 8)
    pyxel.rect(bloc4_x, bloc4_y, 7, 7, 8)
    pyxel.rect(bloc5_x, bloc5_y, 7, 7, 8)
    pyxel.rect(bloc6_x, bloc6_y, 7, 7, 8)
    pyxel.rect(bloc7_x, bloc7_y, 7, 7, 8)
    pyxel.rect(bloc8_x, bloc8_y, 7, 7, 8)
    pyxel.rect(bloc9_x, bloc9_y, 7, 7, 8)
    pyxel.rect(bloc10_x, bloc10_y, 7, 7, 8)
    pyxel.rect(bloc11_x, bloc11_y, 7, 7, 8)

pyxel.run(update, draw)

