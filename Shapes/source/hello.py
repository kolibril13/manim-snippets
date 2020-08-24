from manim import *

class Test1(Scene):
    def construct(self):
        dot = Dot().set_color(BLUE)
        self.add(dot)
        self.wait(1)

from pathlib import Path
if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders -s -p -c 'BLACK' --config_file 'my_config.cfg' " + script )
