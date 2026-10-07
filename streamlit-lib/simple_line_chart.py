import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10,3),columns=["col1","col2","col3"])

st.line_chart(df)

st.subheader("Show data")
st.write(df)
x_axis = "col1"
y_axis = "col2"

st.line_chart(df,x=x_axis, y=y_axis, color= "blue")

