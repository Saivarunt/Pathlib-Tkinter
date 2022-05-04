import pandas as pd 
import pathlib
p=pathlib.Path.cwd()
parts=[]
for i in p.rglob('*.*'):
    parts.append((i.name,i.suffix,i.parent))
c=['Name','Suffix','Parent']
i=len(parts)
df=pd.DataFrame(parts,columns=c,index=range(i))