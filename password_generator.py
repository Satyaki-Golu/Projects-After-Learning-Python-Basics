# Password Generator Python Code

import subprocess
import os
import time
import secrets
import string

chars = string.ascii_letters + string.digits + string.punctuation

def clear():
    if os.name == 'nt':
        subprocess.call('cls', shell=True)
    else:
        subprocess.call('clear', shell=True)

clear()

while True:
    try:
        length = int(input('enter the length of the password: '))
    except ValueError:
        print("please enter a number ")
    else:
        if length < 1 or length > 100:
            print('please enter a number between 1 and 100: ')
        else:
            break

def wait():
    time.sleep(12)

def create_password():
    password = ''
    for _ in range(length):
        password += secrets.choice(chars)
    print(password)

def main():
    global length, password
    password = ''
    while True:
        print('Creating password! please Wait for 12 seconds')

        # TODO: remove the # or add the # for checking the code
        wait()

        create_password()

        input('press enter to continue. ')
        password = ''

        start = input('press n to stop or press enter to continue: ').casefold()

        clear()

        if start == 'n':
            break
            print('I am happy that you used my program 😀'
                  '\nThank you for using my program\n'
                  'created by Satyaki Debnath\n'
                  'created with following every PEP - 8 style\n'
                  'My Project - Password Generator\n')

if __name__ == '__main__':
    main()

'''
### Description about this code: 

Finally we have created our python password generator
and it works very at good it has clear function clearing
the terminal. It has a very good platform compatibility
and one rule only if you have run the code you should have
to create a password at least one time (once).
'''

# You can find my code in this website link in case you want to use this code:
# Created using PEP - 8 Stylings
