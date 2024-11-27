# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 10:02:54 2024

@author: muril
"""
import matplotlib.pyplot as plt

# Definição dos dados
data = {
    'Normal (n=114)': [0.044, 0.255, 0.469, 0.768, 1.48],
    'Caucasian (n=748)': [0.054, 1.884, 3.209, 5.884, 13.484],
    'African-american (n=179)': [0.366, 3.463, 6.223, 10.215, 20.266],
    'Asian (n=61)': [0.448, 3.427, 5.787, 8.484, 16.877]
}

# Ajuste do eixo Y para 0.0-25.0 e plot do boxplot
fig, ax = plt.subplots(figsize=(8, 6))

# Redesigned boxplot with minimalistic style
ax.boxplot(data.values(),
           labels=[
               'Normal\n(n=114)',
               'Caucasian\n(n=748)',
               'African-american\n(n=179)',
               'Asian\n(n=61)'
           ],
           patch_artist=True,
           showmeans=True,
           widths=0.6,  # Adjusted width for better spacing
           boxprops=dict(facecolor='lightgray', edgecolor='darkblue', linewidth=1.5),
           whiskerprops=dict(color='darkblue', linestyle='-', linewidth=1.5),
           capprops=dict(color='darkblue', linewidth=1.5),
           flierprops=dict(marker='x', color='orange', markersize=8),
           meanprops=dict(marker='o', markerfacecolor='green', markersize=8))

# Ajustando título e rótulos
ax.set_title('RAD54L Expression in BRCA Samples by Race', fontsize=14, fontweight='bold', color='darkblue')
ax.set_ylabel('Transcript per million (TPM)', fontsize=12, fontweight='bold', color='darkblue')
ax.set_xlabel('TCGA Samples', fontsize=12, fontweight='bold', color='darkblue')

# Ajuste do eixo Y
ax.set_ylim(0.0, 25.0)

# Ajuste da grade
ax.yaxis.grid(True, linestyle='--', which='major', color='gray', alpha=0.7)
ax.set_axisbelow(True)

# Ajuste do tamanho da fonte do eixo X
plt.xticks(fontsize=10)

plt.tight_layout()
plt.show()
