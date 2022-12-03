import pyxel

# taille de la fenetre 128x128 pixels
# ne pas modifier
pyxel.init(128, 128, title="Nuit du c0de")

# position initiale du vaisseau
# (origine des positions : coin haut gauche)
plateau_x = 60
plateau_y = 30

#initialisation blocs
bloc_liste = []



def plateau_deplacement(x, y):
    """déplacement avec les touches de directions"""

    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 120) :
            x = x + 1
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 0) :
            x = x - 1
    return x, y

def bloc_création(bloc_liste) : 
    if (pyxel.frame_count % 30 == 0) :
        bloc_liste.append([random.randint(0, 40), 0])
    return bloc_liste
# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global plateau_x, plateau_y, bloc_liste

    # mise à jour de la position du vaisseau
    plateau_x, plateau_y = plateau_deplacement(plateau_x, plateau_y)
    
    #position des blocs
    bloc_liste = bloc_creation(bloc_liste)


# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)

    # vaisseau (carre 8x8)
    pyxel.rect(plateau_x, plateau_y, 12, 4, 3)
    
    # blocs destructibles (3x3)
    for bloc in bloc_liste :
        pyxel.rect(bloc[0], bloc[1], bloc[2], 3, 3, 8)

pyxel.run(update, draw)

