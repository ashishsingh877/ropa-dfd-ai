from vsdx import VisioFile

def export_visio(nodes, edges):

    file = VisioFile()
    page = file.pages[0]

    shapes={}
    x=1
    y=8

    for n,t in nodes:

        shape = page.add_shape(
            master="Process",
            x=x,
            y=y,
            text=n
        )

        shapes[n]=shape
        x+=2

    for s,t in edges:
        if s in shapes and t in shapes:
            page.connect(shapes[s],shapes[t])

    path="dfd.vsdx"
    file.save(path)

    return path