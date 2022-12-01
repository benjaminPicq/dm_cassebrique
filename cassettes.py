import pyxel

# taille de la fenetre 128x128 pixels
# ne pas modifier
pyxel.init(128, 128, title="Nuit du c0de")

# position initiale du vaisseau
# (origine des positions : coin haut gauche)
vaisseau_x = 60
vaisseau_y = 100
bloc[0]_x = 5
bloc[0]_y = 5


def vaisseau_deplacement(x, y):
    """déplacement avec les touches de directions"""

    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 120) :
            x = x + 1
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 0) :
            x = x - 1
    return x, y

def bloc(blocs_destructibles_liste) :
  """faire une brique que la balle va détruire pour obtenir des points"""
  if (pyxel.frame_count % 30 == 0) :
    blocs_destructibles_liste.append([random.randint(0, 60), 0])
  return blocs_destructibles_liste


# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y, blocs_destructibles_liste

    # mise à jour de la position du vaisseau
    vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)
    blocs_destructibles_liste =  bloc


# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)

    # vaisseau (rectangle 12x4)
    pyxel.rect(vaisseau_x, vaisseau_y, 12, 4, 3)
    
    # bloc (4x4)
    pyxel.rect(bloc[0], 4, 4, 8)

pyxel.run(update, draw)

