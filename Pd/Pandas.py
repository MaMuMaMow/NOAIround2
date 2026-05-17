import pandas as pd

a = pd.DataFrame({'YES':[50,21], 'NO':[131,2]})
a.to_csv('test.csv')