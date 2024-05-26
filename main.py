# B1: nhap vao 1 ten ai do. Khi bam xac nhan. Thi hien thi xin chao + ten nguoi do.

# B2: Tao thanh progress tu tang den 100%

import streamlit as st
import time
st.title('Hi')
name = st.text_input('Name?')
if st.button('Show name'):
  st.write('Hi',name)

st.title('My progress')
my_bar = st.progress(0)
for i in range(100):
  time.sleep(1)
  my_bar.progress(i + 1)