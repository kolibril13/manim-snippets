from manim import *


class Plot3DataPoints(GraphScene):
    CONFIG = {
        "y_axis_label": r"Concentration[$\%$]",
        "x_axis_label": "Time [s]",
        }

    def construct(self):
        data = [1, 2, 2, 4, 4, 1, 3]
        self.setup_axes(animate=True)
        for time, dat in enumerate(data):
            dot = Dot().move_to(self.coords_to_point(time, dat))
            self.add(dot)
            self.wait(1)
            print(time)
        self.wait()


from pathlib import Path

if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders -s -p -c 'BLACK' --config_file 'my_config.cfg' " + script)
