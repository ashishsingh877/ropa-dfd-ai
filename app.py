import streamlit as st

from ropa_parser import parse_ropa
from groq_client import analyze_ropa
from graph_builder import build_graph
from graphviz_renderer import render_dfd
from drawio_export import export_drawio
from visio_export import export_visio
from ppt_export import export_ppt

st.title("RoPA → Consulting Style DFD Generator")

file = st.file_uploader("Upload RoPA Excel", type=["xlsx"])

if file:
    ropa_text = parse_ropa(file)

    st.info("Analyzing RoPA using Groq AI...")
    data = analyze_ropa(ropa_text)

    nodes, edges = build_graph(data)

    diagram = render_dfd(nodes, edges)
    st.graphviz_chart(diagram)

    drawio_data = export_drawio(nodes, edges)
    visio_path = export_visio(nodes, edges)
    ppt_path = export_ppt(nodes, edges)

    st.download_button("Download Draw.io", drawio_data, "dfd.drawio")

    with open(visio_path, "rb") as f:
        st.download_button("Download Visio", f, "dfd.vsdx")

    with open(ppt_path, "rb") as f:
        st.download_button("Download PowerPoint", f, "dfd.pptx")
