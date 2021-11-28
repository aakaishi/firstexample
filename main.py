import streamlit as st
import pandas

data= {
  'Series 1': [1,2,5,7,9],
  'Series 2': [13,15,18,23,45]
}

df = pandas.DataFrame(data)

st.title('First Streamlit App')
st.subheader('Introduction of application')
st.write(''' This is a example..
Enjoy it!
''')

st.write(df)
st.line_chart(df)
st.area_chart(df)

myslider = st.slider('Celsius')
st.write(myslider, 'in Fahrenheit is: ', myslider * 9/5 + 32)