"""
Gathers data from www.worldometers.info

"""

import pandas as pd

URL_ADD = 'https://www.worldometers.info/coronavirus'
ncov_data_cases = pd.read_html(URL_ADD)

ncov_data_df = ncov_data_cases[0]


def gather_total_data():
    URL_ADD = 'https://www.worldometers.info/coronavirus'
    ncov_data_cases = pd.read_html(URL_ADD)
    ncov_data_df = ncov_data_cases[0]
    return ncov_data_df

def gather_age_data():
    URL_ADD = 'https://www.worldometers.info/coronavirus/coronavirus-age-sex-demographics/'
    ncov_data_age = pd.read_html(URL_ADD)
    ncov_data_age_df = ncov_data_age[0]
    return ncov_data_age_df

def gather_sex_data():
    URL_ADD = 'https://www.worldometers.info/coronavirus/coronavirus-age-sex-demographics/'
    ncov_data_sex = pd.read_html(URL_ADD)
    ncov_data_sex_df = ncov_data_sex[1]
    return ncov_data_sex_df

def gather_precondition_data():
    URL_ADD = 'https://www.worldometers.info/coronavirus/coronavirus-age-sex-demographics/'
    ncov_data_precon = pd.read_html(URL_ADD)
    ncov_data_precon_df = ncov_data_precon[2]
    return ncov_data_precon_df






print(ncov_data_df[ncov_data_df['Country,Other']== 'Iran']['TotalCases'])



#df[df['job']=='unemployed']['education'].value_counts()

#df.to_csv('/Users/yigitbaser/Coronavirusmodel/dataCSV.csv', index=True)



#t = ncov_data.pd.DataFrame.to_csv("data")
#ncov_data.to_csv('/Users/yigitbaser/Coronavirusmodel', index=True)

