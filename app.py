#如果在st后面加上sidebar的话，输入栏会在页面左侧运行
%%writefile app.py
from re import A
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit.入門')

st.write('Display Image')

st.sidebar.write('Interactive Widgets')

st.write('プレグレスバーの表示')
'Start!!'

latest_iteration = st.empty()  #进度条
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i+1)
  time.sleep(0.01)
'Done!!!!!'
##############################################################################
dh = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})#插入表格
if st.checkbox('dataframe'):
 st.table(dh.style.highlight_max(axis=0))

if st.checkbox('章、節、項、プログラミング'):#显示文字#越多字越小，代码显示
  """
  # 章
  ## 節
  ### 項
  ```python
  import streamlit as st
  import numpy as np
  import pandas as pd
  """

if st.checkbox('Show Image'):
  img = Image.open('simple.jpg')
  st.image(img,caption='ペッペ',use_column_width=True)#插入图片

da = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)#定义表格走势图
if st.checkbox('line_chart'):
  st.line_chart(da)#折线图
if st.checkbox('raea_chart'):
  st.area_chart(da)#折现填充图
if st.checkbox('bar_chart'):
  st.bar_chart(da)#柱状图


df = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=['lat','lon']
)#地图范围
if st.checkbox('map'):
  st.map(df)

if st.checkbox('好きな数字'):#菜单选数
  option = st.selectbox(
      'あなたが好きな数字を教えてください',
      list(range(1,11))
  )

  'あなたの好きな数字は、',option,'です。'

if st.checkbox('趣味'):#自己输入文字
  text = st.sidebar.text_input('あなたの趣味を教えてください',)
  #如果在st后面加上sidebar的话，输入栏会在页面左侧运行
  'あなたの趣味は、',text,'です。'

if st.checkbox('調子'):#拉进度条
  condition = st.sidebar.slider('あなたの今の調子は？',0,100,50)
  'コンディション',condition

if st.checkbox('ボタン'):#按钮
  left_column,right_column = st.columns(2)
  button = left_column.button('右カラムに文字を表示')
  if button:
    right_column.write('ここは右カラム')
if st.checkbox('問い合わせ'):#文字菜单
  expander1 = st.expander('問い合わせ1')
  expander1.write('問い合わせ1の回答')
  expander2 = st.expander('問い合わせ2')
  expander2.write('問い合わせ2の回答')
  expander3 = st.expander('問い合わせ3')
  expander3.write('問い合わせ3の回答')
