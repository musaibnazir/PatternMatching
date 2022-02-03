import re

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventure of Batman')
mo2 = batRegex.search('The Adventure of Batwoman')
mo3 = batRegex.search('The Adventure of Batwowowoman')

print(mo1.group())
print(mo2.group())
print(mo3.group())
