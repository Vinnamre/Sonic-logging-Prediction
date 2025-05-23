# loader
import pandas as pd  # Data analysis library for handling structured data
import numpy as np  # Mathematical library for working with numerical data
from petrolib.file_reader import load_las

# # create list of wells to be used for analysis
# files = ['volve_field_data/15_9-F-11A.LAS', 'volve_field_data/16_5-3.las', 'volve_field_data/25_10-9.las', 'volve_field_data/34_11-1.las', 
#          'volve_field_data/35_4-1.las', 'volve_field_data/35_11-10.las', 'volve_field_data/35_11-11.las']


# Function to load a single well and return the dataframe and LAS object
def load_well(file, curves):
    well_df, las = load_las(file=file, return_csv=True, curves=curves)
    well_df = well_df.reset_index()  # Reset index for conformity
    return well_df, las

# Function to load all wells and return them individually
def load_all_wells(files):
    
    # Curves for wells (well1 has different curves)
    curves = ['GR', 'RDEP', 'NPHI', 'RHOB', 'DTC', 'DTS']
    
    # Load all wells and return them
    well1_df, las1 = load_well(files[0], ['GR', 'RT', 'NPHI', 'RHOB', 'DT', 'DTS'])
    well2_df, las2 = load_well(files[1], curves)
    well3_df, las3 = load_well(files[2], curves)
    well4_df, las4 = load_well(files[3], curves)
    well5_df, las5 = load_well(files[4], curves)
    well6_df, las6 = load_well(files[5], curves)
    well7_df, las7 = load_well(files[6], curves)
    
    # Wells that have RDEP and DTC in dataset
    well_column = {'DEPT':'DEPTH','GR':'GR', 'RDEP':'RT', 'NPHI':'NPHI', 'RHOB':'RHOB', 'DT':'DTC', 'DTS':'DTS'}
    well2_df.rename(columns=well_column, inplace=True)
    well3_df.rename(columns=well_column, inplace=True)
    well4_df.rename(columns=well_column, inplace=True)
    well5_df.rename(columns=well_column, inplace=True)
    well6_df.rename(columns=well_column, inplace=True)
    well7_df.rename(columns=well_column, inplace=True)

    # Wells that have RT and DT in dataset
    well_column1 = {'DEPT':'DEPTH','GR':'GR', 'RT':'RT', 'NPHI':'NPHI', 'RHOB':'RHOB', 'DT':'DTC', 'DTS':'DTS'}
    well1_df.rename(columns=well_column1, inplace=True)
    wells = [well1_df, well2_df, well3_df, well4_df, well5_df, well6_df, well7_df]

    return wells
