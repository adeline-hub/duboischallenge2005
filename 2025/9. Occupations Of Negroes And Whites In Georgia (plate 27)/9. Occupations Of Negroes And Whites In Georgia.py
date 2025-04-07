# IMPORT LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# PROCESS DATA

# Create an updated Percentage column
df['Degrees'] = df['Percentage']*112.5/100

# Append the ghost part of the pie adding new rows
new_rows = [
    {"Group": "Ghost", "Occupation": "Whisper1", "Percentage": 0.0, "Degrees": 67.5},
    {"Group": "Ghost", "Occupation": "Whisper2", "Percentage": 0.0, "Degrees": 67.5}
]
new_rows_df = pd.DataFrame(new_rows)
df = pd.concat([df, new_rows_df], ignore_index=True)

df['Percentage updated'] = round(df['Degrees']*100/360,1)
df['Color'] = ['#DC143C', '#2b67c0', '#ffcc00', '#c0842b', 'oldlace','#DC143C', '#2b67c0', '#ffcc00', '#c0842b', 'oldlace', 'oldlace', 'oldlace' ]

# reindex the dataframe
df = df.reindex(index=[0, 10, 8, 9, 6, 7, 5, 11, 3, 4, 1, 2]).reset_index(drop=True)

# PIE PLOT 
percentages = df.loc[df.index, "Percentage updated"]
labels = df.loc[df.index, "Occupation"]
colors = df.loc[df.index, "Color"]

fig, ax = plt.subplots(figsize=(10, 10))
ax.pie(
    percentages,
    #labels=labels,
    colors=colors,
    startangle=75,
    wedgeprops=dict(edgecolor='oldlace')
)
# DESIGN
fig.patch.set_facecolor('oldlace') 
ax.set_facecolor('oldlace')  


# ANNOTATIONS
ax.text(0.3, 0.55, "AGRICULTURE, FISHERIES\nAND MINING", fontsize=9, fontweight='light', fontname="Sans Serif",ha='center', va='top', transform=ax.transAxes, color="grey", rotation=0)
ax.text(0.3, 0.47, "MANUFACTURING AND\nMECHANICAL INDUSTRIES", fontsize=9, fontweight='light', fontname="Sans Serif",ha='center', va='top', transform=ax.transAxes, color="grey", rotation=0)
ax.text(0.8, 0.6, "DOMESTIC AND\nPERSONAL SERVICE", fontsize=9, fontweight='light', fontname="Sans Serif",ha='right', va='top', transform=ax.transAxes, color="grey", rotation=0)
ax.text(0.8, 0.4, "TRADE AND\nTRANSPORTATION", fontsize=9, fontweight='light', fontname="Sans Serif",ha='right', va='top', transform=ax.transAxes, color="grey", rotation=0)
ax.text(0.8, 0.5, "PROFESSIONS", fontsize=9, fontweight='light', fontname="Sans Serif",ha='right', va='top', transform=ax.transAxes, color="grey", rotation=0)

ax.text(0.17, 0.55, " ", fontsize=11, fontweight='light', fontname="Sans Serif", ha='left', va='top', transform=ax.transAxes, color="#2b67c0", rotation=0, bbox=dict(facecolor='#2b67c0', edgecolor='grey', boxstyle='circle,pad=0.8'))
ax.text(0.17, 0.45, " ", fontsize=11, fontweight='light', fontname="Sans Serif", ha='left', va='top', transform=ax.transAxes, color="#DC143C", rotation=0, bbox=dict(facecolor='#DC143C', edgecolor='grey', boxstyle='circle,pad=0.8'))
ax.text(0.83, 0.6, " ", fontsize=11, fontweight='light', fontname="Sans Serif", ha='left', va='top', transform=ax.transAxes, color="#ffcc00", rotation=0, bbox=dict(facecolor='#ffcc00', edgecolor='grey', boxstyle='circle,pad=0.8'))
ax.text(0.83, 0.5, " ", fontsize=11, fontweight='light', fontname="Sans Serif", ha='left', va='top', transform=ax.transAxes, color="#c0842b", rotation=0, bbox=dict(facecolor='#c0842b', edgecolor='grey', boxstyle='circle,pad=0.8'))
ax.text(0.83, 0.4, " ", fontsize=11, fontweight='light', fontname="Sans Serif", ha='left', va='top', transform=ax.transAxes, color="oldlace", rotation=0, bbox=dict(facecolor='oldlace', edgecolor='grey', boxstyle='circle,pad=0.8'))


ax.text(0.5, 0.09, "WHITES", fontsize=12, fontweight='light', fontname="Sans Serif",ha='center', va='top', transform=ax.transAxes, color="grey", rotation=0)
ax.text(0.5, 0.93, "NEGROES", fontsize=12, fontweight='light', fontname="Sans Serif",ha='center', va='top', transform=ax.transAxes, color="grey", rotation=0)

ax.text(0.4, 0.85, "62%", fontsize=11, fontweight='light', fontname="Sans Serif",ha='center', va='top', transform=ax.transAxes, color="#36454F", rotation=0)
ax.text(0.78, 0.75, "5%", fontsize=11, fontweight='light', fontname="Sans Serif",ha='center', va='top', transform=ax.transAxes, color="#36454F", rotation=0)
ax.text(0.68, 0.8, "28%", fontsize=11, fontweight='light', fontname="Sans Serif",ha='center', va='top', transform=ax.transAxes, color="#36454F", rotation=0)
ax.text(0.82, 0.69, "0.5%", fontsize=11, fontweight='light', fontname="Sans Serif",ha='center', va='top', transform=ax.transAxes, color="#36454F", rotation=0)
ax.text(0.8, 0.72, "4.5%", fontsize=11, fontweight='light', fontname="Sans Serif",ha='center', va='top', transform=ax.transAxes, color="#36454F", rotation=0)
ax.text(0.6, 0.16, "64%", fontsize=11, fontweight='light', fontname="Sans Serif",ha='center', va='top', transform=ax.transAxes, color="#36454F", rotation=0)
ax.text(0.30, 0.2, "13.5%", fontsize=11, fontweight='light', fontname="Sans Serif",ha='center', va='top', transform=ax.transAxes, color="#36454F", rotation=0)
ax.text(0.37, 0.16, "5.5%", fontsize=11, fontweight='light', fontname="Sans Serif",ha='center', va='top', transform=ax.transAxes, color="#36454F", rotation=0)
ax.text(0.18, 0.3, "4%", fontsize=11, fontweight='light', fontname="Sans Serif",ha='center', va='top', transform=ax.transAxes, color="#36454F", rotation=0)
ax.text(0.235, 0.24, "13%", fontsize=11, fontweight='light', fontname="Sans Serif",ha='center', va='top', transform=ax.transAxes, color="#36454F", rotation=0)

ax.text(0.5, -0.07, "matplotlib | #DuBoisChallenge2025 | ade yang", fontsize=10, fontweight='light', fontname="Sans Serif", ha='center', va='top', transform=ax.transAxes, color="black")


plt.title("\nOCCUPATIONS OF NEGROES AND WHITES IN GEORGIA.", fontsize=16, fontweight='bold')

plt.tight_layout()
plt.show()
