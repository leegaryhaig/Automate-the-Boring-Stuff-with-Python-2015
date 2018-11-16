import re

#create a function that acts like the strip method

def Stripper(string_to_strip, *char_to_strip):
    print("Original String: " + string_to_strip)

    space_regex = re.compile(r'\S{0,}\S')
    mo = space_regex.findall(string_to_strip)
    print('Without Whitespace: '+ str(mo))

    char_regex = re.compile(str(char_to_strip))
    mo2 = char_regex.sub('', string_to_strip)
    print('Without Char: ' + str(mo2))


#NOT DONE