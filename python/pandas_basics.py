import pandas as pd
'''
Pandas provides high-performance data structures and data analysis tools.
	1. DataFrame object for data manipulation with integrated indexing.
	2. data alignment and handling missing data.
	3. reshaping and vivoting datasets.
	4. slicing, fancy indexing, and subsetting.
	5. Hierarchical axis indexing.
	6. Time series-functionality. etc.

	refer http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/
'''

#Part -1 Series
# Series is a one dimensional object

#default indexing (0 to n-1)
series = pd.Series(['Dave', 'Cheng-Han', 'Udacity', 42, -1789710578])
print series, "\n",series[0]

#explicit indexing
series = pd.Series(['Dave', 'Cheng-Han', 359, 9001],index=['Instructor', 'Curriculum Manager','Course Number', 'Power Level'])
print series, "\n", series['Course Number'], "\n", series[['Course Number', 'Power Level']]

#booean operators to select items from series
series = pd.Series([1, 2, 3, 4, 5], index=['Cockroach', 'Fish', 'Mini Pig',
                                                 'Puppy', 'Kitten'])
print series > 3
print series[series > 3]

#Part -2 DataFrame
# It is similar to a spreadsheet/relational_table
'''
To create a dataframe, first create a dictionary of lists
1) The key of the dictionary will be the column name.
2) The associating list will be the values within that column.
'''
data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'], 'wins': [11, 8, 10, 15, 11, 6, 10, 4], 'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
football = pd.DataFrame(data)
print football, "\n"

#some basic analysis of dataframe
#datatype for each column
print football.dtypes, "\n" 
#basic statistics of the dataframe's numerical columns
print football.describe(), "\n"
#first five rows
print football.head(), "\n"
#last five rows
print football.tail(), "\n"