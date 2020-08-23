## Shapes & Geometrie
```python
class ShapeExample1(Scene):
    def construct(self):
        dot = Dot()
        self.add(dot)
```
![alt text](https://raw.githubusercontent.com/kolibril13/manim-snippets/master/Shapes-Geometrie/ShapeExample1.png)


```python
class ShapeExample2(Scene):
    def construct(self):
        circ = Circle()
        self.add(circ)
```
![alt text](https://raw.githubusercontent.com/kolibril13/manim-snippets/master/Shapes-Geometrie/ShapeExample2.png)



```python
class ShapeExample3(Scene):
    def construct(self):
        sq = Square()
        self.add(sq)
```
![alt text](https://raw.githubusercontent.com/kolibril13/manim-snippets/master/Shapes-Geometrie/ShapeExample3.png)

```python
class ShapeExample4(Scene):
    def construct(self):
        rect = Rectangle(height=2, width=4)
        self.add(rect)
```
![alt text](https://raw.githubusercontent.com/kolibril13/manim-snippets/master/Shapes-Geometrie/ShapeExample4.png)
