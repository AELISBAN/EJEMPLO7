

import streamlit as st

st.title('100 Days of Python with Streamlit!')
st.write('Welcome to my interactive website built using Streamlit and Python!')
st.title('Interactive Slider Example')

slider_value = st.slider('Select a value:', 0, 100, 50)
st.write(f'You selected {slider_value}!')
import streamlit as st

st.title('Interactive Checkbox Example')

checkbox_value = st.checkbox('Check me')
if checkbox_value:
    st.write('Checkbox is checked!')
else:
    st.write('Checkbox is not checked.')
