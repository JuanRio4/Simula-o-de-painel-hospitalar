# 🏥 Projeto: Monitoramento Hospitalar de Temperatura

![Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-blue?logo=streamlit)

## 📋 Descrição
Este projeto simula o monitoramento de temperatura em setores críticos de um hospital oncológico.
Utilizando Python e Streamlit, construímos um painel interativo que alerta em tempo real caso a temperatura ultrapasse os limites de segurança estabelecidos (entre 19°C e 21°C).

---

## 🚑 Funcionalidades
- Monitoramento simultâneo de múltiplas salas:
  - Oncologia 1
  - Oncologia 2
  - Sala de Quimioterapia
- Gráficos históricos de temperatura em tempo real.
- Barras de progresso indicando estado de segurança.
- Alertas sonoros automáticos para temperaturas fora do padrão.
- Botões de Start/Stop para controle da simulação.

---

## 🛠️ Tecnologias Utilizadas
- Python 3.10+
- Streamlit
- Paho-MQTT
- Pandas
- Pydub
- Mosquitto (Broker MQTT)
- Docker
- Grafana + InfluxDB (opcional para visualização avançada)

---

## 📦 Como executar o projeto localmente

### 1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Instale as dependências:
```bash
pip install -r requirements.txt
```

### 3. Rode o aplicativo:
```bash
streamlit run app.py
```

---

## 🌎 Implantação na nuvem
Este projeto pode ser facilmente implantado gratuitamente usando o [Streamlit Community Cloud](https://streamlit.io/cloud).

---

## 📂 Estrutura dos Arquivos
```
📦 projeto-monitoramento-hospitalar
 ┣ 📜 app.py
 ┣ 📜 requirements.txt
 ┣ 📜 alerta.mp3
 ┣ 📜 README.md
```

---

## 🎯 Resumo Final
Este trabalho unifica conceitos de:
- Sistemas Distribuídos
- Comunicação em tempo real (MQTT)
- Visualização interativa (Streamlit)

Tornando o projeto uma POC prática, completa e com aplicações reais em IoT Hospitalar.

-------
