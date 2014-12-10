"""Exercise 39, Learning Python the Hard Way"""
# create a mapping of state to abbreviation
STATES = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
CITIES = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
CITIES['NY'] = 'New York'
CITIES['OR'] = 'Portland'

# print out some cities
print '_' * 10
print "NY State has: ", CITIES['NY']
print "OR State has: ", CITIES['OR']

# print some states
print '_' * 10
print "Michigan's abbreviation is: ", STATES['Michigan']
print "Florida's abbreviation is: ", STATES['Florida']

# do it by using the state then cities dict
print '_' * 10
print "Michigan has: ", CITIES[STATES['Michigan']]
print "Florida has: ", CITIES[STATES['Florida']]

# print every state abbreviation
print '_' * 10
for STATE, abbrev in STATES.items():
    print "%s is abbreviated %s" % (STATE, abbrev)

# print every city in state
print '_' * 10
for abbrev, CITY in CITIES.items():
    print "%s has the city %s" % (abbrev, CITY)

# now do both at the same time
print '_' * 10
for STATE, abbrev in STATES.items():
    print "%s state is abbreviated %s and has city %s" % (
        STATE, abbrev, CITIES[abbrev])

print '_' * 10
# safely get an abbreviation by state that might not be there
STATE = STATES.get('Texas', None)

if not STATE:
    print "Sorry, no Texas."

# get a city with a default value
CITY = CITIES.get('TX', 'Does Not Exist')
print "The city for the state of 'TX' is: %s" % CITY
