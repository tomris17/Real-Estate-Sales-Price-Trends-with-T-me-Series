import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Real Estate Sales & Price Trends", layout="centered")

st.title("Real Estate Sales & Price Trends App")
st.write(
    "Bu uygulama, tarihsel gayrimenkul satış verilerini analiz ederek konut piyasası trendlerini, fiyat dalgalanmalarını ve mülk türüne göre fiyat dağılımlarını görselleştirir."
)

@st.cache_data
def load_data():
    df = pd.read_csv("raw_sales.csv", low_memory=False)
    df["datesold"] = pd.to_datetime(df["datesold"])
    df = df.sort_values("datesold").reset_index(drop=True)
    return df

try:
    df = load_data()
    
    st.subheader("Gayrimenkul Veri Seti Önizlemesi")
    st.dataframe(df.head())

    st.subheader("Gayrimenkul Analiz Grafikleri")
    chart_type = st.selectbox(
        "Grafik Türü Seçin",
        ["Aylık Ortalama Fiyat Trendi", "Mülk Türüne Göre Fiyat Dağılımı"]
    )
    
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(10, 5))
    
    if chart_type == "Aylık Ortalama Fiyat Trendi":
        df_monthly = (
            df.set_index("datesold").resample("ME")["price"].mean().reset_index()
        )
        ax.plot(
            df_monthly["datesold"],
            df_monthly["price"],
            label="Average Monthly House Price",
            color="darkcyan",
            linewidth=2,
        )
        ax.set_title("Real Estate Average Prices Over Time (Monthly Trend)", fontsize=14, fontweight="bold")
        ax.set_ylabel("Average Price", fontsize=12)
        ax.set_xlabel("Date Sold", fontsize=12)
        ax.legend()
    else:
        sns.boxplot(x="propertyType", y="price", data=df, palette="Set2", ax=ax, hue="propertyType", legend=False)
        ax.set_title("Price Distribution by Property Type", fontsize=14, fontweight="bold")
        ax.set_xlabel("Property Type", fontsize=12)
        ax.set_ylabel("Price", fontsize=12)
        
    st.pyplot(fig)

except Exception as e:
    st.error(f"Veri yüklenirken veya işlenirken bir hata oluştu: {e}")