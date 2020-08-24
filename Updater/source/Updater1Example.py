from manim import *


class Updater1Example(Scene):
    def construct(self):
        curve_reference = Line(ORIGIN, LEFT).set_color(GREEN)
        self.add(curve_reference)

        def update_curve(mob, dt):
            mob.rotate_about_origin(dt)

        def update_curve_back(mob, dt):
            mob.rotate_about_origin(-dt)

        curve2 = Line(ORIGIN, LEFT)
        curve2.add_updater(update_curve)
        self.add(curve_reference, curve2)
        self.wait(PI / 2)

        curve2.remove_updater(update_curve)
        curve2.add_updater(update_curve_back)
        self.wait(PI / 2)



from pathlib import Path

if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim   --custom_folders  -p -i  -m -c 'BLACK' --config_file 'my_config.cfg' " + script)
