import csv

with open('databaselol.csv') as database:
    format_data = list(csv.DictReader(database, fieldnames=["username", "password", "fullname", "extra"]))


def separate():
    print("................")


def init_user():
    new_user = input("New username: ")
    new_password = input("New password: ")
    new_fullname = input("Input your fullname: ")
    new_extra_data = input("Write some information about you: ")
    for line in format_data:
        if new_user == line['username']:
            print("Sorry, something went wrong with that request! Please try a different combination.")
            login()

        else:
            f = open('databaselol.csv', 'a')

            f.write("{},{},{},{}\n".format(new_user, new_password, new_fullname, new_extra_data))
            f.close()
            real_database(line)


def real_database(line):
    print("Welcome: {}".format(line["fullname"]))
    print(line["extra"])
    # print("Welcome: {}".format("hi"))
    action = input("(A)dd new user? (L)ogout? Change (I)nformation?>>>").lower()
    if action == 'a':
        print('add')
        init_user()
    else:
        print("goodbye")
        login()


def login():

    with open('databaselol.csv') as database:
        format_data = list(csv.DictReader(database, fieldnames=["username", "password", "fullname", "extra"]))

    print(".....Login.....")
    username = input("Input username: ")
    separate()
    password = input("Input password: ")
    separate()

    for line in format_data:
        if username == line['username'] and password == line['password']:
            print("login successful")
            real_database(line)
            break
    else:
        print("login failed")


login()
