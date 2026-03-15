import xml.etree.ElementTree as ET
import uuid

def export_drawio(nodes, edges):

    root = ET.Element("mxfile")
    diagram = ET.SubElement(root,"diagram")
    graph = ET.SubElement(diagram,"mxGraphModel")
    r = ET.SubElement(graph,"root")

    ET.SubElement(r,"mxCell",{"id":"0"})
    ET.SubElement(r,"mxCell",{"id":"1","parent":"0"})

    node_ids={}
    x=100
    y=100

    for n,t in nodes:

        nid=str(uuid.uuid4())

        cell=ET.SubElement(r,"mxCell",{
            "id":nid,
            "value":n,
            "vertex":"1",
            "parent":"1"
        })

        ET.SubElement(cell,"mxGeometry",{
            "x":str(x),
            "y":str(y),
            "width":"160",
            "height":"60",
            "as":"geometry"
        })

        node_ids[n]=nid
        x+=220

    for s,t in edges:

        ET.SubElement(r,"mxCell",{
            "id":str(uuid.uuid4()),
            "edge":"1",
            "source":node_ids.get(s,""),
            "target":node_ids.get(t,""),
            "parent":"1"
        })

    return ET.tostring(root)