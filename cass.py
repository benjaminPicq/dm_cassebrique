import pyxel    

pyxel.innit(128, 128)
plateau_x = 60

def plateau_deplacements(x) :
  """
  permettre une interaction entre le clavier
  pour le joueur et le jeu en cour
  """
  if pyxel.btn(pyxel.KEY_RIGHT) :
    if (x < 120) :
      x = x + 1
  if pyxel.btn(pyxel.KEY_LEFT) :
    if (x > 0) :
      x = x - 1
      return x
def update() :
  """
  mise à jour des variables (30 fois par seconde)
  """
  plateau_x = plateau_deplacements(plateau_x)

def draw() :
  """
  créer des objets tel que la balle, le plateau
  et les différentes briques
  """
  pyxel.cls(0)
  pyxel.rect(plateau_x, 8, 8, 1)
