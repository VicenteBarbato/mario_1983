import pyxel

class Tuberias:
    """Ubicaremos la funcionalidad de las tuberias"""
    def __init__(self, x, y):
          
        self.x = x
        self.y = y

    def draw_tuberia0_izq(self):    
        pyxel.blt(self.x, self.y, 2, 8, 234, 26, 27)

    def draw_tuberia0_der(self):     
        pyxel.blt(self.x, self.y, 2, 7, 170, 26, 27)

    def draw_tuberia1_izq(self):
          pyxel.blt(self.x, self.y, 2, 47, 158, 47, 32)

class Bloques:
    """Ubicaremos la funcionalidad de los bloques """
    def __init__(self, x, y):
          
          self.x = x
          self.y = y

    def draw_primer_nivel_izq(self):
            pos = 0
            for i in range(11):
                pyxel.blt(self.x + pos, self.y, 2, 108, 186, 7, 7)
                pos += 8

    def draw_primer_nivel_der(self):
            pos = 0
            for i in range(11):
                pyxel.blt(self.x - pos, self.y, 2, 108, 186, 7, 7)
                pos += 8

    def draw_segundo_nivel_izq(self):
            pos = 0
            for i in range(5):
                pyxel.blt(self.x + pos, self.y, 2, 108, 186, 7, 7)
                pos += 8

    def draw_segundo_nivel_centro(self):
            pos = 0
            for i in range(12):
                pyxel.blt(self.x + pos, self.y, 2, 108, 186, 7, 7)
                pos += 8

    def draw_segundo_nivel_der(self):
            pos = 0
            for i in range(5):
                pyxel.blt(self.x - pos, self.y, 2, 108, 186, 7, 7)
                pos += 8

    def draw_tercer_nivel_izq(self):
            pos = 0
            for i in range(13):
                pyxel.blt(self.x + pos, self.y, 2, 108, 186, 7, 7)
                pos += 8

    def draw_tercer_nivel_der(self):
            pos = 0
            for i in range(13):
                pyxel.blt(self.x - pos, self.y, 2, 108, 186, 7, 7)
                pos += 8
