from pandas import DataFrame, Series
import numpy

#job-1: create lists / Series
countries = ['Russian Fed.', 'Norway', 'Canada', 'United States','Netherlands', 'Germany', 'Switzerland', 'Belarus','Austria', 'France', 'Poland', 'China', 'Korea', 
'Sweden', 'Czech Republic', 'Slovenia', 'Japan','Finland', 'Great Britain', 'Ukraine', 'Slovakia','Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

#job-2: create DataFrame 
#(1st way, pass the lists)
df = DataFrame({'country_name' : countries,'gold'  : gold,'silver' :silver,'bronze' :bronze})
#(Alternate way, pass the Series)
df = DataFrame({'country_name' : Series(countries),'gold'  : Series(gold),'silver' :Series(silver),'bronze' :Series(bronze)})
#print one column
print df['country_name'], "\n"
#print multiple columns
print df[['country_name','bronze']]
#print a row based on index
print df.loc[5]
#print rows based on boolean condition
print df[df['bronze'] > 5]

#print average number of gold medals for the teams who have won at least one gold
avg_bronze_at_least_one_gold = df[df['gold']> 0]['bronze'].mean()
print avg_bronze_at_least_one_gold

#####
# Vectorized operations (operate itme by item)
####
print df
mean_of_given_columns = df[['bronze', 'gold', 'silver']].apply(numpy.mean)
print type(mean_of_given_columns)
#mean mean_of_given_columns is a series indexed with 'bronze', 'gold', 'silver'
print mean_of_given_columns['bronze']

#check which columns satisfy the criteria
print df['bronze'].map(lambda x: x >= 5)
print df[['bronze', 'gold', 'silver']].applymap(lambda x: x >= 5)

#numpy.dot() function (list-list ot list-matrix dot product)
point_value = [4, 2, 1]
list_total_points = numpy.dot(df[['gold', 'silver', 'bronze']], point_value)
#alternatively
list_total_points = numpy.dot(point_value, df[['gold', 'silver', 'bronze']].values.T.tolist())
print list_total_points
print df[['bronze', 'gold', 'silver']].values.T.tolist()
ndf = DataFrame({'country_name' : countries, 'points' : list_total_points})
print ndf