import subprocess, time

path1 = "/home/luka/kriptonavti/kriptonavti/bin/bitcoin-cli"
path2 = "-datadir=/home/luka/kriptonavti/data/net"

subprocess.run([path1, path2, "generate","100"])
bool = True
while bool == True:
    subprocess.run([path1, path2, "generate","1"])
    time.sleep(15)
    print('Number of connected devices')
    subprocess.run([path1, path2, "getconnectioncount"])

