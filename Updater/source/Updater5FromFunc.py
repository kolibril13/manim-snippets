from manim import *


class Updater5FromFunc(Scene):
    def construct(self):
        run_setting = {"run_time": 1, "rate_func": linear}
        tick_start = 0
        tick_end = 100
        val_tracker= ValueTracker(tick_start)
        dot_disp= Dot().scale(3).set_color(GREEN)
        self.add(dot_disp)
        def Tiny_Updater(dots,val_trackerX):
            def small_change2(mob):
                mob.move_to(DOWN * 0.01 * val_trackerX.get_value())
                print(val_trackerX.get_value())
                return mob
            return UpdateFromFunc(dots, small_change2)


        tick_start = 0
        tick_end = 100
        self.play(Tiny_Updater(dot_disp,val_tracker),val_tracker.set_value,tick_end,**run_setting)
        self.wait()
        tick_end = 200
        self.play(Tiny_Updater(dot_disp,val_tracker),val_tracker.set_value,tick_end,**run_setting)




from pathlib import Path

if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system( f"manim   --custom_folders --disable_caching -p -i  -m -c 'BLACK' --config_file 'my_config.cfg' " + script)
