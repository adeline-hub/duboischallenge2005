# week 1, 2025 - VALUE OF LAND OWNED BY GEORGIA NEGROES

# IMPORT LIBRAIRIES
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from IPython.display import SVG
import io
from PIL import Image
from cairosvg import svg2png    # pip install cairosvg

#IMPORT DATA
link = 'https://raw.githubusercontent.com/ajstarks/dubois-data-portraits/refs/heads/master/challenge/2025/challenge01/data.csv'
df = pd.read_csv(link)

# IMPORT BAG IMAGE
svg_path ='https://raw.githubusercontent.com/adeline-hub/duboischallenge2005/refs/heads/main/2025/1.%20Value%20of%20Land%20Owned%20by%20Georgia%20Negroes%20(plate%2018)/cashbag2%20(1).svg'
SVG(filename=svg_path)
def get_svg_image(svg_path, scale=1.0):
    png_bytes = svg2png(url=svg_path, scale=scale) # Convert SVG to PNG
    img = Image.open(io.BytesIO(png_bytes))
    return np.array(img)

# NORMALIZE BAG SIZES
df['size WEB'] = [2.5, 3, 3.5, 3.8, 4.2, 4.5] # W.E.B. Du Bois scale
df['size Matplotlib'] = df['size WEB'] *20

# BARPLOT CHART SIMPLE TO DESIGNED

#DESIGN PART 1
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_facecolor('#d9bda5')  # Set background color to old paper
plt.rcParams["font.family"] = "Liberation Sans"

# (BAR)PLOT

x_fixed = 5.0 # = UNIQUE BAR
ax.set_xlim(4, 6) 
padding = 4
ax.set_ylim(df['Year'].min() - 20, df['Year'].max() + 50)

y_positions = np.linspace(df['Year'].min(), df['Year'].max() + 40, len(df))
y_adjusted = df['Year'] - 7

#PLOT YEARS ONE BY ONE
for i, (_, row) in enumerate(df.iterrows()):
    y_pos = y_positions[i]
    image = get_svg_image(svg_path, scale=row['size Matplotlib'] / 100)
    imagebox = OffsetImage(image, zoom=0.3)
    ab = AnnotationBbox(imagebox, (x_fixed, y_pos), frameon=False, xycoords='data', box_alignment=(0.5, 0.5))
    ax.add_artist(ab)

# DESIGN PART 2
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)
plt.gca().invert_yaxis()


# ANNOTATIONS
plt.text(5, 1858, "VALUE OF LANDS OWNED BY GEORGIA NEGROES.", fontsize=12, fontweight="light", fontfamily="sans serif", color="black", ha="center", va="top")  # Align text center and top
plt.text(5, 1940, "matplotlib | #DuBoisChallenge2025 | nambo yang", fontsize=8, fontweight="light", fontfamily="sans serif", color="black", ha="center", va="top")  # Align text center and top

plt.text(4.85,1869,"$1,263,902", fontsize=9, fontweight="light", fontfamily="Liberation Serif", color="#404040")
plt.text(4.8,1881,"$1,522,173", fontsize=10, fontweight="light", fontfamily="Liberation Serif", color="#404040")
plt.text(4.8,1893,"$2,362,889", fontsize=10, fontweight="light", fontfamily="Liberation Serif", color="#404040")
plt.text(4.8,1905,"$3,485,176", fontsize=10, fontweight="light", fontfamily="Liberation Serif", color="#404040")
plt.text(4.8,1917,"$4,158,960", fontsize=10, fontweight="light", fontfamily="Liberation Serif", color="#404040")
plt.text(4.8,1929,"$4,220,120", fontsize=10, fontweight="light", fontfamily="Liberation Serif", color="#404040")

plt.text(4.9,1873,"1875", fontsize=10, fontweight="light", fontfamily="Liberation Serif", color="#404040")
plt.text(4.9,1885,"1880", fontsize=10, fontweight="light", fontfamily="Liberation Serif", color="#404040")
plt.text(4.9,1897,"1885", fontsize=10, fontweight="light", fontfamily="Liberation Serif", color="#404040")
plt.text(4.9,1909,"1890", fontsize=10, fontweight="light", fontfamily="Liberation Serif", color="#404040")
plt.text(4.9,1921,"1895", fontsize=10, fontweight="light", fontfamily="Liberation Serif", color="#404040")
plt.text(4.9,1934,"1899", fontsize=10, fontweight="light", fontfamily="Liberation Serif", color="#404040")



plt.show()
