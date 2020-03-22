class Process():

    def __init__(self):
        version = 'firstVersion'

    def get_country_case_number(country :str,data_type:str,total_case_table):
        return total_case_table[total_case_table['Country,Other'] == country][data_type]

    def calculate_death_toll():
        pass
