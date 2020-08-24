from manim import *



class ParamFunc1(Scene):

    def func(self,t):
        return np.array((np.sin(2*t), np.sin(3*t),0))

    def construct(self):
        func=ParametricFunction(self.func, t_max=TAU, fill_opacity=0)
        self.add(func.scale(3))

from pathlib import Path
if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders -s -p -c 'BLACK' --config_file 'my_config.cfg' " + script )
