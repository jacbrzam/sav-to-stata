# Convert SPSS data files (.sav) to Stata data files (.dta)
# Author: github.com/jacbrzam
#%% imports
import pandas as pd
import pyreadstat
import os
from tkinter.filedialog import askopenfilename
from tkinter import Tk

def replace_extension(filename):
    name, ext = os.path.splitext(filename)
    if ext.lower() == ".sav":
        return name + ".dta"
    else:
        raise Exception("File does not have .SAV extension.")

#%% open file dialog
root = Tk()
root.withdraw() # Hide the main window
root.call('wm', 'attributes', '.', '-topmost', True)

filename = askopenfilename()
outfile = replace_extension(filename) # output filename


#%% read file and process
df, meta = pyreadstat.read_sav(filename)

# truncate variable labels to 80 characters max
varlabels = {}
for col in range(len(meta.column_names)):
    varname = meta.column_names[col]
    varlabel = meta.column_labels[col]
    
    # set varlabel to varname if there's no varlabel
    if varlabel==None:
        varlabel = varname
    
    # truncate varlables to 80 characters
    varlabel = varlabel[0:80]
    varlabels[varname] = varlabel

# remove string variables from the value labels dictionary
value_labels = meta.variable_value_labels
for columna in df.columns.tolist():
    if columna in meta.variable_value_labels:
        if not pd.api.types.is_numeric_dtype(df.dtypes[columna]):
            print(f"The variable {columna} has value labels and is non-numeric. Its value labels will be dropped.")
            value_labels.pop(columna)

#%% save
df.to_stata(
    outfile,
    version=118,
    variable_labels=varlabels,
    value_labels=meta.variable_value_labels
    )

print("File '" + outfile + "' saved!")
