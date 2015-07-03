import pandas

def add_full_name(path_to_csv, path_to_new_csv):
    #Assume you will be reading in a csv file with the same columns that the
    #Lahman baseball data set has -- most importantly, there are columns
    #called 'nameFirst' and 'nameLast'.
    #1) Write a function that reads a csv
    #located at "path_to_csv" into a pandas dataframe and adds a new column
    #called 'nameFull' with a player's full name.
    #
    #For example:
    #   for Hank Aaron, nameFull would be 'Hank Aaron', 
	#
	#2) Write the data in the pandas dataFrame to a new csv file located at
	#path_to_new_csv

    #WRITE YOUR CODE HERE
        originalData = pandas.read_csv(path_to_csv)
        originalData['nameFull'] = originalData['nameFirst'] + " "+ originalData['nameLast']
        originalData.to_csv(path_to_new_csv)
        print originalData['nameFull']




path_to_csv = 'files/input/lahman-csv_2015-01-24/Master.csv'
path_to_new_csv = 'files/output/out_lahman-csv_2015-01-24/Master.csv'
add_full_name(path_to_csv, path_to_new_csv)