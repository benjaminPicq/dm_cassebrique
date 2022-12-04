import pyxel
plateau_x = 128
plateau_y = 220

def plateau_deplacement(x, y):
    """déplacement avec les touches de directions"""

    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 202) :
            x = x + 4
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 20) :
            x = x - 4
    return x, y
  
  def update() :
    
    global plateau_x, plateau_y
    
    plateau_x, plateau_y = plateau_deplacement(plateau_x, plateau_y)

 def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)
    pyxel.rect(plateau_x, plateau_y, 32, 14, 3)
    pyxel.tri(plateau_x, plateau_y, plateau_x, plateau_y+15, plateau_x-15, plateau_y+15, 3)
    pyxel.tri(plateau_x+32, plateau_y, plateau_x+32, plateau_y+15, plateau_x+47, plateau_y+15,)
    
 pyxel.run(update, draw)
