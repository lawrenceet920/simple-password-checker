# Ethan Lawrence
# dec 13 2024
# password checker

password = input("Type your password:   ")
score = 0

lowercase = False
uppercase = False
number = False
special_char = False

for character in password:
    if character in "abcdefghijklmnopqrstuvwxyz":
        lowercase = True
    elif character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        uppercase = True
    elif character in "1234567890":
        number = True
    else:
        special_char = True
else: # For loop "character in password"
    if len(password)>=8:
        score += 5
        print('Your passoword has at least 8 characters.')

# Describe Password
if lowercase:
    print('Your passoword has at least 1 lowercase character.')
if uppercase:
    print('Your passoword has at least 1 uppercase character.')
if number:
    print('Your passoword has at least 1 number.')
if special_char: 
    print('Your passoword has at least 1 number.')

# Score Password
if uppercase and lowercase:
    score += 10
if number and (lowercase or uppercase):
    score += 10
if special_char:
    score += 5
    
print()
print(f'Score: {score}')