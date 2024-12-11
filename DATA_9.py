# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 13:16:39 2024

@author: muril
"""

import matplotlib.pyplot as plt

# Definição dos dados como quartis e extremos
data = {
    'Normal (n=97)': {
        'low': 0.049, 'q1': 0.054, 'median': 0.058, 'q3': 0.062, 'high': 0.079
    },
    'Primary tumor (n=793)': {
        'low': 0.036, 'q1': 0.052, 'median': 0.056, 'q3': 0.062, 'high': 0.078
    }
}

# Preparação dos dados no formato necessário para o boxplot
formatted_data = [
    [data[key]['low'], data[key]['q1'], data[key]['median'], data[key]['q3'], data[key]['high']]
    for key in data
]

# Configuração das cores para os grupos
colors = ['lightblue', 'lightcoral']

# Configurando o boxplot
fig, ax = plt.subplots(figsize=(8, 6))

# Redesigned boxplot
bp = ax.boxplot(
    formatted_data,
    patch_artist=True,  # Permite colorir as caixas
    showmeans=True,  # Mostra a média
    widths=0.6  # Ajusta a largura das caixas
)

# Aplicar cores às caixas individualmente
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_edgecolor('darkblue')
    patch.set_linewidth(1.5)

# Ajuste visual dos whiskers e caps
for whisker in bp['whiskers']:
    whisker.set(color='darkblue', linestyle='-', linewidth=1.5)
for cap in bp['caps']:
    cap.set(color='darkblue', linewidth=1.5)

# Personalização de outliers
for flier in bp['fliers']:
    flier.set(marker='o', color='orange', markersize=5)

# Personalização da linha de média
for mean in bp['means']:
    mean.set(marker='o', markerfacecolor='green', markersize=8)

# Ajustar limites do eixo Y para visibilidade adequada
ax.set_ylim(0.03, 0.09)

# Configurando os rótulos e título
ax.set_title('Promoter Methylation Level of RAD54L in BRCA', fontsize=14, fontweight='bold', color='darkblue')
ax.set_ylabel('Methylation Level', fontsize=12, fontweight='bold', color='darkblue')
ax.set_xlabel('TCGA Samples', fontsize=12, fontweight='bold', color='darkblue')
ax.set_xticks([1, 2])
ax.set_xticklabels(['Normal\n(n=97)', 'Primary tumor\n(n=793)'])

# Grade para melhor visualização
ax.yaxis.grid(True, linestyle='--', which='major', color='gray', alpha=0.7)
ax.set_axisbelow(True)

# Ajuste do layout
plt.tight_layout()
plt.show()
