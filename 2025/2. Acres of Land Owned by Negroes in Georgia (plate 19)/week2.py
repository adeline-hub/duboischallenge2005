# week 2, 2025 - ACRES OF LAND OWNED BY NEGROES IN GEORGIA.

# IMPORT LIBRAIRIES
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#IMPORT DATA
linkk = 'https://raw.githubusercontent.com/ajstarks/dubois-data-portraits/refs/heads/master/challenge/2025/challenge02/data.csv'
df = pd.read_csv(linkk)

#DATA PROCESSING
df['Date']=df['Date'].astype('str')

# HORIZONTAL BARPLOT CHART SIMPLE TO DESIGNED

#DESIGN PART 1
fig, ax = plt.subplots(figsize=(12, 15)) # SIZE THE CHART
fig.patch.set_facecolor('oldlace') # OUTER COLOR
ax.set_facecolor('oldlace')  # INNER COLOR

# (HBAR)PLOT
plt.barh(df['Date'], df['Land'], color='#DC143C', height=0.6)
plt.gca().invert_yaxis()

# DESIGN PART 2
for spine in ['top', 'right', 'left', 'bottom']:
    ax.spines[spine].set_visible(False)
ax.tick_params(axis='y', colors='grey')
ax.xaxis.set_visible(False)
ax.grid(False)

# ANNOTATIONS
ax.text(0.5, 1, "ACRES OF LAND OWNED BY NEGROES\nIN GEORGIA.", fontsize=18, fontweight='light', fontname="Sans Serif", ha='center', va='top', transform=ax.transAxes, color="black")
ax.text(150000, 0, "338,769", fontsize=10, fontweight='light', color="black", va="center")
ax.text(400000, 24, "1,062,223", fontsize=10, fontweight='light', color="black", va="center")
ax.text(300000, 25, "matplotlib | #DuBoisChallenge2025 | nambo yang", fontsize=8, fontweight='light', color="black", va="center")

plt.show()

