from manim import *


class Hi4425(Scene):
    def construct(self):
        dot = Dot().set_color(BLUE)
        self.add(dot)
        self.wait(1)
#end

from pathlib import Path
if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    project_folder =  "/home/jan-hendrik/projects/manim-snippets/"

    destination_img_vid = project_folder + "docs/source"
    img_vid = ""
    markdown_path = project_folder + "docs/source/md1.md"

    # manipulating the config file
    config_file = "/home/jan-hendrik/.config/JetBrains/PyCharm2020.2/scratches/my_config_docs.cfg"
    lines = open(config_file).read().splitlines()
    lines[155] = f"video_dir =  {destination_img_vid}"
    lines[156] = f"images_dir = {destination_img_vid}"
    open(config_file, 'w').write('\n'.join(lines))
    os.system(f"manim  -l --custom_folders  -p {img_vid} -c 'BLACK' --config_file {config_file} " + script)
    file_path  = open("/home/jan-hendrik/projects/manim-snippets/filepath.txt").read()
    file_path = "" + file_path[54:]
    # extracting the python-code-scene
    script_cont = open(script).read().splitlines()
    print(script_cont)
    start = int(*[script_cont.index(l) for l in script_cont[0:5] if l.startswith('class')])
    end = int(*[script_cont.index(l) for l in script_cont if l.startswith('#end')])

    # making the new markdown file
    if img_vid == "-s":
        image_loc = f"![]({file_path})"
        markdown = ["```py", *script_cont[start:end], "```", image_loc, "\n"]
        open(markdown_path, "a").write('\n'.join(markdown))
    if img_vid == "":
        s = f"""<video width="560" height="315" controls>
<source src="{file_path}" type="video/mp4">
</video> """.splitlines()
        markdown = ["```py", *script_cont[start:end], "```", *s]
        open(markdown_path, "a").write('\n'.join(markdown))