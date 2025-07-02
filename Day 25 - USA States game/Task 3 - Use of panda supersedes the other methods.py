import pandas as pd
from pandas.core.internals.construction import dataclasses_to_dicts

# Todo: reading the CSV File.
            #  Todo 1: All functionalities are optional except for the path that leads to the csv file
data = pd.read_csv( "weather_data.csv")
print(data)

            #  Todo 2:Can print out the data for a column
                ## Assumes that the first name of all the rows will be the names. 
print(data["temp"])

            # Todo 3: Converting it into a dictionary
data_dict = data.to_dict()
print( data_dict)

            # Todo 4: Converting the series into a list
data_list  = data["temp"].to_list()
print (data_list)

            # Todo 5: Working out the mean of temperature series
data_temp_average= data["temp"].mean()
print( data_temp_average)

            # Todo 6: Pulling the maximum value of the temperatures.
data_temp_max =  data["temp"].max()
print( data_temp_max)