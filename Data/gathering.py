import pandas as pd


ncov_data_cases = pd.read_html('https://www.worldometers.info/coronavirus/', )

print(ncov_data_cases)

df = pd.DataFrame(ncov_data_cases)
print(df)

df.to_csv('/Users/yigitbaser/Coronavirusmodel/dataCSV.csv', index=True)



#t = ncov_data.pd.DataFrame.to_csv("data")
#ncov_data.to_csv('/Users/yigitbaser/Coronavirusmodel', index=True)

