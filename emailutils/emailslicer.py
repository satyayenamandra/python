#collect email from user
#split the email using @, the first part as the user name, second part as domain
#split doamin using .

def main():
    email_input = input("Input your email address: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username: ",username)
    print("Domain: ",domain)
    print("Extension: ",extension)

while True:
    main()

