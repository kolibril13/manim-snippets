# Some manim Example snippets for the manim-community repo (8/2020)

* [Updater](Updater/updater.md)
* [Annotations](Annotations/annotate.md)

Translate manim3b1b import statements to manimcm scripts directly for bunch of files
```python
from pathlib import Path

example_dict = Path.cwd() 
all_py_files = example_dict.rglob('*.py')

text_to_search = "from manim import *"
replacement_text = "from manim import *"

for py_file in all_py_files:
    text = py_file.read_text()
    text = text.replace(text_to_search, replacement_text)
    py_file.write_text(text)
    print(py_file)
    
print("Done 1!")

text_to_search = "TexMobject"
replacement_text = "MathTex"

for py_file in all_py_files:
    text = py_file.read_text()
    text = text.replace(text_to_search, replacement_text)
    py_file.write_text(text)
    
print("Done 2!")
```
