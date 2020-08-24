from manim import *

class Updater1(Scene):
    def construct(self):
        red_dot = Dot(radius= 0.3, color= RED)
        white_dot = Dot(point=LEFT)
        self.add(red_dot)
        white_dot.move_to(red_dot.get_center()+RIGHT)
        white_dot.target_cent= white_dot.get_center()
        def update_red_dot(mob,dt):
            #mob.rotate(angle= -0.01,about_point= ORIGIN)
            mob.shift(RIGHT*dt*1) #### CHANGE A
        def update_white_dot_min(mob,dt):
            if mob.time > 1:
                mob.time=0
                mob.move_to(red_dot.get_center()+RIGHT)
                mob.rotate(np.random.uniform(-PI,PI) ,about_point= red_dot.get_center())
                mob.target_cent=mob.get_center()
                mob.move_to(red_dot.get_center())
            mob.shift(RIGHT*dt*1) #### CHANGE B
            point= red_dot.get_center() + (mob.target_cent- red_dot.get_center())*mob.time
            mob.move_to(point)
            mob.time += 0.1
        white_dot.time=0
        red_dot.add_updater(update_red_dot)
        white_dot.add_updater(update_white_dot_min)
        self.add(red_dot)
        self.add(white_dot)
        self.wait(5)

from pathlib import Path

if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim  -m --custom_folders  -p  --config_file 'my_config.cfg' " + script)
