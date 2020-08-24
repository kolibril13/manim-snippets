from manim import *


class Plot6HeatDiagram(GraphScene):
    CONFIG = {
        "y_axis_label": r"T[$^\circ C$]",
        "x_axis_label": r"$\Delta Q$",
        "y_min": -8,
        "y_max": 30,
        "x_min": 0,
        "x_max": 40,
        "y_labeled_nums": np.arange(-5, 34, 5),
        "x_labeled_nums": np.arange(0, 40, 5),

    }

    def construct(self):
        data = [20, 0, 0, -5]
        x = [0, 8, 38, 39]
        print(x)
        self.setup_axes(animate=True)
        dot_collection = VGroup()
        for time, val in enumerate(data):
            dot = Dot().move_to(self.coords_to_point(x[time], val))
            self.add(dot)
            dot_collection.add(dot)
        l1 = Line(dot_collection[0].get_center(), dot_collection[1].get_center())
        l2 = Line(dot_collection[1].get_center(), dot_collection[2].get_center())
        l3 = Line(dot_collection[2].get_center(), dot_collection[3].get_center())
        self.add(l1, l2, l3)


from pathlib import Path

if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders -s -p -c 'BLACK' --config_file 'my_config.cfg' " + script)
