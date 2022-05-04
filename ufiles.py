import main as m
from main import *
import pandas as pd
def ufiles(d):
    suflst=[]   
    indx=0
    for i in m.df['Parent'].values:
        if i==pathlib.Path(d):
            j=m.df['Suffix'].values[indx]
            suflst.append(j)
        indx=indx+1
    usuflst=pd.Series(suflst).unique()
    return usuflst