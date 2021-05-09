import subprocess, os

path = "/home/luka/kriptonavti/data/SHOP"

print("Do you wanna set up shop? [y/n]")
answer1 = str(input())

if answer1 == str("y"):
    try:
        os.mkdir(path)
    except:
        pass
    with open(path + "/bitcoin.txt","w") as f:
        f.write("regtest=1\n")
        f.write("rpcuser=user\n")
        f.write("rpcpassword=geslo123\n")
        f.write("debug=1\n")
        f.write("debugexclude=libevent\n")
        f.write("debugexclude=leveldb\n")
        f.write("printtoconsole=1\n")
        f.write("excessiveblocksize=0\n")
        f.write("maxstackmemoryusageconsensus=0\n")
        f.write("port=8302\n")
        f.write("rpcport=8303\n")
        f.write("connect=127.0.0.1:8300\n")

    
    os.rename(path + "/bitcoin.txt", path + "/bitcoin.conf")
    
    print("Install completed, do you want to run nod[y/n]?")
    
    answer2 = str(input())
    if answer2 == str("y"):
        subprocess.run(["/home/luka/kriptonavti/kriptonavti/bin/bitcoind","-datadir=" + path])
