import re
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))



nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))




nongreedyRegex = re.compile(r'<.*?>')
mo1 = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo1.group())
greedyRegex = re.compile(r'<.*>')
mo2 = greedyRegex.search('<To serve man> for dinner.>')
print(mo2.group())



noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
newlineRegex = re.compile('.*', re.DOTALL)
print(newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
