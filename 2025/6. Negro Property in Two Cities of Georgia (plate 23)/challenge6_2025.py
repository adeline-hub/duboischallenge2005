# 6. Negro Property in Two Cities of Georgia (plate 23)

# IMPORT LIBRAIRIES
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import image as mpimg

# IMPORT DATA
df = pd.read_csv('https://raw.githubusercontent.com/ajstarks/dubois-data-portraits/refs/heads/master/challenge/2025/challenge06/data.csv')

# DATA PROCESSING
#savannah = df[df['City'] == 'Savannah']
#atlanta = df[df['City'] == 'Atlanta']
savannah_sorted = savannah.sort_values('Year', ascending=True)
atlanta_sorted = atlanta.sort_values('Year', ascending=True)
years = df['Year'].unique()

# ----- (BAR) PLOT #1 - Vertical Bar Chart for Property Value -----

fig1, ax1 = plt.subplots(figsize=(11, 14))
width = 0.7

bars_savannah = ax1.bar(savannah['Year'] - width / 2, savannah['Property Value (Dollars)'], width, color='#f8c471', label='Savannah')
bars_atlanta = ax1.bar(atlanta['Year'] + width / 2, atlanta['Property Value (Dollars)'], width, color='#7fb3d5', label='Atlanta')

# LABELS
for bar in bars_savannah:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval / 2, f'${yval:,.0f}', ha='center', va='center', fontsize=10, color='black', rotation=90)
for bar in bars_atlanta:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval / 2, f'${yval:,.0f}', ha='center', va='center', fontsize=10, color='black', rotation=90)

# DESIGN 
for spine in ['top', 'right', 'left', 'bottom']:
    ax1.spines[spine].set_visible(False)
ax1.tick_params(axis='y', colors='white')
ax1.xaxis.set_visible(False)

# SAVE PLOT #1 AS PNG
plt.savefig('bar_n.png', bbox_inches='tight', transparent=True)
plt.close(fig1)

# ----- (BARH) PLOT #2 - Horizontal Bar Chart for Number of Owners -----

fig2, ax2 = plt.subplots(figsize=(11, 14))

bars_savannah_h = ax2.barh(savannah_sorted['Year'] - width / 2, savannah_sorted['Owners'], width, color='#f8c471', label='Savannah')
bars_atlanta_h = ax2.barh(atlanta_sorted['Year'] + width / 2, atlanta_sorted['Owners'], width, color='#7fb3d5', label='Atlanta')

# LABELS
for bar in bars_savannah_h:
    xval = bar.get_width()
    ax2.text(xval / 2, bar.get_y() + bar.get_height() / 2, f'{xval:,.0f}', va='center', ha='center', fontsize=10, color='black')
for bar in bars_atlanta_h:
    xval = bar.get_width()
    ax2.text(xval / 2, bar.get_y() + bar.get_height() / 2, f'{xval:,.0f}', va='center', ha='center', fontsize=10, color='black')

# DESIGN
ax2.invert_yaxis()  # 🔹 First year at the top!
for spine in ['top', 'right', 'left', 'bottom']:
    ax2.spines[spine].set_visible(False)
ax2.tick_params(axis='y', colors='white')
ax2.xaxis.set_visible(False)
ax2.legend(frameon=False, loc='upper right', bbox_to_anchor=(0.5, -0.2), ncol=2, fontsize=14)

# SAVE PLOT #2 AS PNG
plt.savefig('bar_m.png', bbox_inches='tight', transparent=True)
plt.close(fig2) 


# ----- OVERLAY BOTH PNGs -----

# LOAD PNGs
img_n = mpimg.imread('bar_n.png')
img_m = mpimg.imread('bar_m.png')

# DESIGN
fig3, ax3 = plt.subplots(figsize=(11, 13))
fig3.patch.set_facecolor('oldlace')
ax3.set_facecolor('oldlace') 
ax3.imshow(img_n, aspect='auto', extent=[0, 1, 0, len(df)], alpha=1)
ax3.imshow(img_m, aspect='auto', extent=[0, 1, 0, len(df)], alpha=1)
ax3.axis('off')

#ANNOTATIONS
ax3.plot([0.1, 0.9], [-0.3, -0.3], color='grey', linestyle='-', linewidth=1) 
ax3.plot([0.03, 0.03], [0.25, 5.5], color='grey', linestyle='-', linewidth=1) 
ax3.set_title("NEGRO PROPERTY IN TWO CITIES \nOF GEORGIA.\n", fontsize=18)
ax3.text(0.5, -0.9, "matplotlib | #DuBoisChallenge2025 | nambo yang", ha='center', fontsize=10, fontweight='light')
ax3.text(0.015, 2.5, "OWNERS.", ha='center', fontsize=13, fontweight='light', rotation=90, color='grey')
ax3.text(0.5, -0.5, "PROPERTY.", ha='center', fontsize=13, fontweight='light', color='grey')
ax3.text(0.578, 1.588, "768,", ha='center', fontsize=8.5, fontweight='light', rotation=90, color='black') #CORRECT

# SAVE FINAL PLOT #13 AS PNG
plt.savefig('final_overlay.png', bbox_inches='tight', transparent=False)

plt.show()
