import re

#In addition to search() method Regex objects also have a findall() method
#The findall() method will return the strings of every match in the
#searched strings - for example
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall('Cell: 858-216-6940 Work: 212-555-0000')
print(mo)
#Does not return a Match object, but a list of strings - as long as there
#there are no groups in the regex

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') #has groups
mo = phoneNumRegex.findall('Cell: 858-216-6940 Work: 212-555-0000')
print(mo)
#if there are groups in the regex then findall() will return list of tuples
 
