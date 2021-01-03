menu = {}
menu['1']="Function 1." 
menu['2']="Function with login"
menu['3']="Function 3"
menu['4']="Exit"

while True: 
    options=menu.keys()
    for entry in options: 
        print(entry), menu[entry]

    selection=input("Please Select: ")
    if selection =='1': 
        lastname = input('Enter firstname: ')
        firstname = input('Enter lastname: ')
        age = input('Enter age: ')
        def func_1(firstname, lastname, age): 
            print('My name is {}'.format(firstname))
            print('My lastname is {}'.format(lastname))
            print('My age is {}'.format(age)) 
        res = func_1(lastname, firstname, age)

    elif selection == '2': 
        def pas(Login, password): 
            if password == '33':
                print('Welcome', Login)
            else:
                print('Access restricted')
        pas(input('Enter your name: '), password = input('Enter your password: '))
        

    elif selection == '3':
        firstname = input('Enter firstname: ')
        lastname = input('Enter lastname: ')
        age = int(input('Enter age: '))
        def func_3(firstname, lastname, age):
            if age > 18:
                return 'You are an adult'
            return 'You are too small' 
        a = firstname
        b = lastname
        c = age
        lol = func_3(a, b, c)
        print(func_3(a, b, c))

    elif selection == '4': 
        break
    else: 
        print("Unknown Option Selected!") 