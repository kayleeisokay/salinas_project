import numpy as np
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

st.title("Simple Streamlit App")

st.write("Here's our first attempt at using data to create a plot")
# dialect+driver://username:password@host:port/database
engine = create_engine('postgresql://postgres:postgres@host.docker.internal:5433/postgres')

chart = pd.read_sql_table('my_third_dbt_model', con=engine, schema="public")

st.bar_chart(data=chart, x='crime', y='crime_count')