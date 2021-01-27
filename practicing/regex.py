import re

"""
Regular Expressions
^ Start
$ Stop
. Any character
* Match one character 0+ times
+ Match one character 1+ times
? Non-greedy
\s Whitespace
\S Non-whitespace
[abc] Match one character in the specified set
[^abc] Match one character not in the specified set
"""

# myString = 'Send an email from this@email.com to test@user.com 34 times.'

# result = re.findall('\S+@\S+', myString)
# print(result)

text = open('shakespear.txt')

for line in text:
    line = line.rstrip()
    if re.search('^A.+$', line):
        print(line)