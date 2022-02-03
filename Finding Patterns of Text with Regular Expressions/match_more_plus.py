import re

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventure of Batwoman')
print(mo1.group())

mo2 = batRegex.search('The Adventure of Batwowowoman.')
print(mo2.group())

mo3 = batRegex.search('The Adventure of Batman')
print(mo3 == None)
