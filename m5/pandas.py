 import pandas as pd
import numpy as np


index = 'r1 r2 r3 r4 r5 r6 r7 r8 r9 r10'.split()
columns = 'c1 c2 c3 c4 c5 c6 c7 c8 c9 c10'.split()
&#9989; *Use **TAB** for auto-complete and **shift + TAB**  for doc.*
# How the index, columns and array_2d look like!
index
columns
### Using arange make a 2d array (10, 10) of 100 to 0 values. 
arrary_2d=np.arange(100,0,-1).reshape(10,10)

array_2d
# create a DataFrame using index, columns and array_2d now 
ind = 'r1 r2 r3 r4 r5 r6 r7 r8 r9 r10'.split()   
col = 'c1 c2 c3 c4 c5 c6 c7 c8 c9 c10'.split()
df=pd.DataFrame(data=arrary_2d,index=ind, columns=col)

# How the DataFrame look like!
df  # select * from df      
**df** is our first dataframe. <br>
We have columns, c1 to c10, and their corresponding rows, r1 to r10. <br>
Each column is actually a pandas series, sharing a common index (row labels). <br>

&#9758; Let's learn how to **Grab data** that we need, this is the most important thing we want to learn to move one!<br>

### Grab a single column c10 
df['c10']

### Grab multiple columns c4, c2, c9
df[['c4','c2','c9']]

### Add a new column name 'new' and value would be c1 * c10
df['new']= df['c1'] * df['c10']  # select *, (c1 * c10) as new from df

### Delete the column 'new' permanently  
df.drop('new', axis=1, inplace=True)


### Grabb more than one rows 'r2', 'r1','r3'
df.loc[['r2','r1', 'r3']]  

### Grab a sub-set of the dataframe where c1 is less than 50
df[df['c1']<50]

### Grab a sub-set of the dataframe where c3 is equal to 38 and c8 is equal to 33
result = df[(df['c3']==38) & (df['c8']==33)]
result

