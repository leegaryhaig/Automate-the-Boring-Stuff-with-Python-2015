import re, pyperclip

# Searches your clipboard for all Phone numbers and Email Addresses
clip_var = pyperclip.paste()

# Regex patterns to find LJI emails and numbers
verbosePhoneRegex = re.compile(r'\d{3}-\d{4}', re.VERBOSE)

verboseEmailRegex = re.compile(r'[a-zA-Z0-9]+@[a-zA-Z0-9]+.org')

# Find matches in clipboard textself.
parsed_phone = []
parsed_email = []

parsed_phone = verbosePhoneRegex.findall(clip_var)
parsed_email = verboseEmailRegex.findall(clip_var)

pyperclip.copy(str(parsed_email) + str(parsed_phone))
[u'rjuarez@lji.org', u'aling@lji.org', u'amiller@lji.org', u'asutherland@lji.org'][u'752-6544', u'752-6584', u'752-6815', u'752-6951']
