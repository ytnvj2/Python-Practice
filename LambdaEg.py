# Create a list of strings: spells
spells = ["protego", "accio", "expecto patronum", "legilimens"]

# Use map() to apply a lambda function over spells: shout_spells
shout_spells = map(lambda spell: spell+'!!!', spells)

# Convert shout_spells to a list: shout_spells_list
shout_spells_list=list(shout_spells)

# Convert shout_spells into a list and print it
print(shout_spells_list)


# Import reduce from functools
from functools import reduce;

# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'eddard', 'jon']

# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda s1,s2:s1+s2, stark)

# Print the result
print(result)
