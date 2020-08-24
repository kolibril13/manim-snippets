from manim import *

class UpdaterExample(Scene):
    def construct(self):
        path = VMobject()
        dot = Dot()
        path.set_points_as_corners([dot.get_center(), dot.get_center()])

        def update_path(path):
            previus_path = path.copy()
            previus_path.add_points_as_corners([dot.get_center()])
            path.become(previus_path)

        path.add_updater(update_path)
        self.add(path, dot)
        self.play(Rotating(dot, radians=PI, about_point=RIGHT, run_time=2))
        self.play(dot.shift, UP)
        self.play(dot.shift, LEFT)


from pathlib import Path
if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders -i -p -c 'BLACK' --config_file '/home/jan-hendrik/.config/JetBrains/PyCharm2020.2/scratches/my_config.cfg' " + script )
