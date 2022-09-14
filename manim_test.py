print("smello world")

from manim import *

class Spam(Scene):
    def construct(self):
        
        name = Tex("ur mom").scale(5)

        sq = Square(side_length=1, fill_color=PURPLE, fill_opacity=0.8).to_corner(UL)
        
        self.play(Create(sq))
        self.play(Write(name))
        for i in range(4):
            self.play(name.animate(run_time=0.2).rotate(PI/2))
        self.wait()        
