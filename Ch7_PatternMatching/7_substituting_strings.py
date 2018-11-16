import re
# Regex's can also substitute new text in place of patterns with the sub() method
# First arg is a string to replace matches, second is the string for Regex
namesRegex = re.compile(r'Agent \w+')
mo = namesRegex.sub('CENSORED', 'Agent Alice gave the secret document to Agent Bob.')
print(mo)

# Sometimes you need to use the matches text itself as part of the substitution
# In the first arg of sub() you can type \1, \2, \3 to mean 'Enter the text of
# group 1, 2, 3' in the sub
agentsNamesRegex = re.compile(r'Agent (\w)\w*')
mo = agentsNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(mo)
