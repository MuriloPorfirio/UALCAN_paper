# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 10:02:54 2024

@author: muril
"""

import pandas as pd
import matplotlib.pyplot as plt

# Caminho para o arquivo Excel
file_path = r"C:\Users\muril\Desktop\UALCAN.xlsx"

# Carregar os dados da planilha
data = pd.ExcelFile(file_path)
df = data.parse('Dado 8')

# Limpeza dos dados
df.columns = ["RAD54L_expression_TPM", "CDCA8_expression_TPM"]
df["RAD54L_expression_TPM"] = pd.to_numeric(df["RAD54L_expression_TPM"], errors="coerce")
df["CDCA8_expression_TPM"] = pd.to_numeric(df["CDCA8_expression_TPM"], errors="coerce")
df_cleaned = df.dropna()

# Criar o gráfico de dispersão
plt.figure(figsize=(8, 6))
plt.scatter(df_cleaned["RAD54L_expression_TPM"], 
            df_cleaned["CDCA8_expression_TPM"], 
            color='purple', alpha=0.7, marker='d')
plt.title("Scatter Plot: RAD54L vs CDCA8 Expression Values", fontsize=14)
plt.xlabel("RAD54L Expression Values (TPM)", fontsize=12)
plt.ylabel("CDCA8 Expression Values (TPM)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)

# Calcular a correlação de Pearson
pearson_correlation = df_cleaned["RAD54L_expression_TPM"].corr(df_cleaned["CDCA8_expression_TPM"], method="pearson")
print(f"Correlação de Pearson entre RAD54L e CDCA8: {pearson_correlation:.4f}")
plt.show()
