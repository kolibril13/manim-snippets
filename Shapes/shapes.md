```python
class ShapesColors(Scene):
    def construct(self):
        color_template = [GREEN, BLUE]
        colors = color_gradient(color_template, 256)
        for num,co in enumerate(colors):
            self.add(Dot(color = co).shift(LEFT*2+RIGHT*0.02*num).scale(4))

```

![alt text](source/ShapesColors.png)