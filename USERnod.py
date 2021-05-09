import subprocess
from scanner import Scanner

path1 = "/home/luka/kriptonavti/kriptonavti/bin/bitcoin-cli"
path2 = "-datadir=/home/luka/kriptonavti/data/USER"


subprocess.run([path1,path2,"generate", "220"])

bool = True
while bool == True:
    print('\n--------------------\nHello user! Your balance = ',)
 
    subprocess.run([path1,path2,"getbalance"])
    print('What would you like to do next? Here are your options:')
    print('--------------------')
    print('press 1 = Scan items you would like to buy! \npress 2 = Mine! Mine! Mine! \npress 3 = Thats all ty!')

    ans1 = str(input())

    if ans1 == str("1"):
        #price = scaner.scan
        price = Scanner().scan()
        #manjka še import in run PAZI!!
        print('\n--------------------\nTotal value of your items is:', price)
        print('\nWould you like to pay with bitcoin SV [y/n]')
        ans2 = str(input())
        if ans2 == str("y"):
            print("\n--------------------\nYou need to add SHOP's address! Your input should be address only!")
            address = str(input())
            print('\n--------------------\nConfirm your payment!\nValue =', price,"\naddress =", address)
            print('Is that correct? [y/n]')
            ans3 = str(input())
            if ans3 == str("y"):
                print("\n--------------------\nYour payment recieved!")
                subprocess.run([path1,path2,"sendtoaddress", f'{address}',f'{price}'])

    if ans1 == str("2"):
        subprocess.run([path1,path2,"generate", "220"])
        print('\nThats all i can do in one round \n :(')

    if ans1 == str("3"):
        break

