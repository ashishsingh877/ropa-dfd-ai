def build_graph(data):

    nodes = []
    edges = []

    for e in data.get("entities", []):
        nodes.append((e,"entity"))

    for p in data.get("processes", []):
        nodes.append((p,"process"))

    for d in data.get("datastores", []):
        nodes.append((d,"datastore"))

    for f in data.get("flows", []):
        edges.append((f[0],f[1]))

    return nodes, edges