import re
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search("My number is 432-123-2111.")
print("Phone number found: ", mo.group())
phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
m = phoneNumberRegex.search("My number is 432-123-2111.")
print(m.group(1))
print(m.group(2))
print(m.group(0))
print(m.groups())
areacode, number = m.groups()
print("area code is: ",areacode)
print("number is: ",number)