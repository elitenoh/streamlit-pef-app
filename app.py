import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

st.set_page_config(page_title="엑셀 기반 구조도", layout="wide")
st.title("📊 PEF 투자 구조도 (엑셀 연동)")

uploaded_file = st.file_uploader("📂 구조도 엑셀 파일 업로드", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    st.subheader("📋 업로드된 데이터")
    st.dataframe(df)

    # 그래프 만들기
    G = nx.DiGraph()
    for _, row in df.iterrows():
        G.add_edge(
            row["From"], row["To"],
            amount=row["Amount"],
            ownership=row["Ownership"],
            note=row["Note"]
        )

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
        st.subheader("🗺️ 자동 생성된 구조도")
        fig, ax = plt.subplots(figsize=(8, 5))
        pos = nx.spring_layout(G, seed=42)
        nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=12, arrowsize=20, font_weight='bold', ax=ax)
        edge_labels = {
            (u, v): f"{d['amount']}, {d['ownership']}" for u, v, d in G.edges(data=True)
        }
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, ax=ax)
        st.pyplot(fig)
