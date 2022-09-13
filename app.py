import pandas as pd 


# Load Data
state = pd.read_csv('data/NY_2019_ADI_9 Digit Zip Code_v3.1.csv', low_memory=False)
hospital = pd.read_csv('data/Hospital_Inpatient_Discharges__SPARCS_De-Identified___2015 (1).csv', low_memory=False)

# Print 
# print("DTYPES\nState: " + str(state.dtypes) + "Hospital: " + str(hospital.dtypes))
# print("COLUMNS\nState: " + str(state.columns) + "Hospital: " + str(hospital.columns))

state.columns
hospital.columns

state_small = state['ZIPID']

state['ZIPID'] = state['ZIPID'].str.slice(4, 7)
print(state_small.sample(10).to_markdown())



hospital_enriched = hospital[[
    'Zip Code - 3 digits',
    'Health Service Area',
    'Hospital County',
    'Facility Name',
    'Age Group',
    'Gender']]

state_enriched = state[[
    'ZIPID',
    'ADI_NATRANK',
    'ADI_STATERNK']]



combined_df = hospital_enriched.merge(state_enriched, how='left', left_on='Zip Code - 3 digits', right_on='ZIPID')
combined_df = pd.merge(state_enriched, how='left',  left_on='Zip Code - 3 digits', right_on='ZIPID')
### save to csv 
combined_df.to_csv('data/combined_df.csv')
combined_df.shape