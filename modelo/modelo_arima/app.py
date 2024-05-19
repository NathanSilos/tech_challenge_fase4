import streamlit as st
import joblib
from datetime import datetime, timedelta

st.markdown('<style>div[role="listbox"] ul{background-color: #6e42ad}; </style>', unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; '> Formulário para Predição do Preço do petróleo 🤑</h1>", unsafe_allow_html = True)

st.warning('Preencha o formulário com todos os dados e clique no botão **ENVIAR** no final da página.')


# Escreva a data de hoje
st.write("""### Data""")

# pegando numero de dias que vamos usar para prever
qtd = float(st.text_input('Daqui quantos dias daqui pra frente você quer saber o preço? (2024-05-13) Digite o número',0))

# Data atual em datetime
data = datetime.strptime('2024-05-13', '%Y-%m-%d')

# Calcula data futura que sera exibida
data_futura = data + timedelta(days = int(qtd))

# Ajusta o formato da data que sera exibida
data_futura = data_futura.strftime('%d/%m/%Y')

#Predições 
if st.button('Enviar'):
    # Realiza a predicao de acordo com o modelo
    arima_model = joblib.load('modelo/arima_model.joblib')
    final_pred = arima_model.forecast(steps=int(qtd))

    # Printa a resposta
    st.success(f'### Esta é a nossa previsão para a {data_futura}: U$ {round(final_pred.values[0],2)}! =D.')
    st.balloons()