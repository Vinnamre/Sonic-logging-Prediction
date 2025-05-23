# data_splitting

def data_splitting(wells, total_well):
    # Divide the welldata back to train and test, since we are done standardizing our features
    train = total_well.iloc[:len(wells[0])+ len(wells[1])+ len(wells[2])+ len(wells[3]) + len(wells[4]) + len(wells[5])]
    test = total_well.iloc[len(wells[0])+ len(wells[1])+ len(wells[2])+ len(wells[3]) + len(wells[4]) + len(wells[5]):]
    
    # Separate the features and target variables
    train_x = train.drop(['DTC','DTS'], axis=1)
    train_y = train[['DTC', 'DTS']]
    
    test_x = test.drop(['DTC','DTS'], axis=1)
    test_y = test[['DTC','DTS']]

    return train_x, train_y, test_x, test_y

