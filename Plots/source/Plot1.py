from manim import *

class Plot1(GraphScene):
    def construct(self):
        self.setup_axes()
        my_func = lambda x: np.sin(x)
        func_graph=self.get_graph(my_func)
        self.add(func_graph)


from pathlib import Path
if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders -s -p -c 'BLACK' --config_file 'my_config.cfg' " + script )