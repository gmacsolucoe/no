
import streamlit as st
import time

st.set_page_config(page_title="Assistente: GMAC", layout="wide")

st.markdown(""" 
    <style>
    body {
        background-color: #f7f8fa;
    }
    .chatbox {
        max-width: 1080px;
        margin: auto;
        padding: 20px;
    }
    .bubble {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 14px;
        padding: 16px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.06);
        font-family: 'Segoe UI', sans-serif;
        animation: fadein 0.5s ease-in;
    }
    .author {
        font-weight: 600;
        color: #1F3645;
        margin-bottom: 12px;
        font-size: 17px;
    }
    .tabela {
        width: 100%;
        border-collapse: collapse;
        font-size: 14px;
    }
    .tabela th, .tabela td {
        border: 1px solid #e6e6e6;
        padding: 8px 10px;
        text-align: center;
    }
    .tabela th {
        background-color: #f0f2f6;
        color: #1F3645;
        font-weight: 600;
    }
    .destaque {
        background-color: #fff4f0 !important;
        font-weight: bold;
        color: #9C0000;
    }
    @keyframes fadein {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    </style>
""", unsafe_allow_html=True)

aba = st.selectbox("Escolha o painel:", ["Frentes de Trabalho", "Atividades"], index=0)

if aba == "Frentes de Trabalho":
    headers = ["Frente", "Área", "Equipamentos principais", "Turno", "Supervisor", "Tec. Doc", "Qtd. Inspetores"]
    linhas = [
        ["1", "Caldeiras/Condensado", "B1-2230A, B1-2230B", "DIA", "Huggo Mello - 01", "Isabella - 01", "2"],
        ["1", "Caldeiras/Condensado", "B1-2230A, B1-2230B", "NOITE", "Adeildo - 01", "Miqueias - 01", "2"],
        ["2", "Oxidação", "Vasos e Trocadores", "DIA", "Expedito Souza - 02", "Adriano - 02", "5"],
        ["2", "Oxidação", "Vasos e Trocadores", "NOITE", "Serginho - 02", "Cristiano - 02", "5"],
        ["3", "Purificação/Tancagem", "Vasos, Trocador", "DIA", "Adalberto Saturno - 03", "Dayvson - 03", "5"],
        ["3", "Purificação/Tancagem", "Vasos, Trocador", "NOITE", "Gutemberg Rolim - 03", "Cristiano - 03", "5"],
        ["4", "ETA / Off Gás / Armazenamento PTA", "Tanques, Torres", "DIA", "Thiago - 04", "Rosemary - 04", "4"],
        ["4", "ETA / Off Gás / Armazenamento PTA", "Tanques, Torres", "NOITE", "Bruno Marques - 04", "Miqueias - 04", "4"]
    ]

    if 'highlight_frente' not in st.session_state:
        st.session_state.highlight_frente = 0
    st.session_state.highlight_frente = (st.session_state.highlight_frente + 1) % len(linhas)

    st.markdown("<div class='chatbox'><div class='bubble'><div class='author'>Assistente: GMAC</div>", unsafe_allow_html=True)

    tabela_html = "<table class='tabela'><tr>"
    tabela_html += "".join([f"<th>{col}</th>" for col in headers]) + "</tr>"

    for i, row in enumerate(linhas):
        row_class = "destaque" if i == st.session_state.highlight_frente else ""
        tabela_html += f"<tr>{''.join([f'<td class="{row_class}">{cell}</td>' for cell in row])}</tr>"

    tabela_html += "</table></div></div>"
    st.markdown(tabela_html, unsafe_allow_html=True)

    time.sleep(3)
    st.rerun()

elif aba == "Atividades":
    headers = ["ATIVIDADE", "Total Previsto", "Em Andamento", "Concluído", "Avanço"]
    atividades = [
        ["INSPEÇÃO VISUAL INTERNA", 55, 16, 16, "29,09%"],
        ["ESPAÇO CONFINADO", 39, 19, 13, "33,33%"],
        ["LP", 39, 16, 18, "46,15%"],
        ["PREPARAÇÃO DE PONTOS ME", 38, 13, 12, "31,58%"],
        ["INSPEÇÃO VISUAL EXTERNA", 37, 10, 15, "40,54%"],
        ["ME", 35, 8, 15, "42,86%"],
        ["IRIS/CP", 23, 7, 7, "30,43%"],
        ["PM", 19, 9, 5, "26,32%"],
        ["REPLICA METALOGRAFICA", 19, 7, 6, "31,58%"]
    ]

    if 'highlight_atividade' not in st.session_state:
        st.session_state.highlight_atividade = 0
    st.session_state.highlight_atividade = (st.session_state.highlight_atividade + 1) % len(atividades)

    st.markdown("<div class='chatbox'><div class='bubble'><div class='author'>Painel de Atividades</div>", unsafe_allow_html=True)

    tabela_html = "<table class='tabela'><tr>"
    tabela_html += "".join([f"<th>{col}</th>" for col in headers]) + "</tr>"

    for i, row in enumerate(atividades):
        row_class = "destaque" if i == st.session_state.highlight_atividade else ""
        tabela_html += f"<tr>{''.join([f'<td class="{row_class}">{cell}</td>' for cell in row])}</tr>"

    tabela_html += "</table></div></div>"
    st.markdown(tabela_html, unsafe_allow_html=True)

    time.sleep(3)
    st.rerun()
