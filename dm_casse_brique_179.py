import pyxel
# taille de la fenetre 128x128 pixels
# ne pas modifier
pyxel.init(128, 128, title="Nuit du c0de")

# position initiale du plateau
plateau_x = 60
plateau_y = 110

# position initiale de la balle
balle_x = 60
balle_y = 98

# vitesse de la balle
xballe = 1
yballe = 1

# coordonnes des blocs
nmbr_bl = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
blocsx = [20, 40, 50, 70, 80, 100, 110, 5, 25, 55, 65, 75, 105, 120, 20, 40, 50, 70, 80, 100, 110]
blocsy = [5, 10, 5, 10, 5, 10, 5, 20, 15, 20, 15, 20, 15, 20, 25, 30, 25, 30, 25, 30, 25]
c = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]

vies = 3
score = 0
jeu = False

def plateau_deplacement(x, y):
    """déplacement avec les touches de directions"""
    
    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 105) :
            x = x + 1
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 11) :
            x = x - 1
    return x, y

def balle_deplacement(x, y) :
    "mouvement de la balle si elle touche le plateau ou l'un des cotes sauf le bas"
    global xballe, yballe, plateau_x, plateau_y
    y -= yballe
    x -= xballe
    if (x < 3) or (x > 123):
        xballe = -xballe
    elif (y < 3):
        yballe = -yballe
    
    if (plateau_y + 7) >= y >= (plateau_y -5) and (plateau_x) <= x <= (plateau_x + 10) :
        yballe = (-yballe + 0.05)
        xballe = (xballe + 0.05)
    if (106) <= y < (128) :
        if (plateau_x -17) <= x <= (plateau_x) or (plateau_x + 17) <= x <= (plateau_x + 25):
            xballe = (-xballe + 0.05)
            yballe = (-yballe + 0.05)
        elif plateau_x <= x <= (plateau_x +15):
            yballe = (-yballe + 0.05)
            xballe = (-xballe + 0.05)

    for n in range(0, len(nmbr_bl)) :
        if blocsx[n] <= x <= (blocsx[n] + 12) and blocsy[n] <= y <= (blocsy[n] + 5) :
            blocsx.pop(n)
            blocsy.pop(n)
            c.pop(0)
            nmbr_bl.pop(0)
            yballe = -yballe
            score += 10
            xballe += 0.01
            yballe += 0.01
    
    else:
        xballe = xballe
        yballe = yballe
    return x, y

def jeux(jeu, vies) :
    global balle_y
    if balle_y > 128 :
        vies -= 1
        jeu = False
    return jeu, vies
# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global plateau_x, plateau_y, balle_x, balle_y, jeu, vies
    
    jeu, vies = jeux(jeu, vies)
    # mise à jour de la position du plateau
    plateau_x, plateau_y = plateau_deplacement(plateau_x, plateau_y)
    
    # si le joueuer n'a pas commence a jouer ou s'il a perdu une vie
    if jeu == False :
        balle_x, balle_y = (plateau_x + 5), (plateau_y - 12)
    
    # si le joueuer touche le bouton espace
    if pyxel.btnr(pyxel.KEY_SPACE):
        jeu = True
        
    if jeu == True :
        # mise à jour de la position de la balle
        balle_x, balle_y = balle_deplacement(balle_x, balle_y)
# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)
    
    if jeu == False :
        pyxel.text(20, 64, 'PRESS SPACE TO START', 11)
        
    # si la balle sort su cadre
    if vies < 1 :
        pyxel.cls(0)
        pyxel.text(50,64, 'GAME OVER', 12)
    
    # si il ne reste plus de blocs
    elif len(nmbr_bl) == 0 :
        pyxel.cls(0)
        pyxel.text(50, 64, 'VICTORY', 12)
        
    else :
        # polygone de 6 cotes
        pyxel.rect(plateau_x, plateau_y, 11, 12, 14)
        pyxel.tri(plateau_x, plateau_y, plateau_x, plateau_y+11, plateau_x-11, plateau_y+11, 14)
        pyxel.tri(plateau_x+11, plateau_y, plateau_x+11, plateau_y+11, plateau_x+22, plateau_y+11, 14)
        pyxel.rect(plateau_x-11, plateau_y+11, 34, 3, 14)
    
        # balle de rayon 3
        pyxel.circ(balle_x, balle_y, 3, 10)
        
        # blocs 9x2 couleur 8 sur trois lignes
        for n in range(0, len(nmbr_bl)) :
            pyxel.rect(blocsx[n], blocsy[n], 9, 2, c[n])

pyxel.run(update, draw)
