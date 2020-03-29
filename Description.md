# NCOV-19 STATISTICS AND MODELLING 
This code includes functions and data to make 
mathematical model of NCOV-19. 

Models to apply:
- SIR Model
- SIRS Model

-Prediction:
- NNs
- ML 

Data Sources:

1) Worldometers.info
2) *Research: Other modules

##Functions
1) Generate Database: Generates the folders and saves the data into csv files.
2) Update Database: Updates the database and metrics adn record as a time-series


##Data Types

There are 

###From Wordometers
1. Main Data: 
    | Country | TotalCases | NewCases | TotalDeaths 
    | NewDeaths | TotalRecovered | ActiveCases | 
    (Serious,Critical) | (Tot Cases/1M Pop)  | (Deaths / 1M Pop)
2. Age Distribution: Age/DeathRate(ConfirmedCases)/DeathRate(AllCases)
3. Sex: Sex/DeathRate(ConfirmedCases)/DeathRate(AllCases)
4. Precondition
5. Total Deaths
6. Daily Deaths
 

###Calculated by functions
* NOTE: Stored in DB, updated by fcn
1. Cases vs time by country
2. Death vs time by country
3. Growth Factor
    * Growth Factor by country
    * Growth Factor worldwide
4. 

    
COMPARE COUNTRIES FIRST DAY PERFORMANCE
    PER 1M PEOPLE


##CASE GRAPHS
- TotalCases graph worldwide 
- Daily new cases worldwide
- growth factor of daily new cases
- total cases excluding mainland china
- daily cases excluding mainland china
- growth factor excluding mainland china
- total cured
- newly infected vs newly recovered
- serious and critical cases
- outcome of cases(recovery or death)

##DEATH GRAPHS
- Total deaths
- daily deaths
- daily deaths growth factor
- total deaths of coronavirus



##
##Stats by country
- Total Cases(total cases vs. time)
- daily new cases(daily case vs. time)
- active cases(active case vs. time)
- 
- Total deaths(total deaths vs. time)
- daily deaths(daily deaths vs. time)
-
- newly infected vs. newly recovered
- outcome of cases(recovery and death rate vs. time)


##MODELLING
SIR MODEL



##




