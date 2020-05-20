from passlib.hash import sha512_crypt
from progress.bar import Bar
import sys

if len(sys.argv) > 3:
    print("Given too many arguments! Please run in this format: python run.py ciphertextfile [mode].If you have question please read READ.md.")
    exit()
if len(sys.argv) < 2:
    print("The argument you give is too less. Please run in this format: python run.py ciphertextfile [mode].If you have question please read READ.md.")
    exit()
print("[!] legal disclaimer: Usage of this project for decode password of attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program\n\n\n")
ciphertext_f = sys.argv[1]
ciphertext_f0 = open(ciphertext_f,"r+")
ciphertext = ciphertext_f0.readline().strip()
mode = 2

if len(sys.argv) == 3:
    mode = int(sys.argv[2])

def decode(ciphertext,mode):

    file0 = None

    if mode == 1:
        file0 = open("mode1.txt","r+")
    elif mode == 2:
        file0 = open("mode2.txt","r+")
    else:
        file0 = open("mode3.txt","r+")
    cipher_list = ciphertext.split(":")[1].split("$")

    if cipher_list[1] != "6":
        print("It is not hashed by SHA-512! Only when the number after the first $ sign is 6, it is SHA-512 hashing.")
        exit()
    else:
        salt0 = cipher_list[2]
        if len(salt0) != 16:
            print("length of salt is not equal to 16!")
        ct = cipher_list[3]
        fw = file0.readlines()
        compare = '$6$'+salt0+'$'+ct
        bar = Bar('Processing', max = len(fw), fill = '♡')
        for i in range(len(fw)):
            bar.next()
            test = fw[i].strip()
            h_test = sha512_crypt.using(salt=salt0,rounds=5000).hash(test)
            if h_test == compare:
                print("\n")
                print("solved!!!")
                print("The password is: {}".format(test))
                bar.finish()
                exit()
        bar.finish()

    if mode in [1,2]:
        print("Cannot find password. You can try the higher mode.")
        exit()
    elif mode == 3:
        print("Looks like it is a very complex password. Sorry I cannot decode it.")
        exit()

decode(ciphertext,mode)
