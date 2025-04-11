import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

st.set_page_config(page_title="PEF 구조도", layout="wide")
st.title("🗺️ PEF 투자 구조도 시각화")

# 투자 구조 정의
G = nx.DiGraph()
G.add_edges_from([
    ("LP1", "Main Fund"),
    ("LP2", "Main Fund"),
    ("Main Fund", "SPC"),
    ("SPC", "Portfolio Company")
])

# 시각화 설정 및 출력
fig, ax = plt.subplots(figsize=(10, 6))
pos = nx.spring_layout(G, seed=42)  # seed 고정 시 위치 안정적
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=12, arrowsize=20, font_weight='bold', ax=ax)
st.pyplot(fig)
