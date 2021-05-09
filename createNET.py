#install required modules
import subprocess, os, shutil, csv

path = '/home/luka/kriptonavti/data'
path2 = '/home/luka/kriptonavti/kriptonavti/bin/bitcoind'

#download and install bitcoin sv

print("Do you want to download the file? [y/n]")

answer1 = str(input())

if answer1 == str("y"):
    subprocess.run(["wget","https://download.bitcoinsv.io/bitcoinsv/1.0.5/bitcoin-sv-1.0.5-x86_64-linux-gnu.tar.gz"])
    
    subprocess.run(["tar","xvf","bitcoin-sv-1.0.5-x86_64-linux-gnu.tar.gz"])
    subprocess.run(["ln","-s","bitcoin-sv-1.0.5","kriptonavti"])
    try:
        os.mkdir(path)
    except:
        pass
    try:
        os.mkdir(path + '/net')
    except:
        pass
    with open(path + "/net/bitcoin.txt","w") as f:
        f.write("regtest=1\n")
        f.write("rpcuser=user\n")
        f.write("rpcpassword=geslo123\n")
        f.write("debug=1\n")
        f.write("debugexclude=libevent\n")
        f.write("debugexclude=leveldb\n")
        f.write("printtoconsole=1\n")
        f.write("excessiveblocksize=0\n")
        f.write("maxstackmemoryusageconsensus=0\n")
        f.write("port=8300\n")
        f.write("rpcport=8301\n")
    os.rename(path + "/net/bitcoin.txt", path + "/net/bitcoin.conf")
    print("Install completed, do you want to run nod[y/n]?")
    answer2 = str(input())
    if answer2 == str("y"):
        subprocess.run([path2,"-datadir=" + path +"/net"])
        pass
else:
    pass