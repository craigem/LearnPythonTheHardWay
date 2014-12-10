"""Exercise 39, Learning Python the Hard Way"""
# create a mapping of states / territories to abbreviation
STATES = {
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
CITIES = {
    'NSW': 'Dubbo',
    'Vic': 'Ballarat',
    'Tas': 'Geeveston',
    'SA': 'Adelaide',
    'WA': 'Margaret River',
    'Qld': 'Cairns'
}

# add some more cities
CITIES['NT'] = 'Alice Springs'
CITIES['ACT'] = 'Fishwyck'

# print out some cities
print '_' * 10
print "Tas State has: ", CITIES['Tas']
print "Qld State has: ", CITIES['Qld']

# print some states
print '_' * 10
print "Western Australia's abbreviation is: ", STATES['Western Australia']
print "Victoria's abbreviation is: ", STATES['Victoria']

# do it by using the state then cities dict
print '_' * 10
print "New South Wales has: ", CITIES[STATES['New South Wales']]
print "Northern Territory has: ", CITIES[STATES['Northern Territory']]

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
STATE = STATES.get('Inebriated', None)

if not STATE:
    print "Sorry, no Inebriation."

# get a city with a default value
CITY = CITIES.get('IN', 'Does Not Exist')
print "The city for the state of 'IN' is: %s" % CITY
