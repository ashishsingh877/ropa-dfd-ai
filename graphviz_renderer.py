from graphviz import Digraph

def render_dfd(nodes, edges):

    dot = Digraph(
        graph_attr={
            "rankdir":"LR",
            "splines":"ortho",
            "nodesep":"0.8",
            "ranksep":"1.2"
        }
    )

    for name, t in nodes:

        if t == "entity":
            dot.node(name, shape="box", style="filled", fillcolor="#FFE6CC")

        elif t == "process":
            dot.node(name, shape="rectangle")

        elif t == "datastore":
            dot.node(name, shape="cylinder", style="filled", fillcolor="#DAE8FC")

    for s,t in edges:
        dot.edge(s,t)

    return dot