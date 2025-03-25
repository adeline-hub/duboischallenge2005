#IMPORT LIBRARIES
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#IMPORT DATA OF WEEK 7 :)
link = 'https://raw.githubusercontent.com/ajstarks/dubois-data-portraits/refs/heads/master/challenge/challenge07/data.csv'
df=pd.read_csv(link)

# PROCESS DATA
df['STANDARDIZATION'] = df['Houshold Value (Dollars)'] / df['Houshold Value (Dollars)'].max()

#(TURTLE)PLOT FUNCTION
def turtle_draw(percentage, which_level, bar_width):
    start_t = 8.6
    end_t = 20.42
    t = np.arange(start_t + ((1 - percentage) * (end_t - start_t)), end_t, 0.001)
    correction = 1 + which_level * bar_width / t
    correction2 = 1 + (which_level + 1) * bar_width / t
    x_outer = t * np.cos(t)
    y_outer = t * np.sin(t)
    x_inner = np.flip(t) * np.cos(np.flip(t))
    y_inner = np.flip(t) * np.sin(np.flip(t))
    x = np.concatenate([x_outer * correction2, x_inner * np.flip(correction)])
    y = np.concatenate([y_outer * correction2, y_inner * np.flip(correction)])    
    return x, y

#(TURTLE)PLOT 
fig, ax = plt.subplots(figsize=(10, 13))
fig.patch.set_facecolor('oldlace') 
ax.set_facecolor('oldlace') 
colors = ['#F08080', 'lightgrey', '#ccbdbd', '#ef9702', '#eeeeee', 'red']
for i in range(6):
    x, y = turtle_draw(df['STANDARDIZATION'][i], 6 - i, 0.9)
    ax.fill(x, y, color=colors[i], edgecolor='black', linewidth=0.1)

# ANNOTATIONS
ax.set_title('ASSESSED VALUE OF HOUSEHOLD AND KITCHEN FURNITURE\nOWNED BY GEORGIA NEGROES', fontsize=18)
ax.text(0,-25, "matplotlib | #DuBoisChallenge2025 | ade yang", ha='center', fontsize=10, fontweight='light')
for i, year in enumerate(df['Year'].sort_values(ascending=False).values[:6]):
    ax.text(-10, 20.5 + (i + 1), f"{year}-${df['Houshold Value (Dollars)'].iloc[i]:,.0f}",
            horizontalalignment='left', fontsize=8, color='grey')

# DESIGN THE CHART
ax.set_aspect('equal')
ax.set_axis_off()
plt.show()
