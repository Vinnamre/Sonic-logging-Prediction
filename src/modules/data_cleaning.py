# data_cleaning
import pandas as pd
import numpy as np
from src.modules.data_loader import load_all_wells

# This function takes a DataFrame containing well log data and a list of log names. It then finds the start and 
# end values of each log based oncertain conditions (non-missing values). The function returns a new DataFrame containing
# the start and end values of each log, which can be used to trim the well log data accordingly.

# # create list of wells to be used for analysis
# files = ['volve_field_data/15_9-F-11A.LAS', 'volve_field_data/16_5-3.las', 'volve_field_data/25_10-9.las', 'volve_field_data/34_11-1.las', 
#          'volve_field_data/35_4-1.las', 'volve_field_data/35_11-10.las', 'volve_field_data/35_11-11.las']

# wells = load_all_wells (files)

def trim_log_values(df, depth_column, log_list):

    """
    Pick the start and end values of multiple logs based on the given conditions.

    Parameters:
    df (DataFrame): The pandas DataFrame containing the log data.
    column1 (str): The column from which to retrieve the values, 'DEPTH in this case'.
    log_list (list): A list of log names to determine the start and end of the logs.

    Returns:
    DataFrame: A pandas DataFrame containing the start and end values of each log.
    """
    trim_data = []
    
    for log in log_list:
        mask = df[log].notnull()  # Create a boolean mask where non-missing values in log are True
        start_index = mask.idxmax()  # Find the index of the first True value
        last_index = mask[::-1].idxmax()  # Find the index of the last True value by reversing the mask
        start_value = df.loc[start_index, depth_column]  # Retrieve the corresponding start value from column1(depth)
        end_value = df.loc[last_index, depth_column]  # Retrieve the corresponding end value from column1(depth)
        trim_data.append([log, start_value, end_value])
    
    trim_df = pd.DataFrame(trim_data, columns=['Log', 'Start Value', 'End Value'])
    return trim_df

def trim_wells(wells):
    
    # Load all wells and return them
    well1_trim = trim_log_values(wells[0], 'DEPTH', ['GR', 'RT', 'NPHI',  'RHOB','DTC', 'DTS'])
    well2_trim = trim_log_values(wells[1], 'DEPTH', ['GR', 'RT', 'NPHI',  'RHOB','DTC', 'DTS'])
    well3_trim = trim_log_values(wells[2], 'DEPTH', ['GR', 'RT', 'NPHI',  'RHOB','DTC', 'DTS'])
    well4_trim = trim_log_values(wells[3], 'DEPTH', ['GR', 'RT', 'NPHI',  'RHOB','DTC', 'DTS'])
    well5_trim = trim_log_values(wells[4], 'DEPTH', ['GR', 'RT', 'NPHI',  'RHOB','DTC', 'DTS'])
    well6_trim = trim_log_values(wells[5], 'DEPTH', ['GR', 'RT', 'NPHI',  'RHOB','DTC', 'DTS'])
    well7_trim = trim_log_values(wells[6], 'DEPTH', ['GR', 'RT', 'NPHI',  'RHOB','DTC', 'DTS'])

    trim_list = [well1_trim, well2_trim, well3_trim, well4_trim, well5_trim, well6_trim, well7_trim]
    
    return trim_list
    
    
    
def data_cleaning(trim_list, wells):
    well1 = wells[0].loc[(wells[0]['DEPTH'] >=  trim_list[0]['Start Value'].max() ) & (wells[0]['DEPTH'] <= trim_list[0]['End Value'].min())]
    well2 = wells[1].loc[(wells[1]['DEPTH'] >= trim_list[1]['Start Value'].max()) & (wells[1]['DEPTH'] <= trim_list[1]['End Value'].min())]
    well3 = wells[2].loc[(wells[2]['DEPTH'] >= trim_list[2]['Start Value'].max()) & (wells[2]['DEPTH'] <= trim_list[2]['End Value'].min())]
    well4 = wells[3].loc[(wells[3]['DEPTH'] >=  trim_list[3]['Start Value'].max()) & (wells[3]['DEPTH'] <= trim_list[3]['End Value'].min())]
    well5 = wells[4].loc[(wells[4]['DEPTH'] >=  trim_list[4]['Start Value'].max()) & (wells[4]['DEPTH'] <= trim_list[4]['End Value'].min())]
    well6 = wells[5].loc[(wells[5]['DEPTH'] >=  trim_list[5]['Start Value'].max()) & (wells[5]['DEPTH'] <= trim_list[5]['End Value'].min())]
    well7 = wells[6].loc[(wells[6]['DEPTH'] >=  trim_list[6]['Start Value'].max()) & (wells[6]['DEPTH'] <= trim_list[6]['End Value'].min())]
    
    # Dropping the missing values
    
    well1 = well1.dropna(how='any').reset_index(drop=True).sort_values('DEPTH')
    well2 = well2.dropna(how='any').reset_index(drop=True).sort_values('DEPTH')
    well3 = well3.dropna(how='any').reset_index(drop=True).sort_values('DEPTH')
    well4 = well4.dropna(how='any').reset_index(drop=True).sort_values('DEPTH')
    well5 = well5.dropna(how='any').reset_index(drop=True).sort_values('DEPTH')
    well6 = well6.dropna(how='any').reset_index(drop=True).sort_values('DEPTH')
    well7 = well7.dropna(how='any').reset_index(drop=True).sort_values('DEPTH')

    # Replacing the outliers
    well1['GR'] = np.where(well1['GR'] <= 200., well1['GR'], 200.)
    well1['RT'] = np.where(well1['RT'] <= 2000., well1['RT'], 107.)
    
    well2['GR'] = np.where(well2['GR'] <= 200., well2['GR'], 200.)
    well2['RT'] = np.where(well2['RT'] <= 2000., well2['RT'], 107.)
    
    well3['GR'] = np.where(well3['GR'] <= 200., well3['GR'], 200.)
    well3['RT'] = np.where(well3['RT'] <= 2000., well3['RT'], 107.)
    
    well4['GR'] = np.where(well4['GR'] <= 200., well4['GR'], 200.)
    well4['RT'] = np.where(well4['RT'] <= 2000., well4['RT'], 107.)
    
    well5['GR'] = np.where(well5['GR'] <= 200., well5['GR'], 200.)
    well5['RT'] = np.where(well5['RT'] <= 2000., well5['RT'], 107.)
    
    well6['GR'] = np.where(well6['GR'] <= 200., well6['GR'], 200.)
    well6['RT'] = np.where(well6['RT'] <= 2000., well6['RT'], 107.)
    
    well7['GR'] = np.where(well7['GR'] <= 200., well7['GR'], 200.)
    well7['RT'] = np.where(well7['RT'] <= 2000., well7['RT'], 107.)

    wells = [well1, well2, well3, well4, well5, well6, well7]
    return wells

































# # well_df = [well1_df, well2_df, well3_df, well4_df, well5_df, well6_df, well7_df]

# def trim_log_values(df, depth_column, log_list):

#     """
#     Pick the start and end values of multiple logs based on the given conditions.

#     Parameters:
#     df (DataFrame): The pandas DataFrame containing the log data.
#     column1 (str): The column from which to retrieve the values, 'DEPTH in this case'.
#     log_list (list): A list of log names to determine the start and end of the logs.

#     Returns:
#     DataFrame: A pandas DataFrame containing the start and end values of each log.
#     """
#     trim_data = []
    
#     for log in log_list:
#         mask = df[log].notnull()  # Create a boolean mask where non-missing values in log are True
#         start_index = mask.idxmax()  # Find the index of the first True value
#         last_index = mask[::-1].idxmax()  # Find the index of the last True value by reversing the mask
#         start_value = df.loc[start_index, depth_column]  # Retrieve the corresponding start value from column1(depth)
#         end_value = df.loc[last_index, depth_column]  # Retrieve the corresponding end value from column1(depth)
#         trim_data.append([log, start_value, end_value])
    
#     trim_df = pd.DataFrame(trim_data, columns=['Log', 'Start Value', 'End Value'])
#     return trim_df

# def trim_wells(wells):
    
#     # Load all wells and return them
#     well1_df = trim_log_values(wells[0], 'DEPTH', ['GR', 'RT', 'NPHI',  'RHOB','DTC', 'DTS'])
#     well2_df = trim_log_values(wells[1], 'DEPTH', ['GR', 'RT', 'NPHI',  'RHOB','DTC', 'DTS'])
#     well3_df = trim_log_values(wells[2], 'DEPTH', ['GR', 'RT', 'NPHI',  'RHOB','DTC', 'DTS'])
#     well4_df = trim_log_values(wells[3], 'DEPTH', ['GR', 'RT', 'NPHI',  'RHOB','DTC', 'DTS'])
#     well5_df = trim_log_values(wells[4], 'DEPTH', ['GR', 'RT', 'NPHI',  'RHOB','DTC', 'DTS'])
#     well6_df = trim_log_values(wells[5], 'DEPTH', ['GR', 'RT', 'NPHI',  'RHOB','DTC', 'DTS'])
#     well7_df = trim_log_values(wells[6], 'DEPTH', ['GR', 'RT', 'NPHI',  'RHOB','DTC', 'DTS'])
    
#     return well1_df, well2_df, well3_df, well4_df, well5_df, well6_df, well7_df
    

# # print(trim_wells(wells))