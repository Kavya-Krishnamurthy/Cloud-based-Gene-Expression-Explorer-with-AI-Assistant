#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 30 18:45:46 2025

@author: kavyadeepak
"""

import streamlit as st
import pandas as pd
from pipeline import filter_low_expression, normalize_tpm
from visualize import plot_heatmap, plot_pca
from assisstant import chat_with_data
import matplotlib.pyplot as plt

st.set_page_config("Gene Expression Explorer", layout="wide")
st.title("🧬 Gene Expression Explorer + AI Assistant")

uploaded = st.file_uploader("Upload Gene Expression CSV", type="csv")
if uploaded:
    df = pd.read_csv(uploaded, index_col=0)

    st.subheader("🔍 Filter Low Expression Genes")
    threshold = st.slider("Mean expression threshold", 0.0, 10.0, 1.0)
    df_filtered = filter_low_expression(df, threshold)
    st.write(df_filtered.head())

    st.subheader("⚖️ Normalize with TPM")
    df_tpm = normalize_tpm(df_filtered)
    st.write(df_tpm.head())

    st.subheader("🧠 AI Assistant")
    query = st.text_input("Ask something about your data:")
    if query:
        with st.spinner("Thinking..."):
            answer = chat_with_data(df_tpm, query)
        st.success(answer)

    st.subheader("🔥 Heatmap")
    plot_heatmap(df_tpm)
    st.image("heatmap.png")

    st.subheader("🔬 PCA")
    pca_df = plot_pca(df_tpm)
    st.write(pca_df)
    st.scatter_chart(pca_df)
