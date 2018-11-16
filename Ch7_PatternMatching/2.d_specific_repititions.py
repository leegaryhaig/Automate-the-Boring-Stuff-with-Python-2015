import re
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())

mo2 = haRegex.search('Ha')
print('mo2 == None: ' + str(mo2 == None))

haRangeRegex = re.compile(r'(Ha){,5}')
mo3 = haRangeRegex.search('HaHaHaHaHa')
mo4 = haRangeRegex.search('Ha')
print(mo3.group())
print(mo4.group())
