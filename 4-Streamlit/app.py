import streamlit as st
from cassandra.cluster import Cluster
import pandas as pd

# Cassandra bağlantısı oluşturma
cluster = Cluster(['CASSANDRA_HOST'])
session = cluster.connect('cassandra_tutorial')  # Cassandra anahtar uzayının adını burada değiştirin

# Cassandra verilerini çekme
result_set = session.execute('SELECT * FROM energy_data')  # Cassandra tablosunun adını burada değiştirin
data = list(result_set)

# Verileri Pandas DataFrame'e dönüştürme
df = pd.DataFrame(data)

# Streamlit ile görselleştirme
st.title("Cassandra Veri Görselleştirme")

# Verileri DataFrame olarak görüntüleme
st.write("Veriler:")
st.dataframe(df)

# Örneğin sadece "use_kw" sütununu bir çizgi grafiği ile görselleştirme
st.write("use_kw Sütunu:")
st.line_chart(df.set_index("time")["use_kw"])
