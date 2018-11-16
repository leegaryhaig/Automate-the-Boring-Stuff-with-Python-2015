import re
#By default Python's regex are greedy
#In ambigious situations they will match the longest string possible
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())


#? can have two seperate unrelated meanings: nongreedy match or flagging
# an optional group
nonGreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nonGreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())
