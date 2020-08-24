```python
class ParamFunc1(Scene):

    def func(self,t):
        return np.array((np.sin(2*t), np.sin(3*t),0))

    def construct(self):
        func=ParametricFunction(self.func, t_max=TAU, fill_opacity=0)
        self.add(func.scale(3))

```

![alt text](source/ParamFunc1.png)