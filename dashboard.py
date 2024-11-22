import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import plotly.express as px

st.title('Dashboard: Top 100 US Companies')

# Carregar o DataFrame
df = pd.read_csv('CompaniesCluster.csv')

# 1. Informações sobre as Empresas
with st.expander("Informações Gerais das Empresas"):
    st.subheader('Companies Information')
    st.write(df.head())

# 2. Gráfico de Dispersão: Revenue vs Employees
with st.expander("Gráfico de Dispersão: Receita vs Número de Empregados por Cluster"):
    st.subheader('Revenue vs Employees per Cluster')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='Revenue(M)', y='Employees', hue='Cluster', data=df, palette='viridis', ax=ax)
    plt.title('Revenue vs Employees per Cluster')
    plt.xlabel('Revenue in Millions')
    plt.ylabel('Number of Employees')
    st.pyplot(fig)

# 3. Estatísticas Descritivas
with st.expander("Estatísticas Descritivas"):
    st.subheader('Descritive Statistics of Data')
    st.write(df.describe())

# 4. Número de Empresas por Cluster
with st.expander("Número de Empresas por Cluster"):
    st.subheader('Number of Companies per Cluster')
    cluster_count = df['Cluster'].value_counts().reset_index()
    cluster_count.columns = ['Cluster', 'Count']
    fig_cluster = px.bar(cluster_count, x='Cluster', y='Count', title='Number of Companies per Cluster')
    st.plotly_chart(fig_cluster)

# 5. Top 5 Empresas com Mais Empregados
with st.expander("Top 5 Empresas com Mais Empregados"):
    st.subheader('Top 5 Empresas with Most Employees')
    top_employees = df[['Name', 'Employees']].sort_values(by='Employees', ascending=False).head(5)
    st.write(top_employees)

# 6. Empresas por Indústria
with st.expander("Empresas por Indústria"):
    industry_filter = st.selectbox('Select an Industry', df['Industry'].unique())
    st.subheader(f'Companies of Industry: {industry_filter}')
    df_filtered = df[df['Industry'] == industry_filter]
    st.write(df_filtered[['Name', 'Revenue(M)', 'Employees', 'Cluster']])

# 7. Receita por Indústria
with st.expander("Distribuição da Receita por Indústria"):
    st.subheader('Revenue of Companies by Industry')
    fig_industry = px.box(df, x='Industry', y='Revenue(M)', title='Distributtion of Revenue by Industry')
    st.plotly_chart(fig_industry)

