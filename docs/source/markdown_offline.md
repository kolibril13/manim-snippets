## Shapes & Geometrie
```python
class ShapeExample1(Scene):
    def construct(self):
        dot = Dot()
        self.add(dot)
```
![](./_static/image_test/ShapeExample1.png)


```python
class ShapeExample2(Scene):
    def construct(self):
        circ = Circle()
        self.add(circ)
```
![](./_static/image_test/ShapeExample2.png)



```python
class ShapeExample3(Scene):
    def construct(self):
        sq = Square()
        self.add(sq)
```
![](./_static/image_test/ShapeExample3.png)

```python
class ShapeExample4(Scene):
    def construct(self):
        rect = Rectangle(height=2, width=4)
        self.add(rect)
```
![](./_static/image_test/ShapeExample4.png)
