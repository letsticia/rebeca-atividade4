import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Dashboard de Covid-19")

df = pd.read_csv('WHO_time_series.csv')

df.info()
df.head(5)
df['Date_reported'] = pd.to_datetime(df['Date_reported'])
df.info()

fig1 = px.line(df,
    x='Date_reported',
    y='Cumulative_cases',
    color = 'Country',
    title = 'Todos os casos acumulados de Covid-19'
)
fig1.update_layout(xaxis_title='Data', yaxis_title='Número de casos acumulados')
fig1.show()

st.plotly_chart(fig1, use_container_width=True)

df_filtro = df.query("Country == 'Brazil' or Country == 'United States of America' or Country == 'India'")
fig2 = px.pie(
    df_filtro,
    names = 'Country',
    values = 'Cumulative_cases',
    title= 'Comparativo entre os casos de Covid nos USA, Brasil e India'
)
fig2.show()

st.plotly_chart(fig2, use_container_width=True)
