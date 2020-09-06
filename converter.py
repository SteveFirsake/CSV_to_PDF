import pandas as pd
import matplotlib.pyplot as plt
import os, glob

fig, ax = plt.subplots()

# hide axes
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

for fyl in glob.glob("*.csv"):
    df = pd.read_csv(fyl, sep=',')
    ax.table(cellText=df.values, colLabels=df.columns, cellLoc='left', loc='center')
    fyl_pdf = fyl[:-4]+".pdf"
    fig.savefig(fyl_pdf, bbox_inches='tight')

