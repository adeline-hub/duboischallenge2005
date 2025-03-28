#WEBduBois_challenge_navy_8

# IMPORT LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import textwrap

# IMPORT DATA
df = pd.read_csv('https://raw.githubusercontent.com/ajstarks/dubois-data-portraits/refs/heads/master/challenge/2025/challenge08/data.csv')

# PROCESS DATA
df['Count_design'] = df['Count'].replace(98400, 63012)
df = df.sort_values(by="Count", ascending=True)
def split_label(label, width=13):
    wrapped = textwrap.wrap(label, width)
    max_lines = 2  
    if len(wrapped) < max_lines:
        wrapped.append("") 
    return "\n".join(wrapped)
df['Wrapped_Occupation'] = df['Occupation'].apply(lambda x: split_label(x))

# BARH PLOT
fig, ax = plt.subplots(figsize=(10, 13))
fig.patch.set_facecolor('oldlace')
ax.set_facecolor('oldlace')

bar_width = 0.4
bar_positions = np.arange(len(df), dtype=float)
spacing_indexes = [4,6,9,12,15,21]   #4 6 9 12 15 21
extra_space = 1.1

for index in spacing_indexes:
    bar_positions[index:] += extra_space  #

bars = ax.barh(bar_positions, df['Count_design'], height=bar_width, color='red', align='center')

# ANNOTATIONS
for bar, count in zip(bars, df['Count']):
    ax.text(-8000,
            bar.get_y() + bar.get_height() / 2,
            f"{int(count):,}", va='baseline', fontsize=12, color='grey')
for bar, label in zip(bars, df['Wrapped_Occupation']):
    ax.text(-16000,
            bar.get_y() + bar.get_height() / 2,
            label, va='center', ha='center', fontsize=11, color='grey')
ax.set_title("OCCUPATIONS OF GEORGIA NEGROES.", fontsize=18)
ax.text(30000, -1.5, "matplotlib | #DuBoisChallenge2025 | ade yang", ha='center', fontsize=12, fontweight='light')
ax.text(30000, 28.7, "MALES OVER 10", ha='center', color='grey', fontsize=14, fontweight='light')
ax.text(30000, 11, "1890.", ha='center', fontsize=18, fontweight='light', color='black')
ax.hlines(y=27, xmin=35588, xmax=63012, color='red', linestyle='-', linewidth=10)
ax.axvline(x=63012, ymin=0.928, ymax=0.947, color='red', linestyle='-', linewidth=10)
ax.axvline(x=5000, ymin=0.0519, ymax=0.67, color='grey', linestyle='-', linewidth=1)
ax.hlines(y=0, xmin=2000, xmax=5000, color='grey', linestyle='-', linewidth=1)
ax.hlines(y=19.01, xmin=2000, xmax=5000, color='grey', linestyle='-', linewidth=1)


# DESIGN
ax.set_xlabel("")
ax.set_ylabel("")
ax.set_yticks([])
ax.set_xticks([])
ax.spines['left'].set_color('oldlace')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.show()
