from manim import *

class Graphing(Scene):
    def construct(self):
        
        plane = NumberPlane(
            x_range=[-5,5,2], x_length=9, y_range=[0,25,4], y_length=8
            ).to_edge(DOWN)

        parab = plane.get_graph(lambda x: x**2, x_range=[-5,5], color=ORANGE)

        self.play(DrawBorderThenFill(plane))
        self.play(Create(parab))
        self.wait()
        