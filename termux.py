#!/data/data/com.termux/files/usr/bin/python3
import os
import time
import sys

os.system("clear")

print('''\033[91m
    ••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
 ____  _   _    _    ____   _____        __
/ ___|| | | |  / \  |  _ \ / _ \ \      / /
\___ \| |_| | / _ \ | | | | | | \ \ /\ / /
 ___) |  _  |/ ___ \| |_| | |_| |\ V  V /
|____/|_| |_/_/   \_\____/ \___/  \_/\_/       CREATED BY  MR_SHADOW
  ''')
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 10000)

print (''' \033[95m
+--------------------------------------+
| This Tool Install All Basic Packages |
+--------------------------------------+
| Coded By  @MR_Shadow_1 |version : 1.0|
+--------------------------------------+''')
slowprint(''' \033[93m
[01] python             [02] python2
[03] python-dev         [04] python3
[05] php                [06] java
[07] git                [08] perl
[09] bash               [10] nano
[11] curl               [12] openssl
[13] openssh            [14] wget
[15] clang              [16] nmap
[17] w3m                [18] hydra
[19] ruby               [20] macchanger
[21] host               [22] dnsutils
[23] coreutils          [24] fish
[25] zip                [27] tor
[28] hydra              [29] figlet 
[30] cowsay             [31] tar
[32] unzip              [33] vim
[34] ruby               [35] wcalc
[36] bmon               [37] unrar
[38] proot              [39] golang
[40] NsLookup           [41] cmatrix
[42] hollywood''')
slowprint('''\033[96m
This Command for access Storage in Termux
[00] termux-setup-storage''')
print ("                                            ")
choice = input("\033[93mDo You Want to Install All Packages [y/n] : ")
if choice == 'n' : sys.exit()
if choice == 'y' : os.system ("apt update")
os.system ("apt upgrade -y")
os.system ("apt install python -y")
os.system ("apt install python2 -y")
os.system ("apt install php -y")
os.system ("apt install python-dev -y")
os.system ("apt install python3 -y")
os.system ("apt install java -y")
os.system ("pkg install root-repo -y")
os.system ("pkg install unstable-repo -y")
os.system ("pkg install x11-repo -y")
os.system ("apt install git -y")
os.system ("apt install perl -y")
os.system ("apt install bash -y")
os.system ("apt install cmatrix -y")
os.system ("apt install hollywood -y")

print ("wait for second and start hacking #MR_SHADOW" )

os.system ("apt install nano -y")
os.system ("apt install curl -y")
os.system ("apt install openssl -y")
os.system ("apt install openssh -y")
os.system ("apt install wget -y")
os.system ("apt install clang -y")
os.system ("apt install nmap -y")
os.system ("apt install w3m -y")
os.system ("apt install hydra -y")
os.system ("apt install ruby2 -y")
os.system ("apt install macchanger -y")
os.system ("apt install host -y")
os.system ("apt install dnsutils -y")
os.system ("apt install coreutils -y")
os.system ("apt install fish -y")
os.system ("apt install zip -y")
os.system ("apt install hydra -y")
os.system ("apt install figlet -y")
os.system ("apt install cowsay -y")
os.system ("apt install unzip -y")
os.system ("apt install vim -y")
os.system ("apt install ruby -y")
os.system ("apt install wcalc -y")
os.system ("apt install bmon -y")
os.system ("apt install unrar -y")
os.system ("apt install proot -y")
os.system ("apt install golang -y")
os.system ("pkg install dnsutils -y")
print ("Allow the Button For Access the Storage in Termux")


os.system ("termux-setup-storage")
 

