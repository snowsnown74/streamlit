import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('streamlit 超入門')

st.write('ぷれぐれすばーの表示')
'start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.001)

st.write('dataFrame')

st.write('Display Image')

Img = Image.open('unko.jpg')
st.image(Img, caption='unnnkokokoko', use_column_width=True)

df = pd.DataFrame(
   np.random.rand(20,3),
    columns=['a','b','c']
)

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

#st.table(df.style.highlight_max(axis=0))

dfmap = pd.DataFrame(
   np.random.rand(100,2)/[50,50] + [35.69, 139.70],
    columns=['lat','lon']
)

st.map(dfmap)

option = st.sidebar.selectbox(
    '好きな数字',
    list(range(1,11))
)

'好きな数字',option,'だよおおおお'

# if st.checkbox('Show Image', True):
#     img = Image.open('unko.jpg')
#     st.image(img, caption='faefafae', use_column_width=True)


st.write('好きな趣味')
text = st.sidebar.text_input('趣味')
'君の趣味は',text

condition = st.sidebar.slider('調子は？',1,10,2)
'ちょうし',condition

lift_column, right_column = st.columns(2)
button = lift_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右からむ')

expander = st.expander('問い合わせ')
expander.write('問い合わせをかく')
expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせをかく1')

