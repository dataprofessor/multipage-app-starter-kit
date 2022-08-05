import streamlit as st
from utilities import test
from tools.utility import test2

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.header("Welcome to the Multipage App! 👋")
st.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus imperdiet lacus nulla, vitae faucibus erat cursus ut. Nullam quam lorem, semper eu nulla sit amet, pharetra viverra mi. Donec suscipit ligula metus, nec venenatis orci pellentesque et. Quisque ac sem eros. Duis non tellus vel est dictum interdum. Nam pulvinar mattis rhoncus. In sit amet ante ut odio scelerisque ullamcorper. Aliquam hendrerit facilisis purus eu mollis. Maecenas iaculis eget turpis nec mollis.')

st.sidebar.header('About')
st.sidebar.write('This is a simple demo of the Multipage App.')

test()
test2()
