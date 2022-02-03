import re
beginWithHello = re.compile(r'^Hello')
m=beginWithHello.search('Hello World!')
print(m)
print(beginWithHello.search('He said Hello')==None)

endsWithNumber = re.compile(r'\d$')
m1=endsWithNumber.search('Your number is 42')
print(m1)
print(endsWithNumber.search('Your number is forty two.') == None)


wholeStringIsNum = re.compile(r'^\d+$')
m2=wholeStringIsNum.search('1234567890')
print(m2)
print(wholeStringIsNum.search('12345xyz67890') == None)
print(wholeStringIsNum.search('12 34567890') == None)
