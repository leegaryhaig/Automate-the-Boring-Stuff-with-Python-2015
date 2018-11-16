import re

regex_object = {'longhand': "r'\d\d\d-\d\d\d-\d\d\d\d'",
                'shorthand': '\d{3}-\d{3}-\d{4}'
                }

phoneNumRegex = re.compile(regex_object['shorthand'])

# search() method searches the string it is passed for any matches to the regex
# Will return None if pattern isn't found and a Match object if pattern is found
mo = phoneNumRegex.search('My Number is 858-216-6940')

# Match objects have group() method that wil lreturn the actual matched text
print('Phone Number Found: ' + mo.group())

print(regex_object['longhand'])
# Why can't I use the longhand option even though the string seems to be exactly what re.compile uses?
