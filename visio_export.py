from vsdx import VisioFile
import shutil

def export_visio(nodes, edges):

    template = "visio_template.vsdx"
    output = "dfd.vsdx"

    shutil.copy(template, output)

    with VisioFile(output) as vis:

        page = vis.pages[0]

        shapes = {}

        x = 1
        y = 8

        for n, t in nodes:

            shape = page.add_shape(
                master="Process",
                x=x,
                y=y,
                text=n
            )

            shapes[n] = shape
            x += 2

        for s, t in edges:

            if s in shapes and t in shapes:
                page.connect(shapes[s], shapes[t])

    return output
