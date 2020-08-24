from manim import *

class Annotate1(Scene):
    def construct(self):
        num1 = TexMobject(r"{\large \textcircled{\small 1}} ").scale(2)
        num2 = TexMobject(r"{\large \textcircled{\small 2}} ").scale(1.5)
        num2.next_to(num1,DOWN)
        self.add(num1 ,num2)
        self.wait(1)


from pathlib import Path
if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders -s -p -c 'WHITE' --config_file 'my_config.cfg' " + script )
