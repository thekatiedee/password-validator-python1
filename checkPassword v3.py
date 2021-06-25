# A password must have at least eight characters.
# A password must consist of only letters and digits - interpreting this as at least 1 letter.
# A password must contain at least two digits.

def validate():

    password = 'a'
    count = 0
    digits = 0
    letters = 0
    alphaNum = False
    password = input('Enter a password: ')

    # check for digits
    for i in password:
        if i.isdigit():
            digits += 1
    # # check for letters
    for j in password:
        if j.isalpha():
            letters += 1
    # check if alpha numeric
    for k in password:
        if k.isalnum():
            alphaNum = True
        else:
            alphaNum = False
    # check length and digits and if alpha numeric
    if (len(password) >= 8) and (digits >= 2) and (alphaNum is True) and (letters >= 1):
        print('This is a valid password.')
        # print('You have', letters, 'letters.')
        # print('You have', digits, 'digits.')
    else:
        print('This is an invalid password.')

validate()
