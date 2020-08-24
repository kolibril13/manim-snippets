from manim import *


class Updater2(Scene):
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
        self.wait()
        self.play(dot.shift, UP)
        self.play(dot.shift, LEFT)
        self.wait()


from pathlib import Path

if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim   --custom_folders  -p  -i -m -c 'BLACK' --config_file 'my_config.cfg' " + script)
