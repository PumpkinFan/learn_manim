"""
arrow pointing from rect to circle
"""

from manim import *

class Maths(Scene):
    def construct(self):

        c = Circle().to_edge(DOWN)
        r = Rectangle(height=3, width=2)

        # using getters
        arrow = always_redraw(  # updater to follow other object movements
            lambda: Line(start=r.get_center(), end=c.get_center()).add_tip()
            )

        self.play(Create(VGroup(r,c,arrow), run_time=0.5)) 

        self.wait()

        self.play(r.animate().to_edge(UR), c.animate().to_edge(DL))

        self.wait()