# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 13:55:46 2024

@author: muril
"""
import matplotlib.pyplot as plt

# Definição dos dados
data = {
    'Normal (n=114)': [0.044, 0.255, 0.469, 0.768, 1.48],
    '21-40 Yrs (n=97)': [0.912, 3.344, 5.042, 7.868, 14.421],
    '41-60 Yrs (n=505)': [0.195, 2.365, 4.228, 7.019, 16.833],
    '61-80 Yrs (n=431)': [0.054, 1.88, 3.207, 5.72, 12.583],
    '81-100 Yrs (n=54)': [0.464, 2.339, 3.478, 6.327, 11.196]
}

# Redesigned Boxplot with adjusted X-axis labels for better readability
fig, ax = plt.subplots(figsize=(8, 6))

# Redesigned boxplot with minimalistic style
ax.boxplot(data.values(),
           labels=[
               'Normal\n(n=114)',
               '21-40 Yrs\n(n=97)',
               '41-60 Yrs\n(n=505)',
               '61-80 Yrs\n(n=431)',
               '81-100 Yrs\n(n=54)'
           ],
           patch_artist=True,
           showmeans=True,
           widths=0.6,  # Adjusted width for better spacing
           boxprops=dict(facecolor='lightgray', edgecolor='darkblue', linewidth=1.5),
           whiskerprops=dict(color='darkblue', linestyle='-', linewidth=1.5),
           capprops=dict(color='darkblue', linewidth=1.5),
           flierprops=dict(marker='x', color='orange', markersize=8),
           meanprops=dict(marker='o', markerfacecolor='green', markersize=8))

# Adjusting title and labels with subtle font adjustments
ax.set_title('RAD54L Expression in BRCA Samples by Age', fontsize=14, fontweight='bold', color='darkblue')
ax.set_ylabel('Transcript per million (TPM)', fontsize=12, fontweight='bold', color='darkblue')
ax.set_xlabel('TCGA Samples', fontsize=12, fontweight='bold', color='darkblue')

# Setting grid for better readability
ax.yaxis.grid(True, linestyle='--', which='major', color='gray', alpha=0.7)
ax.set_axisbelow(True)

# Adjusting Y-axis range
ax.set_ylim(0, 20)

# Reduce the font size of x-axis labels for readability
plt.xticks(fontsize=10)

plt.tight_layout()
plt.show()
