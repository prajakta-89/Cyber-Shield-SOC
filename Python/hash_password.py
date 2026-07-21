import bcrypt


password = "admin123"


hashed = bcrypt.hashpw(

    password.encode(),

    bcrypt.gensalt()

)


print(hashed.decode())


passwords = [
    "analyst123",
    "viewer123"
]


for password in passwords:

    hashed = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    print(password)
    print(hashed.decode())
    print("----------------")