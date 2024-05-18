# Trabalho do Tech Challenge - Fase 4

O objetivo do trabalho é: <b>

    1 - Criar um dashboard interativo com ferramentas a sua escolha.

    2 - Obrigatório trazer pelo menos 4 insights com o Dash.

    3 - Criar um modelo de Machine Learning para a previsão do preço do petróleo diariamente.

    4 - Criar um plano para fazer o deploy em produção do modelo.

    5 - Faça um MVP do seu modelo em produção no Streamlit.

</b>

# Primeira etapa

Para a criação do Dashboard, foi necessária a extratação dos dados de petróleo do site do ipea. Para agregar mais informações, realizei a consulta em outros dados também como:
IPCA, SELIC, cotação do dólar e Inflação Americana.

Dito isso, foi feito todo este processo utilizando o python no arquivo <b>"/extratacao_dos_dados/extracao_dados.ipynb" </b>

Neste arquivo se encontram todas as extratações, tratamentos e carregamentos (ETL). Ao final, foi gerada a base <b>"base_final.csv" </b> onde contem todas as informacoes unificadas em um unico local.

# Segunda etapa

Foi criado o dashboard com as informações extraídas acima na ferramenta Looker, do Google. Já possuo experiência com Tableau e Power BI, decidi utilizar esta para poder aprender uma ferramenta nova. Para acessar o Dash, acesse: 

    - https://lookerstudio.google.com/reporting/dbba5911-b1ee-4287-aaa8-4dbb56949e9e

O Dashboard, possui as visões comparativas no decorrer do tempo e de suas máximas de valores para cada um dos indicadores (Inclui dados apenas do primeiro dia de cada mês para podermos comparar todos os dados de igual para igual). Conforme o print abaixo:

![alt text](image-7.png)

Para selecionar uma período específico, basta ir na visão e clicar de acordo com o que deseja que todas as visões serão ajustadas de acordo. Como por exemplo, selecionando 01/04/2015 até 01/03/2016:

![alt text](image-8.png)

Abaixo segue quatro insights com as visões:

    - Podemos observar que em 01/06/2022, tivemos um pico onde o barril petroleo chegou a U$ 122,20 , quase chegando ao seu preço máximo da história em 01/07/2006 onde foi U$ 139,38 (considerando apeonas os primeiros dias de cada mês).

    - A mínima histórica do valor do petróleo se deu durante a pandemia, chegando a 14,22 em 01/01/2020.

    - Nos últimos 10 anos, percebemos um pico de todos nossos indicadores em 2016 (Valor do Barril do petroleo, SELIC, Inflação americana e cotação do dólar). Após sua estabilização em 2017, vemos que a partir de 2020 tanto a Inflação Americana como o valor do Barril do petróleo vem tem uma tendência de alta. Ponto de atenção nos próximos anos.

    - Enquanto observamos uma tendência de mudança no cenário brasileiro a partir de fevereiro de 2021 (com a subida da selic), vemos que o petróleo, dólar e inflação americana não sofreram com grandes mudanças. 

