
import streamlit as st
import random
import time
import pandas as pd
import base64

st.set_page_config(page_title="Painel Hospitalar Completo", page_icon="🏥", layout="wide")

def play_alert():
    sound_file = open("alerta.mp3", "rb")
    sound_bytes = sound_file.read()
    b64 = base64.b64encode(sound_bytes).decode()
    md = f"""
    <audio autoplay="true">
    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """
    st.markdown(md, unsafe_allow_html=True)

st.title('🏥 Painel de Monitoramento Hospitalar - Ambiente Controlado')

st.markdown("""
> Monitoramento em tempo real de **temperatura**, **umidade** e **pressão atmosférica** em setores críticos.  
> Faixas de segurança:
- Temperatura: **19°C a 21°C**
- Umidade: **45% a 55%**
- Pressão: **1010 a 1020 hPa**
""")

setores = ["Oncologia 1", "Oncologia 2", "Quimioterapia"]
placeholder = st.empty()

col1, col2 = st.columns(2)
start = col1.button("▶️ Iniciar Monitoramento")
stop = col2.button("⏹️ Parar Monitoramento")

historicos = {
    setor: {
        "temperatura": [round(random.uniform(18.0, 22.5), 1) for _ in range(20)],
        "umidade": [round(random.uniform(40.0, 60.0), 1) for _ in range(20)],
        "pressao": [round(random.uniform(1005.0, 1025.0), 1) for _ in range(20)],
    }
    for setor in setores
}

executando = start

while executando:
    alerta_disparado = False

    for setor in setores:
        nova_temp = round(random.uniform(18.0, 22.5), 1)
        nova_umidade = round(random.uniform(40.0, 60.0), 1)
        nova_pressao = round(random.uniform(1005.0, 1025.0), 1)

        historicos[setor]["temperatura"].append(nova_temp)
        historicos[setor]["umidade"].append(nova_umidade)
        historicos[setor]["pressao"].append(nova_pressao)

        for key in historicos[setor]:
            historicos[setor][key] = historicos[setor][key][-20:]

    with placeholder.container():
        st.markdown("---")
        st.subheader("📊 Indicadores por Setor")

        for setor in setores:
            st.markdown(f"### 🏷️ {setor}")
            cols = st.columns(3)

            temp = historicos[setor]["temperatura"][-1]
            umi = historicos[setor]["umidade"][-1]
            press = historicos[setor]["pressao"][-1]

            # Temperatura
            with cols[0]:
                st.metric("🌡️ Temperatura (°C)", f"{temp}")
                bar = st.progress(min(max((temp - 18) / 5, 0), 1))
                if not 19.0 <= temp <= 21.0:
                    st.error("⚠️ Fora da faixa segura")
                    alerta_disparado = True
                else:
                    st.success("✅ Ok")

            # Umidade
            with cols[1]:
                st.metric("💧 Umidade (%)", f"{umi}")
                bar = st.progress(min(max((umi - 40) / 20, 0), 1))
                if not 45.0 <= umi <= 55.0:
                    st.error("⚠️ Fora da faixa segura")
                    alerta_disparado = True
                else:
                    st.success("✅ Ok")

            # Pressão
            with cols[2]:
                st.metric("🧭 Pressão (hPa)", f"{press}")
                bar = st.progress(min(max((press - 1005) / 20, 0), 1))
                if not 1010.0 <= press <= 1020.0:
                    st.error("⚠️ Fora da faixa segura")
                    alerta_disparado = True
                else:
                    st.success("✅ Ok")

        st.markdown("---")
        st.subheader("📈 Gráficos Históricos por Setor")

        for setor in setores:
            st.markdown(f"#### {setor}")
            st.line_chart(pd.DataFrame(historicos[setor]))

        st.caption("Simulação de ambiente hospitalar com sensores de temperatura, umidade e pressão.")

    if alerta_disparado:
        play_alert()

    time.sleep(2)

    if stop:
        break
