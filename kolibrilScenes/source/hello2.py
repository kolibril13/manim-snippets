from manim import *

class Test2(GraphScene):
    def construct(self):
        self.setup_axes(animate=False)
        def func_sin(x):
            return np.sin(x)
        func_graph=self.get_graph(func_sin)
        self.add(func_graph)
        self.wait()

from pathlib import Path

if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim   -l --custom_folders  -p  -c 'BLACK' --config_file 'my_config.cfg' " + script)
