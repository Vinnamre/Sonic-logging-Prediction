from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import numpy as np
def print_metrics(y_true, y_predicted):
    
    ## Print the usual metrics and the R^2 values
    print('R^2                    = ' + str(r2_score(y_true, y_predicted)))
    print('Mean Square Error      = ' + str(mean_squared_error(y_true, y_predicted)))
    print('Root Mean Square Error = ' + str(np.sqrt(mean_squared_error(y_true, y_predicted))))
    print('Mean Absolute Error    = ' + str(mean_absolute_error(y_true, y_predicted)))