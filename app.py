import numpy as np
import pandas as pd
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Dashboard de Dados Python",
    page_icon="📊",
    layout="wide",
)

st.title("Dashboard integrado do projeto de Python")

st.caption(
    "Aluno: Pedro Henriques Silva | Professor: Alexandre Neves Louzada"
)


def carregar_csv_arquivo(nome_arquivo):
    caminho = Path(__file__).resolve().parent / nome_arquivo
    if caminho.exists():
        return pd.read_csv(caminho)
    return None


def dados_vendas():
    df = carregar_csv_arquivo("vendas.csv")
    if df is not None:
        if "data" in df.columns and "data_hora" not in df.columns:
            df["data_hora"] = pd.to_datetime(df["data"])
        elif "data_hora" in df.columns:
            df["data_hora"] = pd.to_datetime(df["data_hora"])
        return df

    dados = {
        "cliente_id": [101, 102, 103, 101, 104, 102, 105, 103],
        "valor": [3500.75, 189.50, np.nan, 1200.00, 450.00, np.nan, 89.90, 780.50],
        "categoria": [
            "Eletronicos",
            "Livros",
            "Roupas",
            "Eletronicos",
            "Automotivo",
            "Livros",
            "Roupas",
            "Roupas",
        ],
        "data_hora": [
            "2024-01-15 10:23:00",
            "2024-01-18 14:05:00",
            "2024-02-05 09:12:00",
            "2024-02-20 16:40:00",
            "2024-03-02 11:00:00",
            "2024-03-15 18:30:00",
            "2024-04-10 08:20:00",
            "2024-04-22 13:45:00",
        ],
        "status": [
            "Concluído",
            "Concluído",
            "Pendente",
            "Concluído",
            "Cancelado",
            "Concluído",
            "Concluído",
            "Concluído",
        ],
        "email": [
            "maria@gmail.com",
            "joao@outlook.com",
            "ana@yahoo.com",
            "maria@gmail.com",
            "carlos@gmail.com",
            "joao@outlook.com",
            "lucas@empresa.com.br",
            "ana@yahoo.com",
        ],
    }
    df = pd.DataFrame(dados)
    df["data_hora"] = pd.to_datetime(df["data_hora"])
    mediana_global = df["valor"].median()
    mediana_categoria = df.groupby("categoria")["valor"].transform("median")
    df["valor"] = df["valor"].fillna(mediana_categoria.fillna(mediana_global))
    return df


def dados_livros():
    df = carregar_csv_arquivo("livros.csv")
    if df is not None:
        return df

    return pd.DataFrame(
        {
            "titulo": [
                "A Revolução dos Bichos",
                "O Pequeno Príncipe",
                "1984",
                "Dom Quixote",
                "A Arte da Guerra",
            ],
            "preco": ["£10.00", "£8.00", "£12.50", "£14.99", "£9.40"],
        }
    )


def dados_populacao():
    df = carregar_csv_arquivo("populacao_paises.csv")
    if df is not None:
        return df

    return pd.DataFrame(
        {
            "Pais": [
                "India",
                "China",
                "Estados Unidos",
                "Indonesia",
                "Paquistão",
                "Nigeria",
                "Brasil",
                "Bangladesh",
                "Russia",
                "Mexico",
            ],
            "Populacao": [
                1434000000,
                1412000000,
                339000000,
                277000000,
                251000000,
                223000000,
                216000000,
                176000000,
                144000000,
                129000000,
            ],
        }
    )


def dados_numpy():
    pecas_vendidas = np.array([150, 120, 90, 210, 300, 250, 180])
    faturamento = pecas_vendidas * 50
    visitas = np.array([1000, 1200, 1500, 1300, 1400, 1600, 1700, 1800, 2000, 2100, 2200, 2500])
    visitas_trimestres = visitas.reshape(4, 3)
    faturamento_campanhas = np.array([12000, 45000, 23000, 89000, 31000])
    return {
        "pecas_vendidas": pecas_vendidas,
        "faturamento": faturamento,
        "visitas": visitas,
        "visitas_trimestres": visitas_trimestres,
        "faturamento_campanhas": faturamento_campanhas,
    }


def dados_imoveis():
    return pd.DataFrame(
        {
            "bairro": ["Centro", "Copacabana", "Barra", "Botafogo", "Ipanema", "Niterói"],
            "preco": [420000, 950000, 760000, 880000, 1010000, 540000],
            "area_m2": [55, 85, 72, 78, 90, 68],
            "lat": [-22.9068, -22.9711, -23.0089, -22.9527, -22.9831, -22.8830],
            "lon": [-43.1729, -43.1822, -43.3664, -43.1834, -43.2010, -43.1036],
        }
    )


vendas = dados_vendas()
livros = dados_livros()
populacao = dados_populacao()
numpy_data = dados_numpy()
imoveis = dados_imoveis()

# Preparação de dados
vendas["mes"] = vendas["data_hora"].dt.strftime("%Y-%m")
resumo = (
    vendas.groupby("categoria")["valor"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
    .rename(columns={"categoria": "Categoria", "valor": "Valor total"})
)

livros["preco_num"] = livros["preco"].astype(str).str.replace("£", "", regex=False).astype(float)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Receita total", f"R$ {vendas['valor'].sum():,.2f}")
with col2:
    st.metric("Pedidos concluídos", int((vendas["status"] == "Concluído").sum()))
with col3:
    st.metric("Livros no catálogo", len(livros))
with col4:
    st.metric("População total", f"{populacao['Populacao'].sum():,.0f}")

abas = st.tabs(["Resumo", "Vendas", "Web e População", "NumPy", "Mapa"])

with abas[0]:
    st.subheader("Resumo geral dos dados")
    st.bar_chart(resumo.set_index("Categoria"), use_container_width=True)
    st.dataframe(resumo, use_container_width=True)

with abas[1]:
    st.subheader("Desempenho por categoria e período")
    categoria_selecionada = st.multiselect(
        "Categorias",
        options=sorted(vendas["categoria"].unique()),
        default=sorted(vendas["categoria"].unique()),
    )
    vendas_filtradas = vendas[vendas["categoria"].isin(categoria_selecionada)].copy()

    if not vendas_filtradas.empty:
        mensal = vendas_filtradas.groupby("mes")["valor"].sum().sort_index()
        st.line_chart(mensal)
        st.bar_chart(vendas_filtradas.groupby("categoria")["valor"].sum())
        st.dataframe(vendas_filtradas, use_container_width=True)
    else:
        st.warning("Selecione pelo menos uma categoria para visualizar o gráfico.")

with abas[2]:
    st.subheader("Dados extraídos dos exercícios de web scraping")
    st.write("### Livros")
    st.bar_chart(livros[["titulo", "preco_num"]].set_index("titulo"))
    st.dataframe(livros[["titulo", "preco"]], use_container_width=True)

    st.write("### População por país")
    populacao_top = populacao.nlargest(10, "Populacao")
    st.bar_chart(populacao_top.set_index("Pais")["Populacao"])
    st.dataframe(populacao_top, use_container_width=True)

with abas[3]:
    st.subheader("Dados da atividade de NumPy")
    st.write("### Peças vendidas")
    st.line_chart(pd.Series(numpy_data["pecas_vendidas"]))

    st.write("### Faturamento por campanha")
    campanhas = pd.Series(
        numpy_data["faturamento_campanhas"],
        index=[f"Campanha {i + 1}" for i in range(len(numpy_data["faturamento_campanhas"]))],
    )
    st.bar_chart(campanhas)

    st.write("### Visitas por trimestre")
    visitas_df = pd.DataFrame(
        numpy_data["visitas_trimestres"],
        index=["Trimestre 1", "Trimestre 2", "Trimestre 3", "Trimestre 4"],
        columns=["Mês 1", "Mês 2", "Mês 3"],
    )
    st.bar_chart(visitas_df)

with abas[4]:
    st.subheader("Mapa dos imóveis")
    st.map(imoveis[["lat", "lon"]])
    st.dataframe(imoveis, use_container_width=True)

st.markdown("---")
st.caption("Dashboard construído com dados dos notebooks de Pandas, NumPy, web scraping e Folium do projeto.")
