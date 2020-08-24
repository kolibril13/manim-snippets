
```python
class Updater1Example(Scene):
    def construct(self):
        curve_reference = Line(ORIGIN, LEFT).set_color(GREEN)
        self.add(curve_reference)

        def update_curve(mob, dt):
            mob.rotate_about_origin(dt)

        def update_curve_back(mob, dt):
            mob.rotate_about_origin(-dt)

        curve2 = Line(ORIGIN, LEFT)
        curve2.add_updater(update_curve)
        self.add(curve_reference, curve2)
        self.wait(PI / 2)

        curve2.remove_updater(update_curve)
        curve2.add_updater(update_curve_back)
        self.wait(PI / 2)
```

![alt text](source/Updater1Example.gif)

```python
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
```

![alt text](source/Updater2.gif)

```python
class Updater3ValueTracker(Scene):
    def construct(self):
        dot_disp = Dot().set_color(RED)
        self.add(dot_disp)

        tick_start = 1
        tick_end = 2
        val_tracker = ValueTracker(tick_start)

        def dot_updater(mob):
            mob.set_y(val_tracker.get_value())

        dot_disp.add_updater(dot_updater)
        self.play(val_tracker.set_value, tick_end, rate_func=linear)
        self.wait()
```

![alt text](source/Updater3ValueTracker.gif)

```python
class Updater3Color(Scene):
    def construct(self):
        tick_start = 1.0
        tick_end = 2.0
        val_tracker = ValueTracker(tick_start)
        square = Square(fill_opacity=1).set_stroke(width=0)
        self.add(square)
        num_colors = 1000
        cols = color_gradient([RED, WHITE, BLUE], num_colors)

        def col_uptater(mob):
            integ = int((val_tracker.get_value() - tick_start) / (tick_end - tick_start) * (num_colors - 1))
            mob.set_color(cols[integ])

        square.add_updater(col_uptater)
        self.play(val_tracker.set_value, tick_end, rate_func=linear, run_time=3)
```

![alt text](source/Updater3Color.gif)

```python
class Updater4AddUpdater(Scene):
    def construct(self):
        dot = Dot()

        def func(t):
            return np.array((np.sin(2 * t), np.sin(3 * t), 0))

        func = ParametricFunction(func, t_max=TAU, fill_opacity=0)
        func.scale(2)
        new_func = CurvesAsSubmobjects(func)
        new_func.set_color_by_gradient(BLUE, RED)
        dot.add_updater(lambda m: m.move_to(func.get_end()))
        func.fade(1)
        self.add(dot)
        self.play(ShowCreation(new_func), run_time=5)
        self.wait()

```
![alt text](source/Updater4AddUpdater.gif)

```python
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
```

![alt text](source/Updater5FromFunc.gif)


```python
class Updater6FromFunc(Scene): #Two Options to update a scene one more nested, one more explicit
    def construct(self):
        tick_start=0
        tick_end=100
        val_tracker= ValueTracker(tick_start)
        dot_disp= Dot()
        self.add(dot_disp)
        # version A
        def small_change(dot_disp,val_tracker):
            dot_disp.shift(UP * 0.001 * val_tracker.get_value())
            print(dot_disp.get_center()[1])
            return dot_disp
        self.play(
            UpdateFromFunc(
                dot_disp,
                lambda mob: mob.become(small_change(dot_disp,val_tracker))),
            val_tracker.set_value,tick_end, rate_func= linear
        )
        #  version B
        val_tracker= ValueTracker(tick_start)
        def Tiny_Updater(dots,val_trackerX):
            def small_change2(mob):
                mob.shift(DOWN * 0.001 * val_trackerX.get_value())
                return mob
            return UpdateFromFunc(dots, small_change2)
        self.play(Tiny_Updater(dot_disp,val_tracker),val_tracker.set_value,tick_end)
        self.wait()
```

![alt text](source/Updater6FromFunc.gif)