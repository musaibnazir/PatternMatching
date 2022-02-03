import re

vowelRegex = re.compile(r'[aeiouAEIOU]')
m = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(m)

consonantRegex = re.compile(r'[^aeiouAEIOU]')
m1= consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(m1)
