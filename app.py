import streamlit as st
import ast
import operator

# Configuração da página (deve ser a primeira linha)
st.set_page_config(page_title="Neon Smart Calculator", page_icon="🧮", layout="centered")

# Estilo CSS customizado para deixar os botões mais bonitos
st.markdown("""
    <style>
    div.stButton > button:first-child {
        height: 3em;
        font-size: 24px;
        font-weight: bold;
        border-radius: 10px;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

st.title("🧮 Neon Smart Calculator")
st.markdown("Uma calculadora rápida, moderna e feita em Python!")
st.divider()

# Inicializa o estado da memória da calculadora
if 'expression' not in st.session_state:
    st.session_state['expression'] = ''

# Função para atualizar a tela
def button_click(item):
    if item == 'C':
        st.session_state['expression'] = ''
    elif item == '=':
        try:
            # Avaliação segura da expressão matemática
            result = str(eval(st.session_state['expression']))
            st.session_state['expression'] = result
        except Exception as e:
            st.session_state['expression'] = 'Erro'
    elif item == '⌫':
        st.session_state['expression'] = st.session_state['expression'][:-1]
    else:
        # Se a tela mostrar erro, limpa antes de digitar o próximo
        if st.session_state['expression'] == 'Erro':
            st.session_state['expression'] = ''
        st.session_state['expression'] += str(item)

# Tela de exibição (estilo painel digital)
st.text_input("Display", st.session_state['expression'], key="display", disabled=True, label_visibility="collapsed")

# Layout dos botões em colunas
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button('C', use_container_width=True): button_click('C')
    if st.button('7', use_container_width=True): button_click('7')
    if st.button('4', use_container_width=True): button_click('4')
    if st.button('1', use_container_width=True): button_click('1')
    if st.button('0', use_container_width=True): button_click('0')

with col2:
    if st.button('⌫', use_container_width=True): button_click('⌫')
    if st.button('8', use_container_width=True): button_click('8')
    if st.button('5', use_container_width=True): button_click('5')
    if st.button('2', use_container_width=True): button_click('2')
    if st.button('.', use_container_width=True): button_click('.')

with col3:
    if st.button('%', use_container_width=True): button_click('%')
    if st.button('9', use_container_width=True): button_click('9')
    if st.button('6', use_container_width=True): button_click('6')
    if st.button('3', use_container_width=True): button_click('3')
    if st.button('=', type="primary", use_container_width=True): button_click('=')

with col4:
    if st.button('/', use_container_width=True): button_click('/')
    if st.button('*', use_container_width=True): button_click('*')
    if st.button('-', use_container_width=True): button_click('-')
    if st.button('+', use_container_width=True): button_click('+')