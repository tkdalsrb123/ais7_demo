import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
import koreanize_matplotlib
import streamlit as st

st.title('타이타닉 생존자 분석')

data = sns.load_dataset('titanic')
data


fig, ax = plt.subplots()
sns.barplot(data=data, x='who', y='survived', ci=None).set_title('Seaborn 활용 타이타닉 생존자 구분')
st.pyplot(fig)

st.subheader('streamlit 활용 타이타닉 생존자 구분')
st.bar_chart(data=data, x='who', y='survived')

data_age = data[['age', 'fare', 'alive']]
data_age = data_age.dropna()


st.sidebar.header('연령대별 생존여부 확인')
sorted_alive = sorted(data.alive.unique())
selected_alive = st.sidebar.multiselect('alive',
        sorted_alive, sorted_alive)

if len(selected_alive) > 0:
    data_age = data_age[data_age['alive'].isin(selected_alive)]

st.dataframe(data_age)

st.subheader('생존자 수의 평균 나이와 평균 요금')
st.bar_chart(data_age, x='alive', y='age')
st.bar_chart(data_age, x='age', y='fare')