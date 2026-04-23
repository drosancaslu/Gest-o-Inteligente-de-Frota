Gestão-Inteligente-de-Frota import streamlit as st
import google.generativeai as genai

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Portal de Inteligência Logística", layout="wide")

# ESTILO PERSONALIZADO (AZUL E CINZA)
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { background-color: #004a99; color: white; border-radius: 5px; }
    .sidebar .sidebar-content { background-image: linear-gradient(#004a99, #002b5c); color: white; }
    </style>
    """, unsafe_allow_html=True)

# SEGURANÇA: CHAVE DE ACESSO SIMPLES
if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False

if not st.session_state["autenticado"]:
    st.title("Acesso Restrito - Consultoria IA")
    senha = st.text_input("Introduza a Chave de Acesso:", type="password")
    if st.button("Entrar"):
        if senha == "SUA_SENHA_AQUI": # Altere para a senha que quer dar ao cliente
            st.session_state["autenticado"] = True
            st.rerun()
    st.stop()

# CONFIGURAÇÃO DA API DO GEMINI
# Aqui você pode deixar fixo ou pedir para inserir na barra lateral
API_KEY = "SUA_API_KEY_DO_GOOGLE_STUDIO"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# MENU LATERAL
st.sidebar.title("MENU ESTRATÉGICO")
opcao = st.sidebar.radio("Navegação:", ["Dashboard de Análise", "Diagnóstico de Frota", "Copiloto IA"])

st.sidebar.markdown("---")
st.sidebar.info("Plataforma de Inteligência Operacional v1.0")

# --- ABA 1: DASHBOARD ---
if opcao == "Dashboard de Análise":
    st.title("📊 Painel de Análise Estratégica")
    st.write("Suba os dados da operação (CSV/TXT) para identificar anomalias financeiras.")
    
    upload = st.file_uploader("Enviar Relatório Operacional", type=['csv', 'txt'])
    if upload:
        dados = upload.read().decode("utf-8")
        st.success("Dados carregados com sucesso!")
        if st.button("Gerar Insights"):
            response = model.generate_content(f"Analise estes dados de transporte e aponte 3 pontos de economia: {dados}")
            st.markdown(f"### Insights da IA:\n{response.text}")

# --- ABA 2: DIAGNÓSTICO DE FROTA ---
elif opcao == "Diagnóstico de Frota":
    st.title("🚌 Diagnóstico Preditivo de Frota")
    problema = st.text_area("Descreva o sintoma ou anomalia do veículo:")
    if st.button("Analisar Risco"):
        response = model.generate_content(f"Com base neste sintoma de autocarro, qual a urgência de manutenção e custo estimado? {problema}")
        st.info(response.text)

# --- ABA 3: COPILOTO IA ---
elif opcao == "Copiloto IA":
    st.title("🤖 Copiloto de Gestão 24/7")
    pergunta = st.chat_input("Pergunte algo sobre a estratégia da sua empresa...")
    if pergunta:
        st.write(f"**Você:** {pergunta}")
        response = model.generate_content(pergunta)
        st.write(f"**Assistente:** {response.text}")
