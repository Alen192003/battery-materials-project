
import streamlit as st

from analysis import load_battery_data


st.set_page_config(
    page_title="Battery Materials Research",
    page_icon="🔋",
    layout="wide",
)

st.title("Battery Materials Research")
st.write(
    "A computational investigation of battery technologies "
    "and their potential for energy storage."
)

st.subheader("Research dataset")

data = load_battery_data()
st.dataframe(data, use_container_width=True)

st.subheader("Data quality")

missing = data.isna().sum()
st.write("Missing values by column")
st.dataframe(
    missing.rename("Missing values"),
    use_container_width=True,
)

st.info(
    "Research stage: dataset setup. "
    "Numerical comparisons will be added after source verification."
)
