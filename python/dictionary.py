'''
Please do not uncomment this, since its not a piece of code, it is just for visualization

{
'a': 
	{ 
		'1': {'count': 0, 'results': [{'grade': 'ok', 'rc': 0}, {'grade': 'warning', 'rc': 1}]}, 
		'2': {'count': 0, 'results': [{'grade': 'ok', 'rc': 0}, {'grade': 'warning', 'rc': 1}]}, 
		'3': {'count': 0, 'results': [{'grade': 'ok', 'rc': 0}, {'grade': 'warning', 'rc': 1}]}, 
		'4': {'count': 0, 'results': [{'grade': 'ok', 'rc': 0}, {'grade': 'warning', 'rc': 1}]}, 
		'5': {'count': 0, 'results': [{'grade': 'ok', 'rc': 0}, {'grade': 'warning', 'rc': 1}]} 
	}, 
'c': 
	{ 
		'1': {'count': 0, 'results': [{'grade': 'ok', 'rc': 0}, {'grade': 'warning', 'rc': 1}]}, 
		'2': {'count': 0, 'results': [{'grade': 'ok', 'rc': 0}, {'grade': 'warning', 'rc': 1}]}, 
		'3': {'count': 0, 'results': [{'grade': 'ok', 'rc': 0}, {'grade': 'warning', 'rc': 1}]}, 
		'4': {'count': 0, 'results': [{'grade': 'ok', 'rc': 0}, {'grade': 'warning', 'rc': 1}]}, 
		'5': {'count': 0, 'results': [{'grade': 'ok', 'rc': 0}, {'grade': 'warning', 'rc': 1}]} 
	}, 
'b': 
	{ 
		'1': {'count': 0, 'results': [{'grade': 'ok', 'rc': 0}, {'grade': 'warning', 'rc': 1}]}, 
		'2': {'count': 0, 'results': [{'grade': 'ok', 'rc': 0}, {'grade': 'warning', 'rc': 1}]}, 
		'3': {'count': 0, 'results': [{'grade': 'ok', 'rc': 0}, {'grade': 'warning', 'rc': 1}]}, 
		'4': {'count': 0, 'results': [{'grade': 'ok', 'rc': 0}, {'grade': 'warning', 'rc': 1}]}, 
		'5': {'count': 0, 'results': [{'grade': 'ok', 'rc': 0}, {'grade': 'warning', 'rc': 1}]} 
	} 
} 

'''
'''
	1. Access dictionary elements using keys
	2. Access list elements using indices
'''

#create above dictionary

L1 = ['a','b','c']
L2 = ['1','2','3','4','5'] 
res_list = [
	 {'grade': 'ok', 'rc': 0}, 
	 {'grade': 'warning', 'rc': 1} 
 ] 
sub_dict = {
	 'count': 0, 
	 'results': res_list
 } 
my_dict = {}
for l1 in L1:
	my_dict[l1] = {}

for l1 in L1: 
	for l2 in L2: 
		my_dict[l1][l2] = sub_dict 


# THE PLAYGROUND : uncomment the appropriate sections below to see the results

'''
#print the entire dictionary
print my_dict
'''

'''
#print outer keys i.e. a,b,c
for keys in my_dict.keys():
	print keys
'''

'''
#print outer values
for values in my_dict.values():
	print values
'''

'''
#print outer keys and values
for keys, values in my_dict.iteritems():
	print keys, values
'''

'''
#print values corresponding to key 'a'
print my_dict['a']
'''

'''
#print values corresponding to key '1' of the inner dictionary and its values
print my_dict['a']['1']
print my_dict['a']['1']['count'] #prints 0
print my_dict['a']['1']['results'] #prints a list [{'grade': 'ok', 'rc': 0}, {'grade': 'warning', 'rc': 1}]
'''

'''
#printing the values of innermost list (accessed using index)
print my_dict['a']['1']['results'][0] #prints {'grade': 'ok', 'rc': 0}
print my_dict['a']['1']['results'][1] #prints {'grade': 'warning', 'rc': 1}
'''

'''
#printing the values of the innermost dictionary
print my_dict['a']['1']['results'][0]['grade'] #prints 'ok'
'''


#iterating over the above dictionary 
'''
'for keys in my_dict.keys()' isEqualTo 'for keys in my_dict' [since .keys() is default looping criteria in dict loops]
alternatively we can iterate through values, or (keys, values) in the following loops using .values() and .iteritems() as explained above
'''
for keys in my_dict.keys():
	for keys1 in my_dict[keys].keys():
		for keys2 in my_dict[keys][keys1].keys():
			if keys2 == 'results':
				for x in xrange( 0,len(my_dict[keys][keys1][keys2])):
					#print my_dict[keys][keys1][keys2][x]
					for keys3 in my_dict[keys][keys1][keys2][x].keys():
						print my_dict[keys][keys1][keys2][x][keys3]

