# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 20:34:36 2024

@author: muril
"""

import pandas as pd
import matplotlib.pyplot as plt

# Caminho para o arquivo Excel
file_path = r"C:\Users\muril\Desktop\Data6.xlsx"

# Carregar os dados da planilha
data = pd.ExcelFile(file_path)
df = data.parse('Dado 6')

# Limpeza dos dados
df.columns = ["RAD54L_expression_TPM", "ORC1L_expression_TPM"]
df["RAD54L_expression_TPM"] = pd.to_numeric(df["RAD54L_expression_TPM"], errors="coerce")
df["ORC1L_expression_TPM"] = pd.to_numeric(df["ORC1L_expression_TPM"], errors="coerce")
df_cleaned = df.dropna()

# Criar o gráfico de dispersão
plt.figure(figsize=(8, 6))
plt.scatter(df_cleaned["RAD54L_expression_TPM"], 
            df_cleaned["ORC1L_expression_TPM"], 
            color='orange', alpha=0.7, marker='x')
plt.title("Scatter Plot: RAD54L vs ORC1L Expression Values", fontsize=14)
plt.xlabel("RAD54L Expression Values (TPM)", fontsize=12)
plt.ylabel("ORC1L Expression Values (TPM)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)

# Calcular a correlação de Pearson
pearson_correlation = df_cleaned["RAD54L_expression_TPM"].corr(df_cleaned["ORC1L_expression_TPM"], method="pearson")
print(f"Correlação de Pearson entre RAD54L e ORC1L: {pearson_correlation:.4f}")
plt.show()
