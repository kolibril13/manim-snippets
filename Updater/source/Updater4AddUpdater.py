from manim import *


class Updater4AddUpdater(Scene):
    def construct(self):
        dot = Dot()

        def func(t):
            return np.array((np.sin(2 * t), np.sin(3 * t), 0))

        func = ParametricFunction(func, t_max=TAU, fill_opacity=0)
        func.scale(2)
        new_func = CurvesAsSubmobjects(func)
        new_func.set_color_by_gradient(BLUE, RED)
        dot.add_updater(lambda m: m.move_to(func.get_end()))
        func.fade(1)
        self.add(dot)
        self.play(ShowCreation(new_func), run_time=5)
        self.wait()


from pathlib import Path

if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(
        f"manim   --custom_folders --disable_caching -p -i  -m -c 'BLACK' --config_file 'my_config.cfg' " + script)
