import gathering



def get_total_case(country: str):
    ncov_data = gathering.gather_total_data()
    print(ncov_data[ncov_data['Country,Other'] == country ]['TotalCases'])
    return ncov_data[ncov_data['Country,Other'] == country ]['TotalCases']

def get_all_data(country: str):
    ncov_data = gathering.gather_total_data()
    print(ncov_data[ncov_data['Country,Other'] == 'France'])
    return ncov_data['Country,Other']
#print(ncov_data[ncov_data['TotalCases']>1000 ]['Country,Other'])

if __name__ == '__main__':

    df = get_total_case('France')

    print(df.shape)

    df2 = get_all_data('France')
    print(df2)