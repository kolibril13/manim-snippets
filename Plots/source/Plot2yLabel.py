from manim import *


class Plot2yLabel(GraphScene):
    CONFIG = {
        "y_min": 0,
        "y_max": 100,
        "y_tick_frequency": 10,
        "y_labeled_nums": np.arange(0, 100, 10)
    }

    def construct(self):
        self.setup_axes(animate=True)
        dot = Dot()
        dot.move_to(self.coords_to_point(PI / 2, 20))
        my_func = lambda x: 20 * np.sin(x)
        func_graph = self.get_graph(my_func)
        self.add(func_graph)
        self.add(dot)


from pathlib import Path

if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders -s -p -c 'BLACK' --config_file 'my_config.cfg' " + script)
