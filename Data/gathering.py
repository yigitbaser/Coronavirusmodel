import pandas as pd
import numpy as np

ncov_data_cases = pd.read_html('https://www.worldometers.info/coronavirus/')
print(type(ncov_data_cases))
#print(ncov_data_cases)
ncov_data_cases_arr = np.array(ncov_data_cases)
print(ncov_data_cases_arr.shape)

#df = ncov_data_cases[0]
#print(type(df))

#print(df[['Country','Cases']])

#df.to_csv('/Users/yigitbaser/Coronavirusmodel/dataCSV.csv', index=True)



#t = ncov_data.pd.DataFrame.to_csv("data")
#ncov_data.to_csv('/Users/yigitbaser/Coronavirusmodel', index=True)

