# create a mapping of states / territories to abbreviation
states = {
	'New South Wales': 'NSW',
	'Victoria': 'Vic',
	'Tasmania': 'Tas',
	'South Australia': 'SA',
	'Western Australia': 'WA',
	'Queensland': 'Qld',
	'Australian Capital Territory': 'ACT',
	'Northern Territory': 'NT'
}

# create a basic set of states and some cities in them
cities = {
	'NSW': 'Dubbo',
	'Vic': 'Ballarat',
	'Tas': 'Geeveston',
	'SA': 'Adelaide',
	'WA': 'Margaret River',
	'Qld': 'Cairns'
}

# add some more cities
cities['NT'] = 'Alice Springs'
cities['ACT'] = 'Fishwyck'

# print out some cities
print '_' * 10
print "Tas State has: ", cities['Tas']
print "Qld State has: ", cities['Qld']

# print some states
print '_' * 10
print "Western Australia's abbreviation is: ", states['Western Australia']
print "Victoria's abbreviation is: ", states['Victoria']

# do it by using the state then cities dict
print '_' * 10
print "New South Wales has: ", cities[states['New South Wales']]
print "Northern Territory has: ", cities[states['Northern Territory']]

# print every state abbreviation
print '_' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '_' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '_' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (
		state, abbrev, cities[abbrev])

print '_' * 10
# safely get an abbreviation by state that might not be there
state = states.get('Inebriated', None)

if not state:
	print "Sorry, no Inebriation."

# get a city with a default value
city = cities.get('IN', 'Does Not Exist')
print "The city for the state of 'IN' is: %s" % city
