from manim import *

class Updaters(Scene):
    def construct(self):
        num = MathTex("-1")

        # use updater to track movement of num
        box = always_redraw(lambda: SurroundingRectangle(
            num, color=LIGHT_GREY, fill_opacity=0.5, fill_color=DARKER_GRAY, buff=1
        )
        )

        # use updater to track movement of box
        name = always_redraw(lambda: Text("Cherlie").next_to(box, DOWN, buff=0.25))

        self.play(Create(VGroup(num, box, name), run_time=3))

        self.play(num.animate().shift(LEFT*2), run_time=1)
        self.wait()
