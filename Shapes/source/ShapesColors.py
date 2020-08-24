from manim import *



class ShapesColors(Scene):
    def construct(self):
        color_template = [GREEN, BLUE]
        colors = color_gradient(color_template, 256)
        for num,co in enumerate(colors):
            self.add(Dot(color = co).shift(LEFT*2+RIGHT*0.02*num).scale(4))

from pathlib import Path
if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders -s -p -c 'BLACK' --config_file 'my_config.cfg' " + script )
