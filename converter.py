import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm, rcParams
import os, glob


csv_files = glob.glob("*.csv") 
csv_files.sort()

fpath = os.path.join(rcParams["datapath"], "Helvetica.ttf")
prop = fm.FontProperties(fname=fpath)

for fyl in csv_files:

        fyl_pdf = fyl[:-4]+".pdf"

        if not os.path.exists(fyl_pdf):

                fig, ax = plt.subplots()

                # hide axes
                fig.patch.set_visible(False)
                ax.axis('off')
                ax.axis('tight')
                
                try:
                        
                        df = pd.read_csv(fyl, sep=',')
                        df_1 = df.sort_values(by = 'hhserial')
                        ax.table(cellText=df_1.values, colLabels=df_1.columns, cellLoc='left', loc='center')
                        fig.savefig(fyl_pdf, bbox_inches='tight')
                        print(  "Done - " + fyl_pdf)
                        plt.close(fig)
                        
                except:
                        
                        print(  "Error - " + fyl_pdf )
        else:

                print(  "Done - " + fyl_pdf)

