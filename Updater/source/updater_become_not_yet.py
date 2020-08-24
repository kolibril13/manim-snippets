from manim import *

class Updater1(Scene):
    def get_dot(self,num):
        print(num)
        return Dot().shift(LEFT*0.01 *num)
    def construct(self):
        tick_start=0
        tick_end=100
        val_tracker= ValueTracker(tick_start)
        dot_disp= self.get_dot(val_tracker.get_value())
        dot_disp.add_updater(lambda x: x.become(self.get_dot(val_tracker.get_value())))
        self.add(dot_disp)
        self.play(val_tracker.set_value, tick_end, rate_func= linear)
        self.wait()
from pathlib import Path
if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders  -p -c 'BLACK' --config_file 'my_config.cfg' " + script )
