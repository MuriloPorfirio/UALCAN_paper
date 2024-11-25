# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 10:29:29 2024

@author: muril
"""
import matplotlib.pyplot as plt
import numpy

# Definição dos dados
data = {
    'Normal (n=114)': [0.044, 0.255, 0.469, 0.768, 1.48],
    'Primary Tumor (n=1097)': [0.054, 2.132, 3.835, 6.627, 14.885]
}

# Redesigned Boxplot for a distinct appearance
fig, ax = plt.subplots(figsize=(6, 4))

# Redesigned boxplot with minimalistic style
ax.boxplot(data.values(),
           labels=data.keys(),
           patch_artist=True,
           showmeans=True,
           widths=0.4,  # Box width adjusted for a cleaner look
           boxprops=dict(facecolor='lightgray', edgecolor='darkblue', linewidth=1.5),
           whiskerprops=dict(color='darkblue', linestyle='-', linewidth=1.5),
           capprops=dict(color='darkblue', linewidth=1.5),
           flierprops=dict(marker='x', color='orange', markersize=8),
           meanprops=dict(marker='o', markerfacecolor='green', markersize=8))

# Adjusting title and labels with subtle font adjustments
ax.set_title('RAD54L Expression in BRCA Samples', fontsize=14, fontweight='bold', color='darkblue')
ax.set_ylabel('Transcript per million', fontsize=12, fontweight='bold', color='darkblue')
ax.set_xlabel('TCGA Samples', fontsize=12, fontweight='bold', color='darkblue')

# Setting grid for better readability
ax.yaxis.grid(True, linestyle='--', which='major', color='gray', alpha=0.7)
ax.set_axisbelow(True)

# Adjusting Y-axis range and removing unnecessary X-axis space
ax.set_ylim(0, 20)
ax.set_xlim(0.5, 2.5)

plt.tight_layout()
plt.show()

#Data: https://docs.google.com/spreadsheets/d/13Fi67hzRoLHzUK2buELFx-iVlolIGMGOhLHwqKCP5Y4/edit?usp=sharing
