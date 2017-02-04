
# coding: utf-8

# In[1]:

"""
Wrapper methods around "import csv" that
are very specific to p3.
Created by Uki D. Lucas on Feb. 4, 2017
"""

# TODO implement batch_from, batch_to - I did not need it for 8037 rows
# TODO implement has_header_row
def read_csv(file_path):
    """
    Usage:
    headers, data = read_csv(file_path)
    Parameter: 
    - file_path: can be relative path "../../../DATA/stuff.csv"
    Returns:
    - headers: array of strings e.g. ['steering', 'throttle', 'brake', 'speed']
    - data: array of strings, you have to convert values to int, float yourself
   test_read_csv()
    """
    import csv
    # Opening spreadsheet to read in TEXT mode: 'rt'
    with open(file_path, 'rt') as csvfile:
        # Most common format of CSV, TODO improve
        payload = csv.reader(csvfile, delimiter=',', quotechar='"') 
        row_counter = 0
        headers = []
        data = []
        for row in payload:
            row_counter = row_counter + 1
            
            if row_counter == 1:
                headers = row
                # print (type(row))
                # print ( row)
                # print ('\t '.join(row))
            elif 1 < row_counter < 3:
                # print (type(row))
                # print ( row)
                # print ('\t '.join(row))
                data.append(row)
            else:
                data.append(row)
        print("row_counter", row_counter)
        return headers, data
    
    
    
def test_read_csv():
    """
    This test is specific to Uki's enviroment.
    """
    data_dir = "../../../DATA/behavioral_cloning_data/"
    headers, data = read_csv(file_path = data_dir + 'driving_log.csv')
    print("headers \n",headers)
    print("3rd row of data \n",data[2:3])
#test_read_csv()


# In[20]:

def split_random(matrix, percentage_train=70, percent_test=15):
    """
    Splits matrix data into random sets.
    Returns:
    - training_data: percentage_train e.g. 70%
    - testing_data: percent_test e.g. 15%
    - validation_data: reminder from 100% e.g. 15%
    """
    percent_validation = 100 - percentage_train - percent_test
   
    if percent_validation < 0:
        print("Make sure that the provided sum of " +         "training and testing percentages is equal, " +         "or less than 100%.")
    else:
        print("percent_validation",percent_validation)
        
    matrix = np.random.RandomState(43) # seed 43
    print(matrix.shape)
    indices = np.arange(n_samples)
    rng.shuffle(indices)
    training_data = x[indices]
    testing_data = y[indices]
    validation_data = z[indices]

training_data, testing_data, validation_data = split_random([], percentage_train=70, percent_test=15) 


# In[2]:

def get_image_center_values(matrix):
    column_image_center = 0
    return [row[column_image_center] for row in matrix]

def get_image_left_values(matrix):
    column_image_left = 1
    return [row[column_image_left] for row in matrix]

def get_image_right_values(matrix):
    column_image_right = 2
    return [row[column_image_right] for row in matrix]

def get_steering_values(matrix):
    column_steering = 3
    return [float(row[column_steering]) for row in matrix]

def get_throttle_values(matrix):
    column_throttle = 4
    return [float(row[column_throttle]) for row in matrix]

def get_brake_values(matrix):
    column_brake = 5
    return [float(row[column_brake]) for row in matrix]

def get_speed_values(matrix):
    column_speed = 6
    return [float(row[column_speed]) for row in matrix]
