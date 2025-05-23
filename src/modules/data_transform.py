# data_transformation
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

def data_transformation(wells):
    welldata = pd.concat((wells[0], wells[1],wells[2],wells[3],wells[4],wells[5],wells[6]), axis='index').reset_index(drop=True)

    # Transform RT values to the conventional logrithm values
    welldata['RT'] = np.log10(welldata['RT'])

    # Standardize the features(train data)
    scaler = StandardScaler()
    features = welldata.drop(['DTC','DTS'], axis=1)
    target = welldata[['DTC','DTS']]
    new_welldata = scaler.fit_transform(features)

    # View the standardized features
    new_df = pd.DataFrame(new_welldata, columns=features.columns)

    # View both the standardized features and the non-standardized target together
    new_df['DTC'] = target['DTC']
    new_df['DTS'] = target['DTS']

    return new_df