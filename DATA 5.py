# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 21:55:14 2024

@author: muril
"""

import pandas as pd
import matplotlib.pyplot as plt

# Caminho para o arquivo Excel
file_path = r"C:\Users\muril\Desktop\UALCAN_Paper_Data.xlsx"

# Carregar os dados da planilha
data = pd.ExcelFile(file_path)
df = data.parse('Dado 5')

# Limpeza dos dados
df.columns = ["RAD54L_expression_TPM", "KIF2C_expression_TPM"]
df["RAD54L_expression_TPM"] = pd.to_numeric(df["RAD54L_expression_TPM"], errors="coerce")
df["KIF2C_expression_TPM"] = pd.to_numeric(df["KIF2C_expression_TPM"], errors="coerce")
df_cleaned = df.dropna()

# Criar o gráfico de dispersão
plt.figure(figsize=(8, 6))
plt.scatter(df_cleaned["RAD54L_expression_TPM"], df_cleaned["KIF2C_expression_TPM"], alpha=0.7)
plt.title("Scatter Plot: RAD54L vs KIF2C Expression Values", fontsize=14)
plt.xlabel("RAD54L Expression Values (TPM)", fontsize=12)
plt.ylabel("KIF2C Expression Values (TPM)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()
