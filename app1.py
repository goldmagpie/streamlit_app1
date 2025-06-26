import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("📊 Streamlit 가짜 데이터 시각화")

# 가짜 데이터 생성
np.random.seed(42)
data = pd.DataFrame({
    '날짜': pd.date_range(start='2025-01-01', periods=30),
    '매출액': np.random.randint(100, 500, size=30)
})

# 데이터 출력
st.subheader("💾 가짜 데이터 (매출)")
st.dataframe(data)

# 선 그래프 그리기
st.subheader("📈 매출 추이 그래프")
fig, ax = plt.subplots()
ax.plot(data['날짜'], data['매출액'], marker='o')
ax.set_xlabel("날짜")
ax.set_ylabel("매출액")
ax.set_title("매출 변화 추이")
st.pyplot(fig)