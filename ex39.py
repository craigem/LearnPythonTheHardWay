# create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
	'CA': 'Sand Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '_' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']
