from manim import *

class Plot5TransformXX(GraphScene):
    CONFIG = {
        "y_min": 0,
        "y_max": 10    }
    def construct(self):
        self.setup_axes(animate=False)
        my_func = lambda x: np.sin(x)
        func_graph=self.get_graph(my_func)
        self.add(func_graph)
        self.wait()


from pathlib import Path

if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders  -p -c 'BLACK' --config_file 'my_config.cfg' " + script)
