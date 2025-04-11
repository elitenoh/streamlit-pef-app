import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

st.set_page_config(page_title="PEF 구조도", layout="wide")
st.title("🗺️ PEF 투자 구조도 + 상세 정보")

# 구조 정의
G = nx.DiGraph()
edges = [
    ("LP1", "Main Fund", {"amount": "100억", "ownership": "50%", "note": "기관 출자자"}),
    ("LP2", "Main Fund", {"amount": "100억", "ownership": "50%", "note": "개인 출자자"}),
    ("Main Fund", "SPC", {"amount": "200억", "ownership": "100%", "note": "전액 출자"}),
    ("SPC", "Portfolio Company", {"amount": "200억", "ownership": "100%", "note": "자회사 지분 보유"})
]
G.add_edges_from(edges)

# Streamlit layout
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("🔎 노드 선택")
    selected_node = st.selectbox("노드를 선택하세요", sorted(G.nodes()))

    st.subheader("📄 상세 정보")
    info = []

    for u, v, d in G.edges(data=True):
        if selected_node == u:
            info.append(f"➡️ {u} → {v}: {d['amount']} / {d['ownership']} ({d['note']})")
        elif selected_node == v:
            info.append(f"⬅️ {u} → {v}: {d['amount']} / {d['ownership']} ({d['note']})")

    if info:
        for line in info:
            st.markdown(f"- {line}")
    else:
        st.markdown("ℹ️ 해당 노드는 연결된 정보가 없습니다.")

with col2:
    st.subheader("📌 투자 구조도")
    fig, ax = plt.subplots(figsize=(8, 5))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=12, arrowsize=20, font_weight='bold', ax=ax)

    edge_labels = {
        (u, v): f"{d['amount']}, {d['ownership']}" for u, v, d in G.edges(data=True)
    }
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, ax=ax)
    st.pyplot(fig)
