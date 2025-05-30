import pandas as pd

def filter_low_expression(df, threshold=1):
    return df[df.mean(axis=1) > threshold]

def normalize_tpm(df):
    gene_lengths = df.sum(axis=1) / 1000  # fake length
    rpk = df.div(gene_lengths, axis=0)
    tpm = rpk.div(rpk.sum(axis=0), axis=1) * 1e6
    return tpm
