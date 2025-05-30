#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 30 18:44:26 2025

@author: kavyadeepak
"""

import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import pandas as pd

def plot_heatmap(df):
    sns.clustermap(df, cmap="viridis")
    plt.savefig("heatmap.png")

def plot_pca(df):
    pca = PCA(n_components=2)
    pcs = pca.fit_transform(df.T)
    pc_df = pd.DataFrame(pcs, columns=["PC1", "PC2"])
    return pc_df