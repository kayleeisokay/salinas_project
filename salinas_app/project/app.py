import numpy as np
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

st.title("Simple Streamlit App")

st.write("Here's our first attempt at using data to create a table:")
st.write(
    pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [20, 30, 40, 50]})
)

engine = create_engine('postgresql://postgres:postgres@host.docker.internal:5432/salinas_db')