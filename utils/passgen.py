import string
import random

def generate_rand_pass(password_len):
    characters = list(string.ascii_letters + string.digits + "!@##$%&")
    random.shuffle(characters)

    gen_pass =[]

    for x in range(password_len):
        gen_pass.append(random.choice(characters))

    random.shuffle(gen_pass)
    return gen_pass



while True:

    pass_string = input("Do you want to generate a password ? ")

    if pass_string == 'y' or pass_string == 'Y':
        password_len = int(input("How long do you want your password ?"))
        gen_pass = generate_rand_pass(password_len)
    else:
        quit()

    print("Generated Password: ",str(gen_pass))
