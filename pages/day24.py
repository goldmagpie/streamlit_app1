import streamlit as st
import numpy as np
import pandas as pd
from time import time

st.title('st.cache')

a0 = time()
st.subheader('st.cache 사용')

@st.cache(suppress_st_warning=True)
def load_data_a():
    df = pd.DataFrame(
        np.random.rand(2000000, 5),
        columns=['a', 'b', 'c', 'd', 'e']
        )
    return df

st.write(load_data_a())
a1 = time()
st.info(a1-a0)


b0 = time()
st.subheader('st.cache 미사용')

def load_data_b():
    df = pd.DataFrame(
        np.random.rand(2000000, 5),
        columns=['a', 'b', 'c', 'd', 'e']
        )
    return df

st.write(load_data_b())
b1 = time()
st.info(b1-b0)