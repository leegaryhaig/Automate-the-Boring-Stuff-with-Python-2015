import re

#longhand
robocop = re.compile(r'robocop', re.IGNORECASE)
mo = robocop.search('RoboCop is part man, part machine, all cop.').group()
print(mo)

#shorthand
terminator = re.compile(r'back', re.I)
mo = terminator.search('I\'LL Be BACK').group()
print(mo)
