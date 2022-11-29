# dm_cassebrique
import pyxel    

pyxel.innit(128, 128)
plateau_x = 60
plateau_y = 60

def plateau_deplacements(x, y) :
  """
  permettre une interaction entre le clavier
  pour le joueur et le jeu en cour
  """
  if pyxel.btn(pyxel.KEY_RIGHT) :
    if (x < 120) :
      x = x + 1
  if pyxel.btn(pyxel.KEY_LEFT):
    if (x > 0) :
      x = x - 1
  if pyxel.btn(pyxel.KEY_DOWN):
    if (y < 120) :
      y = y + 1
  if pyxel.btn(pyxel.KEY_UP):
    if (y > 0) :
      y = y - 1
return x, y

def update() :
  """
  mise à jour des variables (30 fois par seconde)
  """
  plateau_x, plateau_y = plateau_deplacements(plateau_x, plateau_y)
  
def draw() :
  """
  créer des objets tel que la balle, le plateau
  et les différentes briques
  """
   pyxel.cls(0)
   pyxel.rect(plateau_x, plateau_y, 8, 8, 1)
   pyxel.run(update, draw)
