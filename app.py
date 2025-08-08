import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from azure.identity import DefaultAzureCredential


st.set_page_config(page_title="Silal Test App", page_icon="🇦🇪")
# --- App Title ---
st.title("Streamlit App Deployed on Azure")
st.subheader("Hosted in the UAE North Region")
# --- Create a Sample DataFrame ---
data = {
 'Item': ['Dates', 'Camel Milk', 'Spices', 'Honey'],
 'Price (AED)': [50, 15, 25, 80],
 'Stock (kg)': [500, 200, 150, 100]
}
df = pd.DataFrame(data)
# --- Display the DataFrame ---
st.header("Local Product Inventory")
st.dataframe(df)

# Connection parameters
driver = 'ODBC Driver 18 for SQL Server'
server = '4cpzrtcatleexlcussttwgadrm-re46cale6rzu7fzhhoppwwexxa.datawarehouse.fabric.microsoft.com'
database = 'Analytics'

# Create the connection string
conn_str = f"""
    Driver={{{driver}}};
    Server={server};
    Database={database};
    Authentication=ActiveDirectoryInteractive;
    Encrypt=yes;
    TrustServerCertificate=no;
    Connection Timeout=30;
"""

params = urllib.parse.quote_plus(conn_str)
engine = create_engine(f'mssql+pyodbc:///?odbc_connect={params}')

# Query
query = "SELECT TOP 10 * FROM dbo.publicholidays"
try:
    df = pd.read_sql(query, engine)
    st.header("Local Product Inventory")
    st.dataframe(df)
except Exception as e:
    st.error(f"❌ Failed to load data: {e}")

