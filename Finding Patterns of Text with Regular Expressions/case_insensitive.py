import re  

robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoboCop is skdnsk dksnk k').group())
print(robocop.search('ROBOCOP protects the innocent.').group())
print(robocop.search('Al, why does your programming book talk about robocop so much?').group())
