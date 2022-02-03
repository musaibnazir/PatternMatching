#Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE
import re

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
