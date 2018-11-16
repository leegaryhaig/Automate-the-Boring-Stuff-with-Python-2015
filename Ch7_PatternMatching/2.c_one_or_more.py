import re
# Matching one or more - unlike the star * which does not require  its group
# to appear in the matched string, the group preceding the plus must appear
# at least once
batRegex = re.compile(r'Bat(wo)+man')

mo1 = batRegex.search("The adventures of Batwoman")
print(mo1.group())

mo2 = batRegex.search('The adventures of Batwowowowoman')
print(mo2.group())

mo3 = batRegex.search('The adventures of Batman')
print('mo3 == None: ' + str(mo3 == None))
# None is true because the group (wo) does not appear even once.
