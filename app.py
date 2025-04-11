import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

st.title("🧠 PEF 투자 구조도 (단순 버전)")

G = nx.DiGraph()
G.add_edges_from([
    ("LP1", "Main Fund"),
    ("LP2", "Main Fund"),
    ("Main Fund", "SPC"),
    ("SPC", "Portfolio Company")
])

fig, ax = plt.subplots(figsize=(8, 5))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", arrowsize=20, font_size=12, font_weight='bold', ax=ax)
st.pyplot(fig)
