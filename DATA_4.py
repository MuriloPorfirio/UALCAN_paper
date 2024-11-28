# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 11:34:14 2024

@author: muril
"""

import matplotlib.pyplot as plt

# Definição dos dados
data = {
    'Normal (n=114)': [0.044, 0.255, 0.469, 0.768, 1.48],
    'Luminal (n=566)': [0.173, 1.929, 3.265, 5.132, 11.158],
    'HER2 positive (n=37)': [1.396, 3.393, 4.816, 10.504, 20.588],
    'Triple negative (n=116)': [0.384, 6.579, 10.189, 13.547, 23.334]
}

# Ajuste do eixo Y e plot do boxplot
fig, ax = plt.subplots(figsize=(8, 6))

# Redesigned boxplot with minimalistic style
ax.boxplot(data.values(),
           labels=[
               'Normal\n(n=114)',
               'Luminal\n(n=566)',
               'HER2 positive\n(n=37)',
               'Triple negative\n(n=116)'
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
ax.set_title('Expression of RAD54L in BRCA Based on Breast Cancer Subclasses', 
             fontsize=14, fontweight='bold', color='darkblue')
ax.set_ylabel('Transcript per million (TPM)', fontsize=12, fontweight='bold', color='darkblue')
ax.set_xlabel('Breast Cancer Subclasses', fontsize=12, fontweight='bold', color='darkblue')

# Ajuste do eixo Y
ax.set_ylim(0.0, 25.0)

# Ajuste da grade
ax.yaxis.grid(True, linestyle='--', which='major', color='gray', alpha=0.7)
ax.set_axisbelow(True)

# Ajuste do tamanho da fonte do eixo X
plt.xticks(fontsize=10)

# Ajuste do layout
plt.tight_layout()

# Exibição do gráfico
plt.show()
