import pyxel

# taille de la fenetre 128x128 pixels
# ne pas modifier
pyxel.init(128, 128, title="Nuit du c0de")

# position initiale du vaisseau
# (origine des positions : coin haut gauche)
vaisseau_x = 60

def vaisseau_deplacement(x, y):
    """déplacement avec les touches de directions"""

    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 120) :
            x = x + 1
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 0) :
            x = x - 1


  
  
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x

    # mise à jour de la position du vaisseau
    vaisseau_x = vaisseau_deplacement(vaisseau_x)


def draw():
    """création des objets (30 fois par seconde)"""

    pyxel.cls(0)

    pyxel.rect(vaisseau_x, 8, 8, 1)

pyxel.run(update, draw)

