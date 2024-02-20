import streamlit as st
import pandas as pd 

st.markdown("# Kart Configurations 🏎️")
st.sidebar.markdown("# Kart Configurations 🏎️")

st.write("What Kart Configuration is Best?")

df_kart = pd.read_csv('streamlit_template/data/kart_stats.csv')
#st.write(df_kart)
##st.dataframe(df_kart)
##st.dataframe(df_kart)
df_kart=df_kart[['Body','Weight','Acceleration','Mini-Turbo','Ground Speed','Water Speed']]

st.dataframe(df_kart.style
             .highlight_max(color='lightgreen',axis=0,subset=['Weight','Acceleration','Mini-Turbo','Ground Speed','Water Speed'])
             .highlight_min(color='pink',axis=0,subset=['Weight','Acceleration','Mini-Turbo','Ground Speed','Water Speed'])
             )
st.line_chart(df_kart,x='Acceleration',y=['Mini-Turbo','Ground Speed'])
st.scatter_chart(df_kart,x='Ground Speed',y=['Acceleration','Mini-Turbo'])
#st.bar_chart(df_kart,x='Body',y=['Mini-Turbo'])
chosen_kart = st.selectbox('Pick a Kart',df_kart['Body'])
df_single_kart = df_kart.loc[df_kart['Body'] == chosen_kart]

df_unp_kart= df_single_kart.unstack().rename_axis(['catagory','row_number']).reset_index().drop(columns='row_number').rename({0:'strength'},axis=1)
st.bar_chart(df_unp_kart, x='catagory',y='strength')
