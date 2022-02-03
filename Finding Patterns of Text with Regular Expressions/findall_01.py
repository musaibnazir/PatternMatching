import re

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo =  phoneNumberRegex.search('Cell: 123-122-1234  Work: 122-111-1111')
print(mo.group())

mo1 = phoneNumberRegex.findall('Cell: 123-122-1234  Work: 122-111-1111')
print(mo1)



phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo2 = phoneNumRegex.findall('Cell: 123-122-1234  Work: 122-111-1111')
print(mo2)


#Shorthand character class Represents
#\d Any numeric digit from 0 to 9.
#\D Any character that is not a numeric digit from 0 to 9.
#\w Any letter, numeric digit, or the underscore character.
#(Think of this as matching “word” characters.)
#\W Any character that is not a letter, numeric digit, or the
#underscore character.
#\s Any space, tab, or newline character. (Think of this as
#matching “space” characters.)
#\S Any character that is not a space, tab, or newline.


xmasRegex = re.compile(r'\d+\s\w+')
m1=xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(m1)
