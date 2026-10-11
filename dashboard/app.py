import os
import requests
import pandas as pd
import plotly.express as px
import streamlit as st

API = os.getenv("API_URL", "http://api:8000")
st.set_page_config(page_title="Product Metrics", layout="wide")
st.title("Product Metrics Dashboard")

@st.cache_data(ttl=15)
def fetch(path):
    return requests.get(f"{API}{path}").json()

kpi = fetch("/api/metrics/kpi")
rev = pd.DataFrame(fetch("/api/metrics/revenue"))

c1, c2, c3, c4 = st.columns(4)
c1.metric("DAU", kpi["dau"])
c2.metric("MAU", kpi["mau"])
c3.metric("Stickiness", f"{kpi['stickiness']:.2%}")
c4.metric("MRR", f"{kpi['total_mrr']:,.0f}")

c5, c6, c7, c8 = st.columns(4)
c5.metric("MRR growth", f"{kpi['mrr_growth_mom']:.2%}")
c6.metric("NRR", f"{kpi['nrr']:.2%}")
c7.metric("Quick ratio", f"{kpi['quick_ratio']:.2f}")
c8.metric("LTV/CAC", f"{kpi['ltv_cac']:.1f}")

if not rev.empty:
    st.subheader("MRR динамика")
    st.plotly_chart(px.line(rev, x="date", y="mrr"))

    st.subheader("MRR components")
    long = rev.melt(id_vars="date",
                     value_vars=["new","expansion","contraction","churn"],
                     var_name="component", value_name="value")
    st.plotly_chart(px.bar(long, x="date", y="value", color="component"))
