from manim import *

class Plot3bGaussian(GraphScene):
    def construct(self):
        def gaussian(x):
            mu=3; sig= 1; amp=5
            return amp*np.exp( ( -1/2 * ( (x-mu)/sig)**2 ) )
        self.setup_axes()
        graph = self.get_graph(gaussian, x_min=-1, x_max=10, ).set_stroke(width=5)
        self.add(graph)


from pathlib import Path
if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders -s -p -c 'BLACK' --config_file 'my_config.cfg' " + script )