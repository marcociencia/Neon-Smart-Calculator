import streamlit as st

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

# Função de Callback (roda imediatamente ao clicar)
def button_click(item):
    if item == 'C':
        st.session_state['expression'] = ''
    elif item == '=':
        try:
            # Substitui porcentagem por divisão por 100 para o eval funcionar
            expressao_formatada = st.session_state['expression'].replace('%', '/100')
            result = str(eval(expressao_formatada))
            st.session_state['expression'] = result
        except Exception:
            st.session_state['expression'] = 'Erro'
    elif item == '⌫':
        st.session_state['expression'] = st.session_state['expression'][:-1]
    else:
        # Se a tela mostrar erro, limpa antes de digitar o próximo
        if st.session_state['expression'] == 'Erro':
            st.session_state['expression'] = ''
        st.session_state['expression'] += str(item)

# Tela de exibição (Agora atualiza em tempo real!)
st.text_input("Display", st.session_state['expression'], key="display", disabled=True, label_visibility="collapsed")

st.write("") # Espaço extra

# Layout dos botões em colunas (Usando on_click e args)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button('C', on_click=button_click, args=('C',), use_container_width=True)
    st.button('7', on_click=button_click, args=('7',), use_container_width=True)
    st.button('4', on_click=button_click, args=('4',), use_container_width=True)
    st.button('1', on_click=button_click, args=('1',), use_container_width=True)
    st.button('0', on_click=button_click, args=('0',), use_container_width=True)

with col2:
    st.button('⌫', on_click=button_click, args=('⌫',), use_container_width=True)
    st.button('8', on_click=button_click, args=('8',), use_container_width=True)
    st.button('5', on_click=button_click, args=('5',), use_container_width=True)
    st.button('2', on_click=button_click, args=('2',), use_container_width=True)
    st.button('.', on_click=button_click, args=('.',), use_container_width=True)

with col3:
    st.button('%', on_click=button_click, args=('%',), use_container_width=True)
    st.button('9', on_click=button_click, args=('9',), use_container_width=True)
    st.button('6', on_click=button_click, args=('6',), use_container_width=True)
    st.button('3', on_click=button_click, args=('3',), use_container_width=True)
    st.button('=', on_click=button_click, args=('=',), type="primary", use_container_width=True)

with col4:
    st.button('/', on_click=button_click, args=('/',), use_container_width=True)
    st.button('*', on_click=button_click, args=('*',), use_container_width=True)
    st.button('-', on_click=button_click, args=('-',), use_container_width=True)
    st.button('+', on_click=button_click, args=('+',), use_container_width=True)