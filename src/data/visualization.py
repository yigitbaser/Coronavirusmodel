import pandas as pd
import src.Utils.Loader
import matplotlib as plt
import gathering

plt.close('all')

plt.figure()
df = pd.read_csv('/Users/yigitbaser/Coronavirusmodel/Storage/2020-03-18/TotalTable_1933.csv')
#df.plot(x='Country,Other',y='TotalCases',kind='scatter')
#plt.show()