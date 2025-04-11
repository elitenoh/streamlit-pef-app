import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

st.set_page_config(page_title="PEF 구조도 시각화", layout="wide")
st.title("🗺️ PEF 투자 구조도")

# 투자 구조 + 투자금액/지분율 정보
G = nx.DiGraph()
edges = [
    ("LP1", "Main Fund", {"amount": "100억", "ownership": "50%"}),
    ("LP2", "Main Fund", {"amount": "100억", "ownership": "50%"}),
    ("Main Fund", "SPC", {"amount": "200억", "ownership": "100%"}),
    ("SPC", "Portfolio Company", {"amount": "200억", "ownership": "100%"})
]

G.add_edges_from(edges)

# 시각화
fig, ax = plt.subplots(figsize=(10, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=12, arrowsize=20, font_weight='bold', ax=ax)

# 엣지 라벨: 투자금 + 지분율
edge_labels = {
    (u, v): f"{d['amount']}, {d['ownership']}" for u, v, d in G.edges(data=True)
}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, ax=ax)

st.pyplot(fig)
