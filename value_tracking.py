from manim import *

class Vcard(Scene):
    def construct(self):

        k = ValueTracker(4.20)

        n = always_redraw(
            lambda: DecimalNumber().set_value(k.get_value())
            )

        self.play(Write(n))

        self.play(k.animate(run_time=1).set_value(1453))

        self.wait()

        # self.play(k.animate().set_value(0), run_time=5, rate_func=linear)
        self.play(k.animate().set_value(0), run_time=5, rate_func=smooth)
        