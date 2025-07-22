import streamlit as st
from eventos import registrar_evento

# ====== CONFIGURAÇÕES ======
st.set_page_config(page_title="Quiz Relacionamentos", layout='centered')

URL_WHATSAPP = "https://wa.me/5511970162258?text=Olá!%20Fiz%20o%20quiz%20e%20quero%20ajuda%20para%20transformar%20meus%20relacionamentos."
URL_EDUZZ = "https://pay.eduzz.com/SEULINKDECOMPRA"

# TAG/PIXEL
st.markdown("""
<script async src="https://www.googletagmanager.com/gtag/js?id=SEU_ID_GA4"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'SEU_ID_GA4');
</script>
""", unsafe_allow_html=True)


def centralizar_html(html):
    return f"""
        <div style='display:flex;justify-content:center;align-items:center;flex-direction:column;height:auto;width:100%;'>
        {html}
        </div>
    """


# UI - Imagem/Frase destaque
st.markdown("""
<div style='background:linear-gradient(135deg,#fbc2eb 0%,#a6c1ee 100%);
            padding:36px 18px 30px 18px;border-radius:15px;margin-bottom:16px;'>
    <img src="https://images.unsplash.com/photo-1519125323398-675f0ddb6308?auto=format&fit=crop&w=500&q=80"
    style="max-width:200px;border-radius:50%;display:block;margin:auto;">
    <h2 style='text-align:center;color:#b44673;margin-top:25px;margin-bottom:0;'>
            O que está te impedindo de ser feliz no no Amor?    </h2>
   
</div>
""", unsafe_allow_html=True)

perguntas = [
    "Você sente que sempre atrai os mesmos tipos de problemas nos seus relacionamentos, mesmo quando muda de parceiro?",
    "Já teve a sensação de merecer mais compreensão, carinho e respeito do que recebe?",
    "Costuma guardar medos e mágoas do passado que te impedem de se entregar a um novo amor?",
    "Gostaria de transformar suas relações e encontrar sua alma gêmea, mas não sabe por onde começar?"
]

if 'etapa' not in st.session_state:
    st.session_state['etapa'] = 0
if 'respostas' not in st.session_state:
    st.session_state['respostas'] = []
if 'eventos' not in st.session_state:
    st.session_state['eventos'] = []

etapa = st.session_state['etapa']

if etapa < len(perguntas):
    st.markdown(centralizar_html(
        f"<div style='background:#fffbe5;padding:34px 22px 24px 22px;border-radius:12px;margin-bottom:12px;"
        f"box-shadow:0 3px 16px #e5e3eb52;'>"
        f"<h3 style='text-align:center;color:#4a224f;margin-bottom:16px;'>Pergunta {etapa + 1} de {len(perguntas)}</h3>"
        f"<p style='font-size:1.15em;text-align:center;color:#673a5e;font-weight:bold;margin-bottom:22px;'>"
        f"{perguntas[etapa]}</p></div>"
    ), unsafe_allow_html=True)

    resposta = st.radio(
        label="Escolha Sim ou Não",
        options=["Sim", "Não"],
        key=f"quiz_radio_{etapa}",
        index=0,
        horizontal=True,
        label_visibility="collapsed"
    )
    if st.button("Próxima", key=f"btn_proxima_{etapa}"):
        st.session_state['respostas'].append(resposta)
        registrar_evento(st.session_state, "respondeu_pergunta", resposta)
        st.session_state['etapa'] += 1
        st.rerun()

else:
    # Mensagem final
    st.markdown(centralizar_html(
        """
        <div style='background:linear-gradient(120deg,#fcdffb 0%,#c2ece9 100%);
                    padding:32px 20px 24px 20px;border-radius:15px;box-shadow:0 3px 22px #c4aed834;'>
            <h2 style='color:#b44673;text-align:center;margin-bottom:12px;margin-top:0;'>
                Você não precisa enfrentar esses desafios sozinho.
            </h2>
            <p style='font-size:1.23em;text-align:center;color:#32203c;margin-bottom:28px;'>
                Você merece mais. Cure sua história de amor!
            </p>
        </div>
        """), unsafe_allow_html=True)

    # Botões só aparecem aqui, após quiz finalizado
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <style>
        .btn-whatsapp {{
            display: block;
            width: 100%;
            background: linear-gradient(135deg, #fbc2eb, #a6c1ee);
            color: #4a224f;
            padding: 16px 0;
            border-radius: 12px;
            font-size: 1.1em;
            font-weight: 600;
            text-align: center;
            text-decoration: none !important;
            box-shadow: 0 4px 12px #fbc2ea;
            cursor: pointer;
            transition: filter 0.3s ease;
            user-select: none;
        }}
        .btn-whatsapp:hover {{
            filter: brightness(85%);
        }}
        </style>
        <a href="{URL_WHATSAPP}" target="_blank" class="btn-whatsapp" id="btn-whatsapp">
            Quero conversar com a Marta Neris
        </a>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown(f"""
        <style>
        .btn-eduzz {{
            display: block;
            width: 100%;
            background: linear-gradient(135deg, #fbc2eb, #a6c1ee);
            color: #4a224f;
            padding: 16px 0;
            border-radius: 12px;
            font-size: 1.1em;
            font-weight: 600;
            text-align: center;
            text-decoration: none !important;
            box-shadow: 0 4px 12px #fbc2ea;
            cursor: pointer;
            transition: filter 0.3s ease;
            user-select: none;;
        }}
        .btn-eduzz:hover {{
            filter: brightness(85%);
        }}
        .btn-eduzz span {{
            display: block;
            font-size: 0.95em;
            font-weight: 400;
            margin-top: 4px;
            color: #eee;
        }}
        </style>
        <a href="{URL_EDUZZ}" target="_blank" class="btn-eduzz" id="btn-eduzz">
            Quero garantir Minha Vaga na Eduzz
            <span>por 12x de R$19,70</span>
        </a>
        """, unsafe_allow_html=True)
        
