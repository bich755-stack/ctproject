import streamlit as st
import pandas as pd
#import plotly.figure_factory as ff
import plotly.express as px
#import matplotlib.pyplot as plt

st.set_page_config(layout='wide', page_title='My app')

#html variable
html = '''
<html>
    <head>
        <title>This HTML App</title>
        </head>
        <body>
            <h1>This is a long text</h1>
            <br>
            <hr>
            <h3>This is a small text</h3>
        </body>
 </html>
'''

with open('./com_html.html','r',encoding='utf-8') as f:
    filehtml = f.read()
    f.close()

#global variable
url = "https://www.youtube.com/watch?v=XyEOEBsa8I4"

#data app
df = pd.read_csv('./data/data.csv')

st.title('This is my first webapp!')
col1, col2 = st.columns((4,1))
with col1:
    with st.expander('Content1...'):
        st.subheader('Content1...')
        st.video(url)
    
    with st.expander('Content2_image...'):
        st.subheader('Content2_image...')
        st.image('./images/CatDog.jpeg')
        st.write('<hl>This is new title</h1>',unsafe_allow_html=True)
        st.markdown(html, unsafe_allow_html=True)
    
    with st.expander('Content3_htmlcontent...'):
        st.subheader('Content3_htmlcontent...')
        import streamlit.components.v1 as htmlviewer
        htmlviewer.html(filehtml, height=800)
        
        #dff = df.groupby(by='name').sum()
        #st.table(df)
        #st.plotly_chart(df)
        #df = px.data.iris()  # iris is a pandas DataFrame
        #fig = px.scatter(df, x="sepal_width", y="sepal_length")
        #event = st.plotly_chart(fig, key="iris", on_select="rerun")
        
with col2:
    with st.expander('Tips...'):
        st.subheader('Tips...')