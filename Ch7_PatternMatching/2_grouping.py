import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phoneNumRegex.search('My Number is 858-216-6940')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.groups()) #note: THE PLURAL form in the last line

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo1.group())
print(mo2.group())
