# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 2024

@author: muril
"""

import matplotlib.pyplot as plt

# Dados atualizados
data = {
    'Normal (n=97)': {'low': 0.049, 'q1': 0.054, 'median': 0.058, 'q3': 0.062, 'high': 0.079},
    '21 - 40 Yrs (n=73)': {'low': 0.038, 'q1': 0.051, 'median': 0.057, 'q3': 0.061, 'high': 0.072},
    '41 - 60 Yrs (n=374)': {'low': 0.036, 'q1': 0.052, 'median': 0.057, 'q3': 0.063, 'high': 0.080},
    '61 - 80 Yrs (n=306)': {'low': 0.036, 'q1': 0.051, 'median': 0.056, 'q3': 0.062, 'high': 0.077},
    '81 - 100 Yrs (n=37)': {'low': 0.043, 'q1': 0.053, 'median': 0.055, 'q3': 0.064, 'high': 0.075}
}

# Preparação dos dados no formato necessário para o boxplot
formatted_data = [
    [data[key]['low'], data[key]['q1'], data[key]['median'], data[key]['q3'], data[key]['high']]
    for key in data
]

# Configuração das cores para os grupos
colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightyellow', 'lightpink']

# Configurando o boxplot
fig, ax = plt.subplots(figsize=(10, 6))

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
ax.set_xlabel('Age Groups', fontsize=12, fontweight='bold', color='darkblue')
ax.set_xticks(range(1, len(data) + 1))
ax.set_xticklabels(data.keys(), rotation=15, fontsize=10)

# Grade para melhor visualização
ax.yaxis.grid(True, linestyle='--', which='major', color='gray', alpha=0.7)
ax.set_axisbelow(True)

# Ajuste do layout
plt.tight_layout()
plt.show()
