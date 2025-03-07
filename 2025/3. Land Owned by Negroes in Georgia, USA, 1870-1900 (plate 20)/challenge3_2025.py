# week 3, 2025 - LAND OWNED BY NEGROES IN GEORGIA, U.S.S. 1870-1900

# IMPORT LIBRAIRIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd     # pip install geopandas

#IMPORT DATA
link = 'https://raw.githubusercontent.com/ajstarks/dubois-data-portraits/refs/heads/master/challenge/2025/challenge03/data.csv'
df = pd.read_csv(link)

#IMPORT GEODATA
gdf = gpd.read_file('/content/drive/My Drive/dataviz_challenge_du_bois/georgia-1880-county-shapefile/DuBoisChallenge - Georgia Counties w 1870 & 1880 data.shp') # copy in folder

#IMPORT COLORS DATA DF 
df_colors = pd.read_csv('https://raw.githubusercontent.com/adeline-hub/duboischallenge2005/refs/heads/main/2025/3.%20Land%20Owned%20by%20Negroes%20in%20Georgia%2C%20USA%2C%201870-1900%20(plate%2020)/challenge03_colors.csv')

#DATA PROCESSING

#MERGE 3:  DATA, COLORS DF, AND GEODATA IN A UNIQUE DATAFRAME
merged_gdf = gdf.merge(df[['County1890', 'Acres 1899']],
                       left_on='NHGISNAM',
                       right_on='County1890',
                       how='left')
df_final = pd.merge(merged_gdf, 
                    df_colors, 
                    on='County1890', 
                    how='left')

# MAP CHART SIMPLE TO DESIGNED

#DESIGN PART 1
fig, ax = plt.subplots(figsize=(12, 12))
fig.patch.set_facecolor('oldlace') # OUTER COLOR
ax.set_facecolor('oldlace')  # INNER COLOR
for spine in ['top', 'right', 'left', 'bottom']:
    ax.spines[spine].set_visible(False)
    
# (MAP)PLOT
for idx, row in df_final.iterrows():  
    if row['geometry'].geom_type == 'MultiPolygon':
        centroid = row['geometry'].representative_point()  
    else:
        centroid = row['geometry'].centroid

    ax.text(centroid.x, centroid.y, str(int(row['Acres 1899_x'])),
            fontsize=8, ha='center', va='center', color='black')

# DESIGN PART 2
ax.tick_params(axis='y', colors='white')
ax.xaxis.set_visible(False)
ax.grid(False)

# ANNOTATIONS
ax.text(0.5, 0.98, "LAND OWNED BY NEGROES IN GEORGIA, U.S.S. 1870-1900.", fontsize=16, fontweight='light', fontname="Sans Serif", ha='center', va='top', transform=ax.transAxes, color="black")
ax.text( 0.8, 0.8, "THE FIGURES INDICATES THE NUMBER OF \n ACRES OWNED IN EACH COUNTY IN 1899.", fontsize=8, fontweight='light', fontname="Sans Serif", ha='center', va='top', transform=ax.transAxes, color="grey")
ax.text(0.5, 0.04, "matplotlib | #DuBoisChallenge2025 | nambo yang", fontsize=8, fontweight='light', fontname="Sans Serif", ha='center', va='top', transform=ax.transAxes, color="black")

plt.show()


