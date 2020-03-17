"""
Gathers data from www.worldometers.info

"""

import pandas as pd

URL_ADD = 'https://www.worldometers.info/coronavirus'
ncov_data_cases = pd.read_html(URL_ADD)

ncov_data_df = ncov_data_cases[0]
print(type(ncov_data_df))
#print(ncov_data_cases)

print(ncov_data_df[ncov_data_df['Country,Other']== 'Iran']['TotalCases'])



#df[df['job']=='unemployed']['education'].value_counts()

#df.to_csv('/Users/yigitbaser/Coronavirusmodel/dataCSV.csv', index=True)



#t = ncov_data.pd.DataFrame.to_csv("data")
#ncov_data.to_csv('/Users/yigitbaser/Coronavirusmodel', index=True)

