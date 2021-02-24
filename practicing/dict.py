# Using if statement 

name = 'Joe'
if name == 'Fred':
    print('Hello Fred')
elif name == 'Xander':
    print('Hello Xander')
elif name == 'Joe':
    print('Hello Joe')
elif name == 'Arnold':
    print('Hello Arnold')
else:
    print("I don't know who you are!")

# Using dictionaries 

names = {
    'Fred': 'Hello Fred',
    'Xander': 'Hello Xander',
    'Joe': 'Hello Joe',
    'Arnold': 'Hello Arnold'
}

print(names.get('Joe', "I don't know who you are!"))
print(names.get('Rick', "I don't know who you are!"))

# Conditional Expressions
age = 12
s = 'minor' if age < 21 else 'adult'

'yes' if ('qux' in ['foo', 'bar', 'baz']) else 'no'

