import re
#      Shorthand Character Classes
# \d - Any numeric digit from 0 to 9.
# \D - Any character that is not a numeric digit from 0 to 9.
# \w - Any letter, numberic digit, or the underscore. ("word" characters)
# \W - Any character that is not a letter, numeric or underscore.
# \s - Any space, tab , or newline character. ("space" characters)
# \S - Any character that is not a space, tab or newline.

xmasRegex = re.compile(r'\d+\s\w+') #matching one or more with +
mo = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 3 birds, 3 hens, 2 doves, 1 patridge')
print(mo)

# Making your own stricter character classes by using square brackets []
vowelRegex = re.compile(r'[aeiouAEIOU]')
mo = vowelRegex.findall("BabyLegs eats adult food. ADULT FOOD. ")
print(mo)

# Making your own negative character classes by using caret character ^
consonantRegex = re.compile(r'[^aeiouAEIOU]')
mo = consonantRegex.findall("BabyLegs eats adult food. ADULT FOOD. ")
print(mo)

# Making your own stricter character classes by using ranges
consonantRegex = re.compile(r'[a-zA-Z0-9]')
mo = consonantRegex.findall("AbCdEfG1337@-_#")
print(mo)

# You can use caret (^) at the start of the regex to indicate a match must
# occur at the beginning of the searched string or a ($) at the end to
# indicate the string must end with this regex pattern.
beginsWithHello = re.compile(r'^Hello')
mo = beginsWithHello.search('Hello World!')
print(mo)
mo = beginsWithHello.search('He said hello')
print(mo)
# The # r'^\d+$' regex matches strings that both begin and end with one more
# numeric characters
wholeStringIsNum = re.compile(r'^\d+$')
mo = wholeStringIsNum.search('1234567890')
print(mo)

# The . (or dot) character in a regex is called a wildcard and will match any
# character except for a newline
atRegex = re.compile(r'.at')
mo = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo)

# [GREEDY] Match everything with Dot-Star(.*)
NameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = NameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))
# [NON-GREEDY] Match everything with Dot-Star-Question(.*?)
nonGreedyRegex = re.compile(r'<.*?>')
mo = nonGreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

# Matching Newline with the Dot character - all characters + newline
noNewLineRegex = re.compile('.*')
mo = noNewLineRegex.search('1 Serve the public trust.\nProtect the innocent\nUphold the law.').group()
print(mo)
newLineRegex = re.compile('.*', re.DOTALL)
mo = newLineRegex.search('2 Serve the public trust.\nProtect the innocent\nUphold the law.').group()
print(mo)
