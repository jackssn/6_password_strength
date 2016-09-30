import string

def get_password_strength(password):
    length = len(password)
    numbers = sum(c.isdigit() for c in password)
    lowercases = sum(c.islower() for c in password)
    uppercases = sum(c.isupper() for c in password)
    punctuations = 0
    letters = len(set(password))
    for s in password:
        if s in string.punctuation:
            punctuations += 1

    if length >= 15:
        k = 1.75
    elif length >= 10:
        k = 1.6
    elif length >= 5:
        k = 1.5
    else:
        k = 1

    if letters >= 15:
        kk = 1.5
    elif letters >= 10:
        kk = 1.1
    elif letters >= 5:
        kk= 1
    else:
        kk = 0.7

    if numbers >= 6:
        kn = 1.5
    elif numbers >= 4:
        kn = 1.3
    elif numbers >= 2:
        kn = 1
    else:
        kn = 0

    if lowercases >= 6:
        kl = 1.5
    elif lowercases >= 4:
        kl = 1.3
    elif lowercases >= 2:
        kl = 1
    else:
        kl = 0

    if uppercases >= 6:
        ku = 1.5
    elif uppercases >= 4:
        kn = 1.3
    elif uppercases >= 2:
        ku = 1
    else:
        ku = 0

    if punctuations >= 6:
        kp = 1.5
    elif punctuations >= 4:
        kn = 1.3
    elif punctuations >= 2:
        kp = 1
    else:
        kp = 0

    result = int(k*kk*(kl+kn+ku+kp))

    if result > 10: result = 10
    elif result == 0: result = 1

    return result

if __name__ == '__main__':
    while 1:
        password = input("Type your password: ").split(' ')
        if len(password) > 1 or not password:
            print('Incorrect password. Try again')
        else:
            break
    print("Difficulty of password: %s/10" % get_password_strength(password[0]))