import subprocess

path1 = "/home/luka/kriptonavti/kriptonavti/bin/bitcoin-cli"
path2 = "-datadir=/home/luka/kriptonavti/data/SHOP"

bool = True
while bool == True:
    print('\nState your buisness! \npress 1 = if you need address, \npress 2 = if u wanna know your balance, \npress 3 = Have a nice day! Ciao')

    answer = str(input())

    if answer == str("2"):
        print('\n--------------------\nYour balance is:')
        subprocess.run([path1, path2,"getbalance"])
        print('\n--------------------\n')
    if answer == str("1"):
        print('\n--------------------\nYour address is:')
        subprocess.run([path1, path2,"getnewaddress"])
        print('\n--------------------\n')
    if answer == str("3"):
        break

