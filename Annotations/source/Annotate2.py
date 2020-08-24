from manim import *

class Annotate2(Scene):
    def construct(self):
        sourunding_dot = Dot().scale(1.3).set_fill(color=BLACK).set_z_index(-1)
        innerdot = Dot().set_color(ORANGE)
        annotation_dot= VGroup(sourunding_dot,innerdot).scale(4)
        self.add(annotation_dot)
        self.wait()


from pathlib import Path
if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders -s -p -c 'WHITE' --config_file 'my_config.cfg' " + script )
