import pandas as pd

def analyze_data(filepath):

    df = pd.read_csv(filepath)

    #fill the code 
    

    #return a dictionary with the following keys
    # 'num_rows': number of rows in the DataFrame
    # 'num_columns': number of columns in the DataFrame
    # 'column_with_max_mean': name of the column with the maximum mean value;

    #TO DO: implement the logic
    num_rows = None
    num_columns = None
    column_with_max_mean = None

    return {
        'num_rows': num_rows,
        'num_columns': num_columns,
        'column_with_max_mean': column_with_max_mean
    }