import turtle
import random
import sys
import os

class MainGame:
    
    def __init__(self, counterVar):
        self.counterVar = counterVar
        self.score = 0
        self.total_click = 0
        
        # Ekranı Ayarla
        self.main_screen = turtle.Screen()
        self.main_screen.bgpic(self.resource_path("../bgpic.gif"))
        self.main_screen.screensize(600, 338)
        self.main_screen.setup(600, 338)
        self.main_screen.addshape(self.resource_path("../turtlepic.gif"))
        self.main_screen.addshape(self.resource_path("../endgameturtle.gif"))

        # Kaplumbağa Objeleri
        self.turtle_turtle = turtle.Turtle()
        self.turtle_turtle.shape(self.resource_path("../turtlepic.gif"))
        self.turtle_turtle.penup()

        self.turtle_writer = turtle.Turtle()
        self.turtle_writer.hideturtle()
        self.turtle_writer.penup()
        self.turtle_writer.color("red")

        self.turtle_counter = turtle.Turtle()
        self.turtle_counter.penup()
        self.turtle_counter.hideturtle()

        self.turtle_endgame = turtle.Turtle()
        self.turtle_endgame.hideturtle()
        self.turtle_endgame.shape(self.resource_path("../endgameturtle.gif"))

        # Oyun Başlat
        self.turtle_teleport()
        self.counter()
        self.scoreboard_writer()
        
        # Tıklama Eventleri
        self.turtle_turtle.onclick(self.turtle_clicker)
        self.main_screen.onclick(self.screen_clicker)
        
        # Ana Döngü
        turtle.mainloop()

    def resource_path(self, relative_path):
        """PyInstaller için kaynak dosya yolu belirler"""
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return relative_path

    def scoreboard_writer(self):
        """Skor tablosunu günceller"""
        self.turtle_writer.clear()
        self.turtle_writer.goto(-100, 128)
        self.turtle_writer.write(f"Score: {self.score}    Total Try: {self.total_click}", font=("helvetica", 18, "bold"))

    def turtle_clicker(self, x, y):
        """Kaplumbağaya tıklandığında skoru artırır"""
        self.score += 1
        self.scoreboard_writer()

    def screen_clicker(self, x, y):
        """Ekranın herhangi bir yerine tıklandığında toplam denemeyi artırır"""
        self.total_click += 1
        self.scoreboard_writer()

    def counter(self):
        """Sayaç mekanizması"""
        if self.counterVar > 0:
            self.turtle_counter.clear()
            self.turtle_counter.goto(-10, 98)
            self.counterVar -= 1
            self.turtle_counter.write(self.counterVar, font=("helvetica", 18, "bold"))
            self.main_screen.ontimer(self.counter, 1000)
        else:
            self.gameover()

    def turtle_teleport(self):
        """Kaplumbağayı rastgele bir noktaya ışınlar"""
        if self.counterVar > 0:
            xPlane = random.randint(-300, 300)
            yPlane = random.randint(-169, 169)
            self.turtle_turtle.hideturtle()
            self.turtle_turtle.goto(xPlane, yPlane)
            self.turtle_turtle.showturtle()
            self.main_screen.ontimer(self.turtle_teleport, max(500, 1000 - (self.score * 50)))
        else:
            self.turtle_turtle.hideturtle()

    def gameover(self):
        """Oyun bittiğinde ekrana yazdırır"""
        self.turtle_turtle.hideturtle()
        self.turtle_counter.goto(-100, 0)
        self.turtle_counter.write("Game Over", font=("helvetica", 36, "bold"))
        self.turtle_endgame.showturtle()
