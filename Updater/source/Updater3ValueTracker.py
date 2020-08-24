from manim import *


class Updater3ValueTracker(Scene):
    def construct(self):
        dot_disp = Dot().set_color(RED)
        self.add(dot_disp)

        tick_start = 1
        tick_end = 2
        val_tracker = ValueTracker(tick_start)

        def dot_updater(mob):
            mob.set_y(val_tracker.get_value())

        dot_disp.add_updater(dot_updater)
        self.play(val_tracker.set_value, tick_end, rate_func=linear)
        self.wait()


from pathlib import Path

if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim   --custom_folders  -p -i  -m -c 'BLACK' --config_file 'my_config.cfg' " + script)
