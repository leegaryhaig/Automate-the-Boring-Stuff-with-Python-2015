import re
# Matching complicated patterns might require long, convoluted regexes, you can
# mitigate this by tell the re.compile() function to ignore whitespace as well
# comments inside the regex string. This "verbose" mode can be enable by passing
# the variable re.VERBOSE as the second argument to re.compile


phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

# VERSUS

verbosePhoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?           # area code
    (\s|-|\.)?                   # separator
    \d{3}                        # first 3 digits
    (\s|-|\.)                    # separator
    \d{4}                        # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})? # extension
    )''', re.VERBOSE)

# Note how the previous example uses the triple-quote syntax(''') to create a
# multiline string so that you can spread the regex definition over many lines/
# extra spaces inside the multiline string for regexs are not considered part of
# the text pattern to be matched.


# Combing re.IGNORECASE, re/DOTALL, re/VERBOSE
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
mo = someRegexValue.findall('FOO       FoO  foofoofoo')
print(mo)
