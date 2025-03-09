#DuBois_challenge_2025: ASSESSED VALUATION OF ALL TAXABLE PROPERTY OWNED BY GEORGIA NEGROES .

#to update with annotation text rotation :)

#IMPORT USEFULL LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#IMPORT DATA
df = pd.read_csv('https://raw.githubusercontent.com/ajstarks/dubois-data-portraits/refs/heads/master/challenge/2025/challenge05/data.csv')

# DATA PROCESSING
sizes2 = [300]
sizes3 = [300]
sizes4 = [100]
sizes5 = [100]
sizes6 = [100]
colors = ['black', 'grey', 'blue', '#f0bd13', 'oldlace', '#c0392b'] # DEFINE COLORS
central_color = 'black'  # Set the color of the central circle

#DESIGN PART #1
fig, ax = plt.subplots(figsize=(10, 13)) # SIZE THE CHART
fig.patch.set_facecolor('oldlace') # OUTER COLOR
ax.set_facecolor('oldlace')  # INNER COLOR

# (MULTIPLE PIE) PLOT
ax.pie([1], radius=0.9, colors=[central_color], startangle=90, wedgeprops={'edgecolor': 'black'})

ax.pie(sizes2, colors=[colors[1]], startangle=90, wedgeprops={'width': 0.35, 'edgecolor': 'grey'}, radius=0.8)
ax.pie(sizes3, colors=[colors[2]], startangle=90, wedgeprops={'width': 0.45, 'edgecolor': 'grey'}, radius=1.0)
ax.pie(sizes4, colors=[colors[3]], startangle=90, wedgeprops={'width': 0.35, 'edgecolor': 'grey'}, radius=1.1)
ax.pie(sizes5, colors=[colors[4]], startangle=90, wedgeprops={'width': 0.10, 'edgecolor': 'grey'}, radius=1.2)
ax.pie(sizes6, colors=[colors[5]], startangle=90, wedgeprops={'width': 0.10, 'edgecolor': 'grey'}, radius=1.3)

ax.set_aspect('equal')
ax.axis('off')

# ANNOTATIONS

ax.text(0.25, 0.90, "   $13,447,423", fontsize=11, fontweight='light', fontname="Sans Serif", ha='left', va='top', transform=ax.transAxes, color="black", rotation=-50, bbox=dict(facecolor='#c0392b', edgecolor='#c0392b', boxstyle='rarrow,pad=1.2'))
ax.text(0.65, 0.85, "   $12,941,230", fontsize=11, fontweight='light', fontname="Sans Serif", ha='left', va='top', transform=ax.transAxes, color="black", rotation=50, bbox=dict(facecolor='oldlace', edgecolor='oldlace', boxstyle='larrow,pad=1.2'))
ax.text(0.67, 0.5, "   $12,322,003", fontsize=11, fontweight='light', fontname="Sans Serif", ha='left', va='top', transform=ax.transAxes, color="black", rotation=0, bbox=dict(facecolor='#f0bd13', edgecolor='#f0bd13', boxstyle='larrow,pad=1'))
ax.text(0.52, 0.4, "   $8,153,390", fontsize=11, fontweight='light', fontname="Sans Serif", ha='left', va='top', transform=ax.transAxes, color="white", rotation=-52, bbox=dict(facecolor='blue', edgecolor='blue', boxstyle='larrow,pad=0.9'))
ax.text(0.35, 0.5, "   $5,764,293", fontsize=11, fontweight='light', fontname="Sans Serif", ha='left', va='top', transform=ax.transAxes, color="black", rotation=49, bbox=dict(facecolor='grey', edgecolor='grey', boxstyle='rarrow,pad=0.8'))
ax.text(0.525, 0.5, "$5,393,885", fontsize=11, fontweight='light', fontname="Sans Serif",ha='center', va='top', transform=ax.transAxes, color="white", rotation=0)

ax.text(0.5, 0.35, "1875", fontsize=11, fontweight='light', fontname="Sans Serif",ha='center', va='top', transform=ax.transAxes, color="white", rotation=0)
ax.text(0.5, 0.31, "1880", fontsize=11, fontweight='light', fontname="Sans Serif",ha='center', va='top', transform=ax.transAxes, color="white", rotation=0)
ax.text(0.5, 0.23, "1885", fontsize=11, fontweight='light', fontname="Sans Serif",ha='center', va='top', transform=ax.transAxes, color="white", rotation=0)
ax.text(0.5, 0.10, "1890", fontsize=11, fontweight='light', fontname="Sans Serif",ha='center', va='top', transform=ax.transAxes, color="black", rotation=0)
ax.text(0.5, 0.05, "1895", fontsize=11, fontweight='light', fontname="Sans Serif",ha='center', va='top', transform=ax.transAxes, color="black", rotation=0)
ax.text(0.5, 0.01, "1899", fontsize=11, fontweight='light', fontname="Sans Serif",ha='center', va='top', transform=ax.transAxes, color="white", rotation=0)

ax.text(0.5, -0.07, "matplotlib | #DuBoisChallenge2025 | nambo yang", fontsize=10, fontweight='light', fontname="Sans Serif", ha='center', va='top', transform=ax.transAxes, color="black")

#DESIGN PART #2
ax.set_title("ASSESSED VALUATION OF ALL TAXABLE PROPERTY \nOWNED BY GEORGIA NEGROES .\n", fontsize=18)


plt.show()
