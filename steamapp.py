import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
import plotly.express as px


col1,col2,col3=st.columns([1,2,1])



insurance=pd.read_csv("insurance.csv")

st.markdown("# Hello, Welcome to this Website for CMSE 830.")
with st.expander(  "# Click here for Some Website Info!"):
    st.write("This website will provide some basic information on a dataset about insurance rates accross different regions of the United States.")

click_here=st.selectbox('Please select the dataset:',['Insurance'])

if click_here=='Insurance':
    df1=insurance
    st.write("Let's look at the Insurance Dataset!")





st.write(df1.head(12))

df = df1

button1=st.button("Show Statistics")
if button1:
    st.write(df.describe())
if st.button("Hide Statistics"):
    button1=False

cols=df.columns



button2=st.button("Show Columns")
if button2:
    st.write("Here is the column length!",len(cols))
    st.write("The names are as follows:")
    st.write(df.columns)
if st.button("Hide Columns"):
    button2=False
st.write("What Variables do you want to investigate?")
x_val=st.selectbox('Variable on the x-axis?',cols)
y_val=st.selectbox('Variable on the x-axis?:',cols)

button3=st.button("Bar Chart");
if button3:
    st.bar_chart(data=df, x=x_val, y=y_val)

if st.button("Hide Bar Chart"):
    button3=False

button4=st.button("Scatter Plot");
if button4:
    scatter_fig = px.scatter(df, x=x_val, y=y_val)
    st.plotly_chart(scatter_fig, use_container_width=True)

if st.button("Hide Scatter Plot "):
    button4=False

st.write("We have looked at some of the infomation regarding the insurance dataset. Please come back later when the project is finished!")




